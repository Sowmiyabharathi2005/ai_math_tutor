import requests

url = "http://127.0.0.1:5000"

print("Server running:", requests.get(url).status_code)