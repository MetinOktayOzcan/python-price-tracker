from bs4 import BeautifulSoup
from curl_cffi import requests
import time
import random

def scraper(url):
    bolme=url.split("/")
    website = bolme[2]
    website=url.split(".")
    website=website[1]

    match website:
        case "amazon":
            amazonScraper(url)
        case "trendyol":
            tredyolScraper(url)
        case _:
            return "hata"


def amazonScraper (url):
    resuld=requests.get(url, impersonate="chrome110", timeout=10)
    doc = BeautifulSoup(resuld.text,"html.parser")
    prices = doc.find_all("span", class_="a-price-whole")
    prices =prices[0].parent
    prices=prices.get_text().replace(".", "")
    prices=prices.replace(",", ".")
    prices=prices.replace("TL","")
    prices=int(prices[0:-3])
    return prices
    print(prices)

def tredyolScraper (url):
    resuld=requests.get(url, impersonate="chrome110", timeout=10)
    doc = BeautifulSoup(resuld.text,"html.parser")
    prices = doc.find_all("span", class_="discounted")
    prices =prices[0].parent
    prices=prices.get_text().replace(".", "")
    prices=int(prices.replace(" TL",""))
    return prices

scraper("https://www.amazon.com.tr/Apple-iPhone-Pro-Max-teknolojisine/dp/B0FQFVL6DK")