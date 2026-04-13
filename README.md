# Discord Bot

Um bot para Discord com funcionalidades de música e chat com IA.

## Funcionalidades

### Música
- Toca músicas do YouTube por link ou nome/artista
- Aceita links do Spotify (track, playlist, álbum) e converte para busca no YouTube
- Comandos de fila, pausa, pular, etc.

### IA (Groq)
- Conversa com IA usando o modelo `llama-3.3-70b-versatile` via Groq
- Respostas curtas e diretas

## Pré-requisitos
- Python 3.9+
- Token do bot Discord
- Credenciais do Spotify Developer (Client ID e Secret)
- API Key do Groq

## Instalação
1. Clone o repositório
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Crie um arquivo `.env` com:
   ```env
   DISCORD_TOKEN=seu_token_aqui
   SPOTIPY_CLIENT_ID=seu_client_id_aqui
   SPOTIPY_CLIENT_SECRET=seu_client_secret_aqui
   GROQ_API_KEY=sua_api_key_aqui
   ```
4. Execute o bot:
   ```bash
   python main.py
   ```

## Comandos

### Música
- `.play <url ou texto>` — Toca música do YouTube ou busca por nome/artista
- `.play <link do Spotify>` — Busca a faixa/playlist/álbum no YouTube e toca
- `.queue` — Mostra a fila
- `.skip` — Pula para a próxima
- `.clear` — Limpa a fila
- `.pause` — Pausa a música
- `.resume` — Continua a música
- `.stop` — Para a música
- `.leave` — Sai do canal de voz

### Geral
- `.salve` — Cumprimento do bot
- `.chat <pergunta>` — Conversa com a IA

## Estrutura do Projeto
```
discord-bot/
├── main.py              # Entrada: cria o bot e carrega os cogs
├── config.py            # Configurações (ytdl, spotify, constantes)
├── utils/
│   ├── spotify.py       # Helpers do Spotify (track, playlist, álbum)
│   └── youtube.py       # YTDLSource e helpers do YouTube
├── cogs/
│   ├── music.py         # Comandos de música
│   └── ai.py            # Comandos de IA
├── requirements.txt
└── .env
```

## Observações
- O bot **não toca áudio diretamente do Spotify** (por restrições da API), apenas busca no YouTube
- Para melhor funcionamento, mantenha o `yt-dlp` sempre atualizado
- O bot funciona em múltiplos servidores simultaneamente

## Licença
MIT
