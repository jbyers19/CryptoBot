# Imports
import requests


# Gets the current price bitgrail
def get_price():
    r = requests.get('https://bitgrail.com/api/v1/markets')
    if r.status_code == 200:
        price = r.json()['response']['BTC'][0]['last']
        return float(price)
    else:
        print("Request Failed.")
        return None
