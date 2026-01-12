import json
from pathlib import Path
from typing import Dict, Any

class MemoryStore:
    def __init__(self, path: str = "runs/memory.json"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            self._write({})

    def _read(self) -> Dict[str, Any]:
        return json.loads(self.path.read_text(encoding="utf-8"))

    def _write(self, data: Dict[str, Any]) -> None:
        self.path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    def set(self, key: str, value: Any) -> None:
        data = self._read()
        data[key] = value
        self._write(data)

    def get(self, key: str, default=None):
        data = self._read()
        return data.get(key, default)

    def all(self) -> Dict[str, Any]:
        return self._read()
