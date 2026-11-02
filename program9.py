import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/1",
    timeout=10
)

if response.status_code == 200:
    print("API Success:", response.json())
else:
    print("API Failed:", response.status_code)
