import requests

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users",
        timeout=10
    )
    response.raise_for_status()
    print(response.json())

except requests.RequestException as error:
    print("API Error:", error)
