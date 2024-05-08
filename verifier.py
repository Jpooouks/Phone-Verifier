import requests
import json

def verify_number(number):

    api_key = "api-key-here"

    url = f"https://api.apilayer.com/number_verification/validate?number={number}"
    headers = {'apikey': api_key}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        response_data = response.json()

        return response_data
    else:
        print(f"Error: {response.status_code} - {response.text}")

