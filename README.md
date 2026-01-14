# YouTube to MP3 Downloader

Script Python para baixar vídeos do YouTube e converter automaticamente para MP3.

## 📋 Funcionalidades

- Baixa múltiplas músicas/vídeos do YouTube de uma vez
- Converte automaticamente para MP3
- Lê URLs de um arquivo de texto
- Salva as músicas em uma pasta dedicada

## 🚀 Como usar

### 1. Clone o repositório:
```bash
git clone https://github.com/otaciobarbosa/mp3_youtube.git
cd mp3_youtube
```

### 2. Instale as dependências:
```bash
pip install yt-dlp imageio-ffmpeg
```

### 3. Adicione suas URLs:
Edite o arquivo `musicas.txt` e adicione as URLs dos vídeos do YouTube (uma por linha).

### 4. Execute o script:
```bash
python download_mp3.py
```

Os arquivos MP3 serão salvos na pasta `musicas`.

## 📦 Dependências

- `yt-dlp` - Para baixar vídeos do YouTube
- `imageio-ffmpeg` - FFmpeg embutido para conversão de áudio

## 📁 Estrutura do projeto

```
mp3_youtube/
├── download_mp3.py    # Script principal
├── musicas.txt        # Lista de URLs para download
├── musicas/           # Pasta onde os MP3 são salvos
└── README.md          # Este arquivo
```

## ⚙️ Configuração

O script está configurado para:
- Baixar apenas vídeos individuais (não playlists)
- Converter para MP3 com qualidade de 192kbps
- Usar FFmpeg embutido (via imageio-ffmpeg)

## 📝 Notas

- A pasta `musicas/` e os arquivos MP3 são ignorados pelo Git
- Certifique-se de ter conexão estável com a internet
- Respeite os direitos autorais ao baixar conteúdo
