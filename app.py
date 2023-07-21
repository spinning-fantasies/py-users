# app.py
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Sample user data (using a list of dictionaries)
users_data = [
    {"id": 1, "name": "John Doe", "email": "john@example.com", "deleted": False},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com", "deleted": False},
]

def get_user_by_id(user_id):
    return next((user for user in users_data if user['id'] == user_id), None)

@app.route('/users')
def users():
    # Only show non-deleted users
    active_users = [user for user in users_data if not user['deleted']]
    return render_template('users.html', users=active_users)

@app.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])
def edit_user(user_id):
    user = get_user_by_id(user_id)
    if not user:
        return "User not found", 404

    if request.method == 'POST':
        # Handle the form submission to update the user data
        name = request.form['name']
        email = request.form['email']

        user['name'] = name
        user['email'] = email

        return redirect(url_for('users'))

    # Render the edit form
    return render_template('edit_user.html', user=user)

@app.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    user = get_user_by_id(user_id)
    if not user:
        return "User not found", 404

    user['deleted'] = True

    return redirect(url_for('users'))

@app.route('/users/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        # Handle the form submission to add the new user
        name = request.form['name']
        email = request.form['email']

        # Generate a new user ID (Assuming no duplicate user IDs)
        new_user_id = max(user['id'] for user in users_data) + 1
        new_user = {"id": new_user_id, "name": name, "email": email, "deleted": False}
        users_data.append(new_user)

        return redirect(url_for('users'))

    # Render the add user form
    return render_template('add_user.html')

if __name__ == '__main__':
    app.run(debug=True)
