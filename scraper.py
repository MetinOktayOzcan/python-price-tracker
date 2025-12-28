from bs4 import BeautifulSoup
from curl_cffi import requests
import time
import random

def scraper(url):
    if "amazon" in url:
        return amazonScraper(url)
    elif "trendyol" in url:
        return trendyolScraper(url)
    else:
        return "URL hatali veya Desteklenmeyen web site girdiniz"
    
    


def amazonScraper (url):
    try:
        resuld=requests.get(url, impersonate="chrome110", timeout=10)
        doc = BeautifulSoup(resuld.text,"html.parser")
        prices = doc.find_all("span", class_="a-price-whole")
        prices =prices[0].parent
        prices=prices.get_text().replace(".", "")
        prices=prices.replace(",", ".")
        prices=prices.replace("TL","")
        prices=int(prices[0:-3])
        return prices
    except Exception as e:
        return None

def trendyolScraper (url):
    try:
        resuld=requests.get(url, impersonate="chrome110", timeout=10)
        doc = BeautifulSoup(resuld.text,"html.parser")
        prices = doc.find_all("span", class_="discounted")
        prices =prices[0].parent
        prices=prices.get_text().replace(".", "")
        prices=int(prices.replace(" TL",""))
        return prices
    except Exception as e:
        return None
