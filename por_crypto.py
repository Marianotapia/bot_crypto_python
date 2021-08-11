import bs4
from bs4 import BeautifulSoup
import requests
from lxml import html
def multiplo(moneda):
    crypto = {"BTC":"https://coinmarketcap.com/currencies/bitcoin/",
                "PVU":"https://coinmarketcap.com/currencies/plantvsundead/",
                "MIST":"https://coinmarketcap.com/currencies/mist/",
                "REVO":"https://coinmarketcap.com/currencies/revomon/",
                "ETH": "https://coinmarketcap.com/currencies/ethereum/",
                "ZOON": "https://coinmarketcap.com/currencies/cryptozoon/"}
    coinmarket = requests.get(crypto[moneda])
    soup = bs4.BeautifulSoup(coinmarket.text,"html.parser")
    precio_crypto = soup.find("div",{"class":"priceValue___11gHJ"})
    precio_crypto2 = precio_crypto.text.split("$")[1]

    return(float(precio_crypto2))

