import requests
import config # to read api key using config

# API_KEY = 'fca_live_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' # directly provide the key
# BASE_URL = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'

# or, read key from a config.py file containing API_KEY = 'fca_live_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
api_key=config.API_KEY
BASE_URL = f'https://api.freecurrencyapi.com/v1/latest?apikey={api_key}'

# currencies of interest
CURRENCIES = ["USD","EUR", "CNY","CAD", "AUD"]


def convert_currency(base):
    # to pass currencies as string
    currencies = ",".join(CURRENCIES)
    # query parameters
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    # better error handling
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except :
        print("Invalid currency entered")
        return None


# user input in a while loop:
while True:
    base = input("Enter the base currency (q for quit): ").upper()
    if base == "Q":
        break

    data = convert_currency(base)
    if not data: 
        continue
    
    del data[base]  # to remove the user input base currency that will show up as "1"

    for ticker, value in data.items():
        print(f"{ticker}: {value}")