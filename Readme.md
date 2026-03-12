# Auto Uploader de Shorts a YouTube

Este script automatiza la subida de videos cortos (Shorts) a YouTube. Utiliza Ollama local (modelo qwen2.5:14b) para generar títulos, descripciones y hashtags de forma automática, y luego sube el video a YouTube mediante la API oficial.

Ideal para creadores de contenido que manejan muchos videos y quieren agilizar el proceso de publicación.

---------------------------------------------------------------------

CARACTERISTICAS:

- Detección automática de videos en una carpeta inbox.
- Generación de metadatos (título, descripción, hashtags) usando Ollama.
- Subida a YouTube con autenticación OAuth (token persistente).
- Espera aleatoria entre 3 y 15 minutos entre subidas.
- Manejo de errores y archivos no válidos.
- Organización automática: videos subidos se mueven a carpeta uploaded.

---------------------------------------------------------------------

REQUISITOS:

1. Software necesario:
   - Python 3.8 o superior
   - Ollama instalado (ollama.ai)
   - Modelo qwen2.5:14b descargado en Ollama
   - Conexión a internet

2. Dependencias de Python:
   pip install google-api-python-client google-auth-oauthlib

3. Credenciales de Google (YouTube API):
   - Ir a Google Cloud Console
   - Crear proyecto y habilitar YouTube Data API v3
   - Configurar pantalla de consentimiento
   - Crear credencial OAuth 2.0 para aplicación de escritorio
   - Descargar JSON y renombrar a client_secrets.json

---------------------------------------------------------------------

ESTRUCTURA DE DIRECTORIOS:

~/shorts/
├── global/
│   ├── inbox/       # Coloca aquí los videos a subir
│   └── uploaded/    # Videos subidos se mueven aquí

Nota: En Windows usar C:\shorts\global\inbox

---------------------------------------------------------------------

MODO DE USO:

1. Colocar videos en inbox/
2. Ejecutar: python auto_uploader.py
3. Autorizar YouTube (solo primera vez)
4. El proceso automático comienza:
   - Genera metadata con Ollama
   - Sube a YouTube (público, categoría Música)
   - Mueve video a uploaded/
   - Espera 3-15 minutos antes del siguiente

---------------------------------------------------------------------

PERSONALIZACION:

- Cambiar modelo Ollama: editar OLLAMA_MODEL
- Tiempos de espera: modificar random.randint() en el código
- Categoría YouTube: cambiar categoryId (actualmente 10=Música)
- Prompt de metadata: editar generate_metadata()

---------------------------------------------------------------------

SOLUCION DE PROBLEMAS:

Error client_secrets.json no encontrado:
  - Colocar el archivo en la misma carpeta del script

Error Ollama o JSON inválido:
  - Verificar que ollama serve esté corriendo
  - Confirmar modelo descargado: ollama pull qwen2.5:14b

Error subida YouTube:
  - Borrar token.json y re-autorizar
  - Verificar cuota de API
  - Video debe ser ≤ 60 segundos (Shorts)

Videos no detectados:
  - Extensiones soportadas: .mp4, .mov, .mkv

---------------------------------------------------------------------

NOTAS ADICIONALES:

- No se borran videos, solo se mueven a uploaded/
- Si falla subida, video queda en inbox para reintentar
- token.json guarda credenciales de YouTube

---------------------------------------------------------------------

CONTRIBUCIONES Y LICENCIA:

Contribuciones bienvenidas via issues o pull requests.
Licencia MIT.

---------------------------------------------------------------------

¡Ahora puedes automatizar la publicación de tus Shorts!
END_README_COPY_HERE
