import json
from pathlib import Path
from typing import List, Any, Dict
from bananalyzer import Example

def load_examples_from_json(path: Path) -> List[Example]:
    """
    Load examples from a JSON file
    """
    if not path.exists():
        return []
    
    with open(path, "r") as f:
        data = json.load(f)
        
    return [
        Example(
            id=item.get("id", ""),
            url=item.get("url", ""),
            goal=item.get("goal", ""),
            expected_output=item.get("expected_output", {}),
            type=item.get("type", "detail"),
            mhtml_path=item.get("mhtml_path")
        )
        for item in data
    ]

def filter_examples(examples: List[Example], example_type: str) -> List[Example]:
    """
    Filter examples by type
    """
    return [e for e in examples if e.type == example_type]
