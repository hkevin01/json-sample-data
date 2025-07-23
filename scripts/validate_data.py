import json
import os


def validate_json(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            json.load(f)
        print(f"{filename} is valid JSON.")
    except json.JSONDecodeError as e:
        print(f"Error in {filename}: {e}")


def main():
    data_dir = os.path.join(os.path.dirname(__file__), '../data')
    for fname in os.listdir(data_dir):
        if fname.endswith('.json'):
            validate_json(os.path.join(data_dir, fname))


if __name__ == "__main__":
    main()
