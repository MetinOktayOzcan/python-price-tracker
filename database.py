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


# #Veritabanı testi için eklenen kodlar
# urunEkle("test")

# c.execute("SELECT * FROM urunBilgi")
# bilgiler = c.fetchall()
# for bilgi in bilgiler:
#     print(bilgi)

        










