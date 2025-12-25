import sqlite3

conn=sqlite3.connect('fiyatTakip.db')

c =conn.cursor()

def veritabaniOlustur():    
    c.executescript("""
    CREATE TABLE IF NOT EXISTS urunBilgi(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            urunAdı text,
            urunSitesi text,
            urunUrl text
            );
            
    CREATE TABLE IF NOT EXISTS urunFiyat(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            urun_id INTEGER,
            urunFiyat REAL,
            urunTarih TEXT,
            FOREIGN KEY(urun_id) REFERENCES urunBilgi(id)
            );
    """)
    conn.commit()

def veritabaniKayit(urunAdi,urunSitesi,urunUrl):
    c.execute("INSERT INTO urunBilgi (urunAdı,urunSitesi,urunUrl) VALUES (?,?,?)", (urunAdi, urunSitesi, urunUrl))
    conn.commit()

#veritabaniKayit("amazon","amazon","amazon")
c.execute("SELECT * FROM urunBilgi")
print(c.fetchall())




