import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {"title": "Python", "body": "Advanced API", "userId": 2}

response = requests.post(url, json=data, timeout=20)
print(response.status_code, response.json())
