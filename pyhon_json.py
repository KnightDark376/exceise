import json

a = {
    'name': 'max',
    'age': 22,
    'mark': [90, 50, 80,40],
    'pass': True,
    'object': {
        'color': ('red','blue')
    }
}

print(json.dumps(a, indent=2))