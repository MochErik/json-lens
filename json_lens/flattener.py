"""JSON flattener and diff calculation engine."""

import json
from typing import Dict, Any, List


def flatten_json(data: Any, prefix: str = "", separator: str = ".") -> Dict[str, Any]:
    """Flatten deeply nested JSON dictionaries and lists into dot-notation keys."""
    items = {}
    if isinstance(data, dict):
        for k, v in data.items():
            new_key = f"{prefix}{separator}{k}" if prefix else str(k)
            items.update(flatten_json(v, new_key, separator=separator))
    elif isinstance(data, list):
        for i, v in enumerate(data):
            new_key = f"{prefix}[{i}]"
            items.update(flatten_json(v, new_key, separator=separator))
    else:
        items[prefix] = data
    return items


def compute_json_diff(obj1: Dict[str, Any], obj2: Dict[str, Any]) -> Dict[str, Any]:
    """Compute structural and value differences between two JSON objects."""
    flat1 = flatten_json(obj1)
    flat2 = flatten_json(obj2)

    all_keys = set(flat1.keys()).union(set(flat2.keys()))
    
    added = {}
    removed = {}
    modified = {}

    for k in sorted(list(all_keys)):
        if k in flat1 and k not in flat2:
            removed[k] = flat1[k]
        elif k in flat2 and k not in flat1:
            added[k] = flat2[k]
        elif flat1[k] != flat2[k]:
            modified[k] = {"from": flat1[k], "to": flat2[k]}

    return {
        "added": added,
        "removed": removed,
        "modified": modified,
        "has_changes": bool(added or removed or modified)
    }
