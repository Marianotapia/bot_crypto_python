import bs4
from bs4 import BeautifulSoup
import requests
from lxml import html

def price(moneda):
    crypto = {"BTC":"https://coinmarketcap.com/currencies/bitcoin/",
            "PVU":"https://coinmarketcap.com/currencies/plantvsundead/",
            "MIST":"https://coinmarketcap.com/currencies/mist/",
            "REVO":"https://coinmarketcap.com/currencies/revomon/",
            "ETH": "https://coinmarketcap.com/currencies/ethereum/",
            "ZOON": "https://coinmarketcap.com/currencies/cryptozoon/"}
    coinmarket = requests.get(crypto[moneda])
    soup = bs4.BeautifulSoup(coinmarket.text,"html.parser")
    precio_crypto = soup.find("div",{"class":"priceValue___11gHJ"})
    return("1 " + moneda +" = " + precio_crypto.text + " USD")