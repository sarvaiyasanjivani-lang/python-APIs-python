import requests

with requests.Session() as session:
    session.headers.update({"Accept": "application/json"})

    response = session.get(
        "https://jsonplaceholder.typicode.com/users/1",
        timeout=10
    )

    print(response.json())
