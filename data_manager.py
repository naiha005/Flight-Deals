from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/800df3612144c9df868e5517c77a4946/flightDeals/prices"
SHEETY_USER_ENDPOINT = "https://api.sheety.co/670bd5b7865748332674b8e31ee750e1/flightDeals/users"
SHEETY_APIKEY = "YOUR APIKEY"


class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.customer_data = ''

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        # print(data)
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            # print(response.text)

    def get_customer_emails(self):
        # header = {"apikey": f"Authorization: Bearer {SHEETY_APIKEY}"}
        response = requests.get(url=SHEETY_USER_ENDPOINT)
        data = response.json()
        print(data)
        self.customer_data = data['users']
        return self.customer_data
