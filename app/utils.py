import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict


def now_iso() -> str:
    return datetime.utcnow().isoformat() + "Z"


def safe_json_loads(text: str) -> Dict[str, Any]:
    """
    Tries best-effort to parse JSON.
    Handles cases where model returns JSON inside ```json blocks.
    """
    text = text.strip()

    # remove markdown code block wrappers if present
    if text.startswith("```"):
        text = text.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(text)
    except Exception:
        return {"raw": text}


def write_json(path: str, data: Any) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def read_text(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")
