import requests
import os

token = os.getenv("API_TOKEN")

if not token:
    raise ValueError("Set API_TOKEN environment variable")

headers = {"Authorization": f"Bearer {token}"}

response = requests.get(
    "https://api.example.com/profile",
    headers=headers,
    timeout=10
)

response.raise_for_status()
print(response.json())
