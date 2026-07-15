"""
run.py

Entry point for the Inventory Management System.
Starts the Flask development server.
"""

from app import app

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5555,
        debug=True
    )