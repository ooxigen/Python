import requests
import time

while True:
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=LTC&convert=BRL"
    headers = {
        "Accepts": "application/json",
        "X-CMC_Pro_API_Key": "462b13fe-538b-4ca9-8730-8102a99dd1cc" # coinmarket key
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    bitcoin_price = data["data"]["LTC"]["quote"]["BRL"]["price"]
    price_formatted = "R$ {:,.2f}".format(bitcoin_price)
    print("O preço atual do LITECOIN é:", price_formatted)
    time.sleep(1500)