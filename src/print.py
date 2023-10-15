
import json

def prints():
    try:
        with open('src/coletadds', 'r') as file:
            data = json.load(file)
            return print(data['acoes'])
    except (FileNotFoundError, KeyError):
        return 0

prints()