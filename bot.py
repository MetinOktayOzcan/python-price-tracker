import database
import scraper
import time

def botFiyatTakip():
    veriler = database.takipListesiniGetir()
    link=veriler[1]

    if not veriler:
        print("veri bulunmuyor")
        return

    cekilenFiyat=scraper.scraper(link)
    database.urunFiyatGuncelle(link,cekilenFiyat)
    time.sleep(7)

botFiyatTakip()
