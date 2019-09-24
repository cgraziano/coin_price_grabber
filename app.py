from pricegetter.coin_market_cap import CoinMarketCap
from coin_market_cap_coins.cmc_coins import CMCCoins
import time
import sys
from requests import Session

def getApiKeyFromFile():
    file = open('key.txt', 'r')
    key = file.read()
    return key

def getApiKeyFromArguments():
    arguments = sys.argv
    print arguments
    file = open('key.txt', 'r')
    key = file.read()
    return key

def getPrices():
    timeToSleep = 0
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': getApiKeyFromArguments()
    }
    session = Session()
    session.headers.update(headers)
    file = open('results.txt', 'w')

    pricegetter = CoinMarketCap(session)
    for coin in CMCCoins:
        price = pricegetter.getPrice(coin.value)
        output = coin.name + ' ' + str(price)
        print(output)
        file.write(output)
        time.sleep(timeToSleep)
    file.close()


getApiKeyFromArguments()
getPrices()
