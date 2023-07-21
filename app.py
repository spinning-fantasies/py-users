# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Users Management Back Office Application!"

@app.route('/users')
def users():
    # Replace this with actual user data from the database
    users_data = [
        {"id": 1, "name": "John Doe", "email": "john@example.com"},
        {"id": 2, "name": "Jane Smith", "email": "jane@example.com"},
    ]
    return render_template('users.html', users=users_data)

if __name__ == '__main__':
    app.run(debug=True)
