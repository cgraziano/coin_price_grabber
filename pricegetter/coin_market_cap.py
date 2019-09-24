from pricegetter.pricegetter import PriceGetter
import json

class CoinMarketCap(PriceGetter):
    def __init__(self, session):
        self.baseUrl = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
        self.session = session

    def getPrice(self, coinName):
        url = self.baseUrl
        parameters = {'id':coinName}
        response = self.session.get(url, params=parameters)
        data = json.loads(response.text)
        dollarAmountFloat = data['data'][coinName]['quote']['USD']['price']
        dollarAmount2Decimal = round(dollarAmountFloat, 2)
        return dollarAmount2Decimal
