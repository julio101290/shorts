#!/usr/bin/env python3
# ==========================================
# Auto uploader de Shorts a YouTube
# Usa Ollama local por CLI para metadata
# ==========================================

import os
import json
import shutil
import subprocess
import datetime
import re
import time
import random

# ==========================================
# CONFIGURACIÓN
# ==========================================
BASE_DIR = os.path.expanduser("~/shorts")
INBOX_DIR = os.path.join(BASE_DIR, "global", "inbox")
UPLOADED_DIR = os.path.join(BASE_DIR, "global", "uploaded")

OLLAMA_MODEL = "qwen2.5:14b"
VIDEO_EXTS = (".mp4", ".mov", ".mkv")

# ==========================================
# LOG
# ==========================================
def log(msg):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] {msg}")

# ==========================================
# JSON SAFE PARSER
# ==========================================
def extract_json(text):
    try:
        match = re.search(r"\{.*\}", text, re.S)
        if not match:
            return None

        raw = match.group(0)

        # Reparaciones comunes
        raw = raw.replace("\n", " ")
        raw = re.sub(r",\s*}", "}", raw)
        raw = re.sub(r",\s*]", "]", raw)

        return json.loads(raw)
    except Exception:
        return None

# ==========================================
# OLLAMA CLI
# ==========================================
def generate_metadata(video_name):
    prompt = f"""
Genera metadata para un SHORT DE BATERÍA.
NO inventes historias.

Devuelve SOLO JSON válido.

Formato:
{{
  "title": "...",
  "description": "...",
  "hashtags": ["#tag1", "#tag2", "#tag3"]
}}

Reglas:
- Título máximo 60 caracteres
- Descripción máximo 2 líneas
- Hashtags 5 a 8
- Idioma español
- Estilo directo, atractivo, no narrativo

Nombre del video: {video_name}
"""

    try:
        result = subprocess.run(
            ["ollama", "run", OLLAMA_MODEL, prompt],
            capture_output=True,
            text=True,
            timeout=120
        )
    except Exception as e:
        log(f"Ollama error: {e}")
        return None

    meta = extract_json(result.stdout)

    if not meta:
        log("Ollama devolvió JSON inválido")
        return None

    return meta

# ==========================================
# YOUTUBE UPLOAD (Modificado para Token persistente)
# ==========================================
def upload_youtube(video_path, meta):
    try:
        from google_auth_oauthlib.flow import InstalledAppFlow
        from googleapiclient.discovery import build
        from googleapiclient.http import MediaFileUpload
        from google.auth.transport.requests import Request
        from google.oauth2.credentials import Credentials
    except ImportError:
        log("Dependencias de YouTube no instaladas (instala google-api-python-client google-auth-oauthlib)")
        return False

    SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
    creds = None

    # Intentar cargar token guardado
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # Si no hay credenciales válidas, pedir login
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists("client_secrets.json"):
                log("YouTube error: client_secrets.json no encontrado")
                return False
            flow = InstalledAppFlow.from_client_secrets_file("client_secrets.json", SCOPES)
            creds = flow.run_local_server(port=0, prompt="consent")
        
        # Guardar el token para la próxima subida
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        youtube = build("youtube", "v3", credentials=creds)

        body = {
            "snippet": {
                "title": meta["title"],
                "description": meta["description"] + "\n\n" + " ".join(meta["hashtags"]),
                "tags": [h.replace("#", "") for h in meta["hashtags"]],
                "categoryId": "10"
            },
            "status": {
                "privacyStatus": "public",
                "selfDeclaredMadeForKids": False
            }
        }

        media = MediaFileUpload(video_path, resumable=True)

        request = youtube.videos().insert(
            part="snippet,status",
            body=body,
            media_body=media
        )

        response = request.execute()
        log(f"YouTube OK → videoId={response.get('id')}")
        return True

    except Exception as e:
        log(f"Error en la subida a YouTube: {e}")
        return False

# ==========================================
# MAIN
# ==========================================
def main():
    log("Entrando al main loop (SOLO YOUTUBE)")

    if not os.path.exists(INBOX_DIR):
        log("Inbox no existe")
        return

    # Obtenemos la lista de archivos válidos primero
    files_to_process = [f for f in os.listdir(INBOX_DIR) if f.lower().endswith(VIDEO_EXTS)]
    total = len(files_to_process)

    if total == 0:
        log("No hay videos para procesar en inbox.")
        return

    for i, file in enumerate(files_to_process):
        video_path = os.path.join(INBOX_DIR, file)
        log(f"Procesando ({i+1}/{total}): {file}")

        meta = generate_metadata(file)
        if not meta:
            log("Metadata inválida → skip")
            continue

        ok = upload_youtube(video_path, meta)
        if ok:
            shutil.move(
                video_path,
                os.path.join(UPLOADED_DIR, file)
            )
            log("Video movido a uploaded/")
            
            # --- LÓGICA DE SLEEP (15 a 20 min) ---
            if i < total - 1:
                wait_time = random.randint(200, 900) # 900s = 15m, 1200s = 20m
                next_time = (datetime.datetime.now() + datetime.timedelta(seconds=wait_time)).strftime("%H:%M:%S")
                log(f"ESPERA: {wait_time // 60} min. Próxima subida estimada: {next_time}")
                time.sleep(wait_time)
        else:
            log("Falló subida → queda en inbox")

    log("Main loop terminado")

# ==========================================
if __name__ == "__main__":
    main()
