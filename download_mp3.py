import os
import yt_dlp
from imageio_ffmpeg import get_ffmpeg_exe

# Criar a pasta "musicas" se não existir
os.makedirs("musicas", exist_ok=True)

# Ler as URLs do arquivo
with open("musicas.txt", "r") as file:
    urls = [line.strip() for line in file if line.strip()]

# Obter o caminho do FFmpeg embutido
ffmpeg_location = get_ffmpeg_exe()
print(f"Usando FFmpeg: {ffmpeg_location}\n")

# Configurações do yt-dlp para baixar e converter para MP3
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': 'musicas/%(title)s.%(ext)s',
    'ffmpeg_location': ffmpeg_location,
    'quiet': False,
    'no_warnings': False,
    'noplaylist': True,  # Baixar apenas o vídeo, não a playlist
}

# Baixar cada música
print(f"Iniciando download de {len(urls)} músicas...\n")

for i, url in enumerate(urls, 1):
    try:
        print(f"[{i}/{len(urls)}] Baixando: {url}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"✓ Download concluído\n")
    except Exception as e:
        print(f"✗ Erro ao baixar {url}: {str(e)}\n")

print("Processo finalizado!")
