#!/usr/bin/env python3
"""Génère preview.html à partir de preview.template.html.

Le script :
  1. scanne videos/*.mp4
  2. génère les vignettes manquantes dans thumbs/ (ffmpeg, image à 0,8 s)
  3. lit les métadonnées, dans cet ordre de priorité :
       a. un fichier sidecar <nom>.json posé à côté de la vidéo
          (téléchargements X / YouTube / TikTok, etc.)
          — champ optionnel « thumb_at » (secondes) pour choisir la vignette
       b. l'index Instagram urls-video.json
       c. le nom de fichier seul (shortcode_owner)
  4. mesure durée / résolution / poids de chaque fichier (ffprobe)
  5. injecte le tout dans le template et écrit preview.html

Usage : python3 build-preview.py
"""

import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VIDEOS = ROOT / "videos"
THUMBS = ROOT / "thumbs"
META = ROOT / "urls-video.json"
TEMPLATE = ROOT / "preview.template.html"
OUTPUT = ROOT / "preview.html"

THUMB_WIDTH = 480
THUMB_AT = "0.8"

# hôte -> libellé du bouton « Ouvrir sur … »
SOURCES = [
    ("instagram.com", "Instagram"),
    ("x.com", "X"),
    ("twitter.com", "X"),
    ("youtube.com", "YouTube"),
    ("youtu.be", "YouTube"),
    ("tiktok.com", "TikTok"),
    ("facebook.com", "Facebook"),
]


def need(binary):
    if shutil.which(binary) is None:
        sys.exit(f"{binary} est introuvable — installe ffmpeg (brew install ffmpeg).")


def probe(path):
    """Retourne (durée, largeur, hauteur) via ffprobe."""
    raw = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0",
         "-show_entries", "stream=width,height:format=duration",
         "-of", "json", str(path)],
        capture_output=True, text=True, check=True,
    ).stdout
    data = json.loads(raw)
    stream = (data.get("streams") or [{}])[0]
    try:
        duration = float(data.get("format", {}).get("duration") or 0)
    except ValueError:
        duration = 0.0
    return duration, int(stream.get("width") or 0), int(stream.get("height") or 0)


def make_thumb(video, dest, width, height, at=THUMB_AT):
    """Vignette 9:16. Une vidéo paysage est posée entière sur un fond flouté,
    pour que la grille reste homogène sans recadrer l'image."""
    thumb_height = round(THUMB_WIDTH * 16 / 9)
    if height >= width:
        filters = f"scale={THUMB_WIDTH}:-2"
    else:
        filters = (
            f"split[a][b];"
            f"[a]scale={THUMB_WIDTH}:{thumb_height}:force_original_aspect_ratio=increase,"
            f"crop={THUMB_WIDTH}:{thumb_height},gblur=sigma=20[bg];"
            f"[b]scale={THUMB_WIDTH}:{thumb_height}:force_original_aspect_ratio=decrease[fg];"
            "[bg][fg]overlay=(W-w)/2:(H-h)/2"
        )
    subprocess.run(
        ["ffmpeg", "-v", "error", "-y", "-ss", str(at), "-i", str(video),
         "-frames:v", "1", "-vf", filters, "-q:v", "4", str(dest)],
        check=True,
    )


def source_label(url):
    """« Instagram », « X », « YouTube »… à partir du nom d'hôte de l'URL."""
    host = url.split("/")[2].lower() if url.count("/") >= 2 else ""
    for domain, label in SOURCES:
        if host == domain or host.endswith("." + domain):
            return label
    return host or "la source"


def read_sidecar(video):
    sidecar = video.with_suffix(".json")
    if not sidecar.is_file():
        return None
    try:
        return json.loads(sidecar.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print(f"  ! sidecar illisible ({video.name}) : {exc}")
        return None


def sidecar_timestamp(meta, fallback):
    """Date « 2026-09-20 » -> timestamp epoch, sinon mtime du fichier."""
    raw = str(meta.get("upload_date") or "")[:10]
    try:
        return int(datetime.strptime(raw, "%Y-%m-%d").replace(tzinfo=timezone.utc).timestamp())
    except ValueError:
        return fallback


def main():
    need("ffmpeg")
    need("ffprobe")

    if not VIDEOS.is_dir():
        sys.exit(f"Dossier introuvable : {VIDEOS}")
    if not TEMPLATE.is_file():
        sys.exit(f"Template introuvable : {TEMPLATE}")

    THUMBS.mkdir(exist_ok=True)

    # Index Instagram : nom de fichier attendu -> entrée
    by_filename = {}
    if META.is_file():
        for entry in json.loads(META.read_text(encoding="utf-8")):
            by_filename[f"{entry['shortcode']}_{entry['owner']}.mp4"] = entry

    items = []
    files = sorted(VIDEOS.glob("*.mp4"))
    if not files:
        sys.exit(f"Aucun .mp4 dans {VIDEOS}")

    for video in files:
        mtime = int(video.stat().st_mtime)
        side = read_sidecar(video)
        entry = by_filename.get(video.name)

        if side:
            owner = str(side.get("uploader_id") or side.get("uploader") or "inconnu").lstrip("@")
            shortcode = str(side.get("id") or video.stem.split("_")[0])
            caption = side.get("title") or side.get("caption") or ""
            url = side.get("url") or ""
            taken = sidecar_timestamp(side, mtime)
        elif entry:
            owner = entry["owner"]
            shortcode = entry["shortcode"]
            caption = entry.get("caption") or ""
            url = entry.get("input") or f"https://www.instagram.com/p/{shortcode}/"
            taken = int(entry.get("taken_at") or mtime)
        else:  # fichier hors index : shortcode_owner, découpe au premier « _ »
            shortcode, _, owner = video.stem.partition("_")
            caption = ""
            url = ""
            taken = mtime
            print(f"  ! {video.name} : aucune métadonnée, nom de fichier utilisé")

        duration, width, height = probe(video)

        thumb = THUMBS / f"{video.stem}.jpg"
        if not thumb.is_file() or thumb.stat().st_mtime < video.stat().st_mtime:
            make_thumb(video, thumb, width, height, (side or {}).get("thumb_at", THUMB_AT))
            print(f"  vignette  {thumb.name}")

        items.append({
            "file": f"videos/{video.name}",
            "thumb": f"thumbs/{thumb.name}",
            "shortcode": shortcode,
            "owner": owner,
            "caption": caption,
            "url": url,
            "source": source_label(url),
            "takenAt": taken,
            "duration": round(duration, 3),
            "size": video.stat().st_size,
            "w": width,
            "h": height,
        })

    payload = json.dumps(
        {"dir": str(ROOT), "items": items},
        ensure_ascii=False,
    ).replace("<", "\\u003c")

    html = TEMPLATE.read_text(encoding="utf-8")
    marker = "__DATA__"
    if marker not in html:
        sys.exit(f"Marqueur {marker} absent de {TEMPLATE.name}")
    OUTPUT.write_text(html.replace(marker, payload), encoding="utf-8")

    total = sum(i["size"] for i in items)
    print(f"\n{len(items)} vidéos · {total / 1048576:.1f} Mo → {OUTPUT.name}")


if __name__ == "__main__":
    main()
