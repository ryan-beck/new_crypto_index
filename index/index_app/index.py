import json
import urllib2
from pprint import pprint
from datetime import datetime

def get_index():
    endpoint = 'https://api.coinmarketcap.com/v1/ticker/?limit=20'

    data = urllib2.urlopen(endpoint)
    content = data.read()
    parsed = json.loads(content)
    total = 0
    for coin in parsed:
        total += float(coin['market_cap_usd'])

    return (total/(10**9))
