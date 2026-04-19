import os
import re

import yt_dlp
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
MAX_PLAYLIST_ITEMS = 100

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
))

FFMPEG_OPTIONS = {
    "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
    "options": "-vn",
}

ytdl = yt_dlp.YoutubeDL({
    "format": "bestaudio/best",
    "noplaylist": False,
    "quiet": True,
    "default_search": "ytsearch",
    "ignoreerrors": True,
    "sleep_interval": 1,
    "max_sleep_interval": 3,
    "retries": 3,
    "fragment_retries": 3,
    "extractor_retries": 3,
    "extractor_args": {"youtube": {"player_client": ["android", "web"]}},
})

YOUTUBE_RE = re.compile(r"^(https?://)?(www\.)?(youtube\.com|youtu\.be)/", re.IGNORECASE)
SPOTIFY_TRACK_RE = re.compile(r"open\.spotify\.com/(?:[\w-]+/)?track/", re.IGNORECASE)
SPOTIFY_PLAYLIST_RE = re.compile(r"open\.spotify\.com/(?:[\w-]+/)?playlist/", re.IGNORECASE)
SPOTIFY_ALBUM_RE = re.compile(r"open\.spotify\.com/(?:[\w-]+/)?album/", re.IGNORECASE)
