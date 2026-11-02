import requests

url = "https://jsonplaceholder.typicode.com/posts/2"

response = requests.delete(url, timeout=20)
print("Status:", response.status_code)
