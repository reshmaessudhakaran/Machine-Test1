import requests

url = "http://127.0.0.1:5000/users"

# Invalid email
data = {
    "name": "Check User",
    "email": "invalidemail@examplecom"
}

response = requests.post(url, json=data)
print(response.json())  # return {"error": "Invalid email format"}
