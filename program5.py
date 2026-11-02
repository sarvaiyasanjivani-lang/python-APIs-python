import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(
    url,
    params={"userId": 1},
    timeout=10
)
