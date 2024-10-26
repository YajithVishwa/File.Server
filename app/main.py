# app/main.py

# Import any additional modules as needed
from flask import jsonify

# Define additional routes, functions, or utility methods here

def health_check():
    """A simple health check endpoint."""
    return jsonify({"status": "OK"})
