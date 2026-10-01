import dataclasses
import json
from enum import Enum
from typing import Any


def _to_plain(obj: Any, _seen: set[int] | None = None) -> Any:
    """Convert an arbitrary object into JSON-friendly data, dropping None values and callables."""
    if _seen is None:
        _seen = set()

    # Primitives pass straight through
    if obj is None or isinstance(obj, (str, int, float, bool)):
        return obj
    if isinstance(obj, Enum):
        return obj.value

    # Guard against circular references
    if id(obj) in _seen:
        return f"<circular {type(obj).__name__}>"
    _seen = _seen | {id(obj)}

    def clean_mapping(items):
        out = {}
        for key, value in items:
            if value is None or callable(value):
                continue
            out[str(key)] = _to_plain(value, _seen)
        return out

    if isinstance(obj, dict):
        return clean_mapping(obj.items())
    if isinstance(obj, (list, tuple, set, frozenset)):
        return [_to_plain(v, _seen) for v in obj if v is not None and not callable(v)]

    # Pydantic v2 / v1 models
    if hasattr(obj, "model_dump"):
        return clean_mapping(obj.model_dump().items())
    if hasattr(obj, "dict") and hasattr(obj, "__fields__"):
        return clean_mapping(obj.dict().items())

    # Dataclasses (shallow read so nested objects keep their own handling)
    if dataclasses.is_dataclass(obj) and not isinstance(obj, type):
        return clean_mapping((f.name, getattr(obj, f.name)) for f in dataclasses.fields(obj))

    # Plain objects with attributes
    if hasattr(obj, "__dict__"):
        return clean_mapping((k, v) for k, v in vars(obj).items() if not k.startswith("_"))

    # Anything else (datetime, Path, etc.)
    return str(obj)


def pretty_print(obj: Any, indent: int = 2) -> None:
    """Pretty print any object as JSON, hiding None values and callables."""
    print(json.dumps(_to_plain(obj), indent=indent, ensure_ascii=False, default=str))
