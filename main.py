import database
import scraper 

def urunEklemeIslemi():
    urunIsmi = input("Eklemek istediğiniz ürünün ismini giriniz: ")
    yanit = database.urunEkle(urunIsmi)
    print(yanit)

def urunleriGoruntule():
    print("-----Ürünler-----")
    veriler = database.tumUrunlerinIsminiListele()
    for veri in veriler:
        print(f"Urun:{veri[0]}")

    print("-----------------")
    islem = input("İşlem yapacağınız ürünün ismini giriniz: ")
    for veri in veriler:
        if islem == veri[0]:
         print(F"seçtiğiniz ürün {veri[0]} yapmak istediğiniz işlem")
         print("""
                    1-Ürüne link ekle
                    2-Ürünün en ucuz fiyatını bul
                    3-Ürünü sil
                    4-ürünün linkini sil
                    5-Çık
              """)
         secenek = input("Hangi işlemi yapmak istiyorsunuz 1-5: ")   
         
         if secenek == "1":
             link = input("site URL")
             siteismi = input("site ismi")
             fiyat = scraper.scraper(link)
             if fiyat is not None:
                database.urunUrlEkle(veri[0],siteismi,link,1,fiyat)
             else:
                 print("Fiyat çekilemedi")   
         elif secenek == "2":
            print("-----------------")
            print(database.enUcuzunuBul(veri[0]))
         elif secenek == "3":
            print("-----------------")
            mesaj =database.urunSil(veri[0])
            if mesaj is not None:
                print("Hata")
            else:
                print(f"{veri[0]} ürünü başarıyla silindi")
         elif secenek == "4":
             print("-----------------")
             linkler = database.urunLinkiniGetir(veri[0])
             for link in linkler:
                 print(link)
             sUrl=input("Silinecek url'i giriniz: ")
             mesaj= database.tekLinkSil(sUrl)
             if mesaj is not None:
                print("Hata")
             else:
                print(f"link başarıyla silindi")
         elif secenek == "5":
             print("ana menüye dönülüyor...")
             break
    print("-----------------")
    

def main():
    while True:
        print("""
        İşlemler
        1-Ürün Ekle
        2-Ürünleri Görüntüle
        q-Çıkış
        """)
        islem = input("Yapmak istediğiniz işlemi seçiniz 1-2: ")
        match islem:
            case "1":
                urunEklemeIslemi()
            case "2":
                urunleriGoruntule()
            case "q":
                print("Programdan çıkılıyor...")
                break
            case _:
                print("Hatalı seçim")

if __name__ == "__main__":
    main()