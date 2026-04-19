from config import sp, SPOTIFY_TRACK_RE, SPOTIFY_PLAYLIST_RE, SPOTIFY_ALBUM_RE, MAX_PLAYLIST_ITEMS


def _spotify_id(url: str) -> str:
    return url.split("/")[-1].split("?")[0]


def _track_to_query(track: dict) -> tuple[str, str]:
    name = (track.get("name") or "").strip()
    artists = [a["name"].strip() for a in (track.get("artists") or []) if a.get("name")]
    query = f"{name} {artists[0]}".strip() if artists else name
    display = f"{name} - {', '.join(artists)}" if name and artists else name
    return query or "unknown", display or "unknown"


def is_spotify_track_url(url: str) -> bool:
    return bool(SPOTIFY_TRACK_RE.search(url))


def is_spotify_playlist_url(url: str) -> bool:
    return bool(SPOTIFY_PLAYLIST_RE.search(url))


def is_spotify_album_url(url: str) -> bool:
    return bool(SPOTIFY_ALBUM_RE.search(url))


def get_spotify_track_query(url: str) -> tuple[str, str] | None:
    try:
        return _track_to_query(sp.track(_spotify_id(url)))
    except Exception:
        return None


def get_spotify_playlist_queries(url: str, limit: int = MAX_PLAYLIST_ITEMS) -> list[tuple[str, str]]:
    try:
        out, offset = [], 0
        while len(out) < limit:
            resp = sp.playlist_items(
                _spotify_id(url),
                limit=min(100, limit - len(out)),
                offset=offset,
                additional_types=("track",),
            )
            items = resp.get("items") or []
            if not items:
                break
            for it in items:
                track = (it or {}).get("track")
                if track and not track.get("is_local"):
                    q, d = _track_to_query(track)
                    if q != "unknown":
                        out.append((q, d))
                if len(out) >= limit:
                    break
            offset += len(items)
            if not resp.get("next"):
                break
        return out
    except Exception:
        return []


def get_spotify_album_queries(url: str, limit: int = MAX_PLAYLIST_ITEMS) -> list[tuple[str, str]]:
    try:
        out, offset = [], 0
        while len(out) < limit:
            resp = sp.album_tracks(_spotify_id(url), limit=min(50, limit - len(out)), offset=offset)
            items = resp.get("items") or []
            if not items:
                break
            for track in items:
                if track:
                    q, d = _track_to_query(track)
                    if q != "unknown":
                        out.append((q, d))
                if len(out) >= limit:
                    break
            offset += len(items)
            if not resp.get("next"):
                break
        return out
    except Exception:
        return []
