#cli inventory management system run with rest api
import requests

BASE_URL = "http://127.0.0.1:5555"
#help function to print a separator line
def print_separator():
    print("\n" + "=" * 60)


def handle_connection_error():
    print("\nError: Could not connect to the Flask API.")
    print("Make sure app.py is running on http://127.0.0.1:5555\n")

