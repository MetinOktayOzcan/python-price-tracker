import sqlite3
import datetime

conn=sqlite3.connect('fiyatTakip.db')
c =conn.cursor()

def veritabaniOlustur():
    c.execute("PRAGMA foreign_keys = ON;") 
    c.executescript("""
    CREATE TABLE IF NOT EXISTS urunBilgi(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            urunAdi TEXT UNIQUE,
            urunEklemeTarihi DATETIME   
            );                

    CREATE TABLE IF NOT EXISTS urunAdresi(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            urunSiteIsmi TEXT,
            urunUrl TEXT UNIQUE,
            urunAktif BOOLEAN DEFAULT 1,    
            urunGuncelFiyat REAL,
            FOREIGN KEY(product_id) REFERENCES urunBilgi(id) ON DELETE CASCADE
            );
            
    CREATE TABLE IF NOT EXISTS urunFiyat(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            link_id INTEGER,
            urunFiyat REAL,
            urunTarih DATETIME,
            FOREIGN KEY(link_id) REFERENCES urunAdresi(id) ON DELETE CASCADE
            );
    """)
    conn.commit()

veritabaniOlustur()

def urunEkle(urunAdi):
    c.execute("SELECT id FROM urunBilgi WHERE urunAdi=?",(urunAdi,))
    veri = c.fetchone()

    if veri is not None:
        return "Bu ismiyle Kayıtlı Ürün Bulunuyor"
    else:
        zaman = datetime.datetime.now()
        c.execute("INSERT INTO urunBilgi (urunAdi,urunEklemeTarihi) VALUES (?,?)", (urunAdi,zaman))
        conn.commit()

def urunUrlEkle(urunAdi,urunSiteIsmi,urunUrl,urunAktif,urunGuncelFiyat):
    c.execute("SELECT id FROM urunBilgi WHERE urunAdi=?",(urunAdi,))
    product_id = c.fetchone()

    if product_id is not None:
        product_id= product_id[0]
        try:
                c.execute("INSERT INTO urunAdresi (product_id, urunSiteIsmi, urunUrl, urunAktif, urunGuncelFiyat) VALUES (?,?,?,?,?)", 
                        (product_id, urunSiteIsmi, urunUrl, urunAktif, urunGuncelFiyat))
                conn.commit()
        except sqlite3.IntegrityError:
             return "HATA:Vertitabanında bu url ile kayıt mevcut"
    else:
         return "Bu isimle bir ürün bulunmuyor"    


# c.execute("SELECT * FROM urunAdresi")
# bilgiler = c.fetchall()
# for bilgi in bilgiler:
#         print(bilgi)

        










