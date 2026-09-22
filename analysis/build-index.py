#!/usr/bin/env python3
"""Construit analysis/index.json : la liste des vidéos analysées.

Appelé automatiquement à la fin de ./analyse-video, et utilisable seul :

    python3 analysis/build-index.py
"""

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main():
    videos = []
    for manifest in sorted(ROOT.glob("*/manifest.json")):
        data = json.loads(manifest.read_text(encoding="utf-8"))
        video_id = data["video_id"]
        videos.append({
            "video_id": video_id,
            "video": data["video"],
            "duration": data["duration"],
            "sheet_count": data["sheet_count"],
            "frame_count": data["frame_count"],
            "manifest": f"analysis/{video_id}/manifest.json",
            "sheets_dir": f"analysis/{video_id}/sheets/",
            "frames_dir": f"analysis/{video_id}/frames/",
        })

    index = {
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "analysis_fps": 2,
        "frames_per_sheet": 12,
        "video_count": len(videos),
        "sheet_count": sum(v["sheet_count"] for v in videos),
        "frame_count": sum(v["frame_count"] for v in videos),
        "videos": videos,
    }
    (ROOT / "index.json").write_text(
        json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"index : {index['video_count']} vidéos, "
          f"{index['sheet_count']} planches, {index['frame_count']} frames")


if __name__ == "__main__":
    main()
