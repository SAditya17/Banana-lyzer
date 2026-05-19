import argparse
import sys
from typing import List

def main(args: List[str] = sys.argv[1:]) -> None:
    parser = argparse.ArgumentParser(description="Banana-lyzer: AI Agent evaluation framework")
    parser.add_argument("path", help="Path to the agent runner file (e.g., agent_runner.py)")
    parser.add_argument("--examples", help="Path to the examples.json file", default="static/examples.json")
    parser.add_argument("--type", help="Filter by example type (listing, detail, listing_detail)")
    
    parsed_args = parser.parse_args(args)
    
    print(f"🍌 Banana-lyzer starting...")
    print(f"🧐 Loading agent from: {parsed_args.path}")
    
    from pathlib import Path
    from bananalyzer.loader import load_examples_from_json, filter_examples
    
    examples_path = Path(parsed_args.examples)
    examples = load_examples_from_json(examples_path)
    
    if parsed_args.type:
        examples = filter_examples(examples, parsed_args.type)
        print(f"🎯 Filtering by type: {parsed_args.type}")

    print(f"📚 Loaded {len(examples)} examples")

    # TODO: Implement pytest dynamic test generation and execution
    print("🚀 Running evaluations...")
    print("✅ Done!")

if __name__ == "__main__":
    main()
