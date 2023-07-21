# app.py
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Sample user data (using a list of dictionaries)
users_data = [
    {"id": 1, "name": "John Doe", "email": "john@example.com", "deleted": False},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com", "deleted": False},
]

def get_user_by_id(user_id):
    return next((user for user in users_data if user['id'] == user_id), None)

@app.route('/')
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

if __name__ == '__main__':
    app.run(debug=True)
