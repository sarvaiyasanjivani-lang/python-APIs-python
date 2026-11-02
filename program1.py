import requests

url = "https://jsonplaceholder.typicode.com/users/1"
response = requests.get(url, timeout=20)

print(response.json())
