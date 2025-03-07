from flask import Flask, request, jsonify
import re

app = Flask(__name__)
from flask import Flask, request, jsonify

# list of users with id, name, and email
users = [
    {"id": 1, "name": "ABC", "email": "abc@example.com"},
    {"id": 2, "name": "XYZ", "email": "xyz@example.com"},
    {"id": 3, "name": "Reshma E S", "email": "reshma@example.com"}
]

# Home Route
@app.route('/')
def home():
    return "Flask API is running....! "

# function to validate email format
def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email)

# Endpoint to get the list of users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Endpoint to add a new user with validation for unique email
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    # Validate if name and email given
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Missing name or email"}), 400

    # Validate email format
    if not is_valid_email(data['email']):
        return jsonify({"error": "Invalid email format"}), 400

    # Check if email already exists in the users list
    if any(user['email'] == data['email'] for user in users):
        return jsonify({"error": "Email already exists"}), 400

    # Create a new user
    new_user = {
        "id": users[-1]['id'] + 1 if users else 1,
        "name": data['name'],
        "email": data['email']
    }
    users.append(new_user)
    return jsonify(new_user), 201

# Run the Flask app in debug mode
if __name__ == '__main__':
    app.run(debug=True)
