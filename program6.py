import requests

headers = {"Accept": "application/json"}

response = requests.get(
    "https://jsonplaceholder.typicode.com/users",
    headers=headers,
    timeout=10
)
