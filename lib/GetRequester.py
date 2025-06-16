import requests  # Import the requests library

class GetRequester:
    def __init__(self, url):
        self.url = url  # Store the URL passed at initialization

    def get_response_body(self):
        # Send a GET request and return the raw response body
        response = requests.get(self.url)
        return response.content  # Returns bytes

    def load_json(self):
        # Send a GET request and return the JSON-decoded response
        response = requests.get(self.url)
        return response.json()  # Automatically parses JSON to dict or list
