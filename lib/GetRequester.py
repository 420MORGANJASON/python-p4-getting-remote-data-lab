import requests
import json


class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_requester(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an exception if the request was unsuccessful
            return response.content
        except requests.exceptions.RequestException as e:
            print("Error occurred during the request:", e)
            return None

    def load_json(self, json_string):
        try:
            return json.loads(json_string)
        except json.JSONDecodeError as e:
            print("Error occurred while parsing JSON:", e)
            return None

    def get_response(self):
        response_content = self.get_requester()
        if response_content is not None:
            responses = self.load_json(response_content)
            if responses is not None:
                views_list = []
                for response in responses:
                    if "agency" in response:
                        views_list.append(response["agency"])
                return views_list

        return []


# Instantiate the GetRequester class
URL = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
requester = GetRequester(URL)

# Call the get_response method
got_responses = requester.get_response()

# Print the unique agency names
for response in set(got_responses):
    print(response)
