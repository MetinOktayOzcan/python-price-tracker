import database
import scraper
import time
import notification

def botFiyatTakip():
    veriler = database.takipListesiniGetir()

    if not veriler:
        print("veri bulunmuyor")
        return

    for veri in veriler:
        link=veri[1]
        cekilenFiyat=scraper.scraper(link)
        if cekilenFiyat is not None:
            database.urunFiyatGuncelle(link,cekilenFiyat)
            time.sleep(5)
            print(f"{link[0:15]} {cekilenFiyat} olarak güncellendi")

            notification.bildirimGonder(
                "Fiyat Güncellendi", 
                f"Ürün fiyatı güncellendi: {cekilenFiyat} TL"
            )
            
        else:
            print("Fiyat çekilemedi")

if __name__ == "__main__":
    while True:
        botFiyatTakip()
        print("tüm linkleri güncellemek için 10 saniye bekleniyor")
        time.sleep(10)
