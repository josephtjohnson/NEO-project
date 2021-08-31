import json

def load_nobel_prizes(filename='cad.json'):
    with open(filename) as file:
        return json.load(file)
    
def json_data():
    data = load_noble_prizes()
    print(data)