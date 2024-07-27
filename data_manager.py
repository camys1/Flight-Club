import os
from pprint import pprint
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv # type: ignore


load_dotenv()

class DataManager:
    def __init__(self):

        self.prices_endpoint = os.getenv("SHEETY_PRICES_ENDPOINT")
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        
        response = requests.get(url=self.prices_endpoint)
        data = response.json()
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
                url=f"{self.prices_endpoint}/{city['id']}",
                json=new_data
            )
            print(response.text)

