# working with coinbase API
import requests
response = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/sell')
print('Bitcoin sell price is %s' % response.json()['data']['amount'])

response = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/buy')
print('Bitcoin buy price is %s' % response.json()['data']['amount'])

response = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/spot')
print('Bitcoin spot price is %s' % response.json()['data']['amount'])

