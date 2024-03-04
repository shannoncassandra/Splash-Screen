import json

def load_json_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        
    # If the data contains a 'bytes' field with hex strings, convert them to integers
    if 'bytes' in data and all(isinstance(b, str) for b in data['bytes']):
        data['bytes'] = [int(b, 16) for b in data['bytes']]
        
    return data
