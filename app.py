from pricegetter.coin_market_cap import CoinMarketCap
from coin_market_cap_coins.cmc_coins import CMCCoins
import time
from requests import Session

def getKey():
    file = open('key.txt', 'r')
    key = file.read()
    return key

def getPrices():
    timeToSleep = 0
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': getKey()
    }
    session = Session()
    session.headers.update(headers)
    file = open('results.txt', 'w')

    pricegetter = CoinMarketCap(session)
    for coin in CMCCoins:
        price = pricegetter.getPrice(coin.value)
        output = coin.name + ' ' + str(price) + '\n'
        print(output)
        file.write(output)
        time.sleep(timeToSleep)
    file.close()


getPrices()