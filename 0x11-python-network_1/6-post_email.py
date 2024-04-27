#!/usr/bin/python3
"""Sends a POST request with an email parameter to a specified URL."""
import requests
import sys

if __name__ == "__main__":
    # Extract URL and email from command line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Data to be sent with POST request
    data = {'email': email}

    # Send POST request
    response = requests.post(url, data=data)

    # Display the body of the response
    print(response.text)
