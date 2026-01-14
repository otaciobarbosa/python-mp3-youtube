# Instalação e uso

## 1. Instalar dependências necessárias:
```bash
pip install yt-dlp
```

## 2. Instalar FFmpeg (necessário para converter para MP3):

### Windows:
- Baixe o FFmpeg de: https://www.gyan.dev/ffmpeg/builds/
- Extraia e adicione o executável ao PATH do sistema
- Ou use: `choco install ffmpeg` (se tiver Chocolatey)
- Ou use: `winget install ffmpeg` (Windows 11)

### Alternativa simples:
```bash
pip install ffmpeg-python
```

## 3. Executar o script:
```bash
python download_mp3.py
```

Os arquivos MP3 serão salvos na pasta `musicas`.
