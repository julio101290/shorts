# 🎬 Auto Uploader de YouTube Shorts con IA (Ollama)

Script en **Python** que automatiza completamente la subida de **YouTube
Shorts**.

El sistema:

1.  Detecta videos nuevos en una carpeta.
2.  Usa **IA local con Ollama** para generar:
    -   Título
    -   Descripción
    -   Hashtags
3.  Sube automáticamente el video a **YouTube**.
4.  Mueve el archivo a la carpeta de **subidos**.
5.  Espera un tiempo aleatorio antes de subir el siguiente video.

Todo funciona **de forma local sin depender de APIs externas de IA**.

------------------------------------------------------------------------

# 🚀 Características

✔ Generación automática de metadata con **IA local**\
✔ Subida automática a **YouTube Shorts**\
✔ Espera aleatoria entre subidas\
✔ Manejo automático de tokens de YouTube\
✔ Sistema simple basado en carpetas\
✔ No requiere servicios en la nube para la IA\
✔ Funciona en **Linux, Mac y Windows (WSL)**

------------------------------------------------------------------------

# 📂 Estructura de Carpetas

El script utiliza la siguiente estructura:

    ~/shorts/

    global/
       inbox/
          video1.mp4
          video2.mp4

       uploaded/
          video1.mp4
          video2.mp4

### 📥 inbox

Aquí se colocan los videos que se quieren subir.

### 📤 uploaded

Los videos que ya fueron subidos se moverán automáticamente aquí.

------------------------------------------------------------------------

# ⚙️ Requisitos

## Python

Python **3.9 o superior**

Instalar dependencias:

``` bash
pip install google-api-python-client google-auth-oauthlib google-auth-httplib2
```

------------------------------------------------------------------------

## Ollama (IA local)

Instalar Ollama:

https://ollama.com

Descargar el modelo usado por el script:

``` bash
ollama pull qwen2.5:14b
```

Modelo usado:

    qwen2.5:14b

Este modelo genera:

-   títulos optimizados
-   descripciones
-   hashtags

sin necesidad de internet.

------------------------------------------------------------------------

## Credenciales de YouTube

Debes crear credenciales OAuth en Google Cloud.

1️⃣ Ir a:

https://console.cloud.google.com/

2️⃣ Crear un proyecto

3️⃣ Activar la API:

    YouTube Data API v3

4️⃣ Crear credenciales:

    OAuth Client ID

Tipo:

    Desktop Application

5️⃣ Descargar el archivo:

    client_secrets.json

Colócalo en la misma carpeta que el script.

------------------------------------------------------------------------

# 📦 Instalación

### 1️⃣ Guardar el script

    uploader.py

------------------------------------------------------------------------

### 2️⃣ Crear carpetas

``` bash
mkdir -p ~/shorts/global/inbox
mkdir -p ~/shorts/global/uploaded
```

------------------------------------------------------------------------

### 3️⃣ Instalar dependencias

``` bash
pip install google-api-python-client google-auth-oauthlib
```

------------------------------------------------------------------------

### 4️⃣ Instalar modelo de IA

``` bash
ollama pull qwen2.5:14b
```

------------------------------------------------------------------------

# ▶️ Uso

### 1️⃣ Colocar videos en:

    ~/shorts/global/inbox

Ejemplo:

    drum_fill_01.mp4
    drum_solo_fast.mp4

------------------------------------------------------------------------

### 2️⃣ Ejecutar el script

``` bash
python3 uploader.py
```

------------------------------------------------------------------------

### 3️⃣ Primer inicio

Se abrirá una ventana de login de Google.

Después de iniciar sesión se generará:

    token.json

Ese archivo permitirá subir videos **sin volver a iniciar sesión**.

------------------------------------------------------------------------

# 🧠 Cómo funciona

Flujo del script:

    Video nuevo
          │
          ▼
    IA genera metadata
          │
          ▼
    Subida a YouTube
          │
          ▼
    Mover a carpeta uploaded
          │
          ▼
    Esperar tiempo aleatorio

------------------------------------------------------------------------

# ⏱ Sistema Anti-Spam

El script espera un tiempo aleatorio entre videos:

    200 a 900 segundos

Esto equivale aproximadamente a:

    3 a 15 minutos

Esto ayuda a evitar comportamientos detectables como automatización
masiva.

------------------------------------------------------------------------

# 🧠 Generación de Metadata con IA

El script usa **Ollama local** para generar contenido optimizado para
Shorts.

Ejemplo de salida:

``` json
{
  "title": "Fill de batería rápido 🔥",
  "description": "Un fill explosivo en batería.\n¿Puedes tocarlo?",
  "hashtags": ["#bateria", "#drums", "#drummer", "#shorts", "#musica"]
}
```

------------------------------------------------------------------------

# 🎯 Por qué usar este sistema

## 1️⃣ Automatización total

Puedes subir **decenas o cientos de Shorts automáticamente**.

------------------------------------------------------------------------

## 2️⃣ IA local

No dependes de:

-   OpenAI
-   APIs pagadas
-   límites de uso

Todo corre en tu computadora.

------------------------------------------------------------------------

## 3️⃣ Ideal para contenido masivo

Perfecto para:

-   músicos
-   creadores de contenido
-   clips de gaming
-   podcasts
-   contenido educativo

------------------------------------------------------------------------

## 4️⃣ Ahorra tiempo

Subir manualmente muchos videos puede tomar horas.

Este sistema puede hacerlo automáticamente.

------------------------------------------------------------------------

## 5️⃣ Escalable

Puedes expandirlo para:

-   TikTok
-   Instagram Reels
-   Facebook Reels
-   múltiples cuentas

------------------------------------------------------------------------

# 🔧 Configuración del Script

Variables principales:

``` python
BASE_DIR = "~/shorts"

OLLAMA_MODEL = "qwen2.5:14b"

VIDEO_EXTS = (".mp4", ".mov", ".mkv")
```

------------------------------------------------------------------------

# 📊 Logs del Sistema

El script imprime logs como:

    [2026-03-10 12:22:01] Procesando: drum_fill.mp4
    [2026-03-10 12:22:04] Metadata generada
    [2026-03-10 12:22:12] YouTube OK → videoId=abc123
    [2026-03-10 12:22:12] Video movido a uploaded
    [2026-03-10 12:22:12] Esperando 10 minutos...

------------------------------------------------------------------------

# ⚠️ Posibles Errores

### Ollama no instalado

    Ollama error

Solución:

    ollama install

------------------------------------------------------------------------

### client_secrets.json no encontrado

    YouTube error: client_secrets.json no encontrado

Debes descargar las credenciales de Google Cloud.

------------------------------------------------------------------------

# 🔒 Seguridad

El sistema guarda un archivo:

    token.json

Este archivo contiene el acceso a tu cuenta de YouTube.

**No lo compartas.**

------------------------------------------------------------------------

# 🧩 Posibles mejoras

Puedes expandir el sistema para:

-   subir a **TikTok automáticamente**
-   generar **miniaturas**
-   generar **títulos A/B**
-   programar horarios de publicación
-   subir a **múltiples canales**
