#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status."""
import requests

if __name__ == "__main__":
    # Fetch the URL
    response = requests.get("https://alx-intranet.hbtn.io/status") 
    # Print the body of the response
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
