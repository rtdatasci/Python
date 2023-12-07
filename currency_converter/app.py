import requests

API_KEY = 'fca_live_QOIg78VwmICn5LEFCiIK2Fa79meOLyz8AZ8AfCCr'
BASE_URL = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'

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
        print(data)
        return data
    except Exception as e:
        print(e)
        return None

convert_currency("USD")