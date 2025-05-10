"""
auth.py

This module defines authentication-related routes (login, logout, signup)
using a Flask Blueprint named 'auth'.
Currently, it returns simple HTML placeholders for each route.
"""

from flask import Blueprint

# Create a Blueprint for authentication routes
auth = Blueprint('auth', __name__)

# Route for the login page (GET /login)
@auth.route('/login')
def login():
    return "<h1>Login</h1><p>This is the login page!</p>", 200

# Route for the logout page (GET /logout)
@auth.route('/logout')
def logout():
    return "<h1>Logout</h1><p>This is the logout page!</p>", 200

# Route for the signup page (GET /sign-up)
@auth.route('/sign-up')
def sign_up():
    return "<h1>Sign Up</h1><p>This is the signup page!</p>", 200
