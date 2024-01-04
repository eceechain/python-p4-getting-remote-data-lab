import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.text

    def load_json(self):
        response_body = self.get_response_body()
        return json.loads(response_body)

# Example usage:
url = " https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
requester = GetRequester(url)

# Get the response body
response_body = requester.get_response_body()
print("Response Body:")
print(response_body)

# Load JSON data
json_data = requester.load_json()
print("\nJSON Data:")
print(json_data)
