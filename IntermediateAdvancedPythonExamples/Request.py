# requests and APIs
import requests
res = requests.get('https://api.livecoin.net/exchange/ticker?currencyPair=BTC/USD')
print(res)
print(res.text)
print(res.json())

price = res.json()
print(price['high'])
