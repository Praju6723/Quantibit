import json

def load_json_file(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON in {filename}.")
        return None

def print_keys_and_values(data):
    if isinstance(data, dict):
        for key, value in data.items():
            print(f" {key} : {value}")
    elif isinstance(data, list):
        for index, item in enumerate(data):
            print(f"Item {index}:")
            print_keys_and_values(item)
    else:
        print("Unsupported JSON format.")

if __name__ == "__main__":
    filename = "Task11.json"
    json_data = load_json_file(filename)
    
    if json_data:
        print_keys_and_values(json_data)
