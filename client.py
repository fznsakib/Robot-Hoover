import requests

payload = {
    'roomSize': [5, 5],
    'coords': [1, 2],
    'patches': [
        [1, 0],
        [2, 2],
        [2, 3]
    ],
    'instructions': 'NNESEESWNWW'
}

r = requests.post('http://127.0.0.1:5000/navigate', json=payload)
print(r.json())