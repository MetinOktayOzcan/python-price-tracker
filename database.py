import sqlite3

conn=sqlite3.connect('fiyatTakip.db')

c =conn.cursor()

def veritabanıOlustur():    
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
    conn.close()

def veritabanıKayıt():
    c.execute("INSERT INTO urunBilgi VALUES ()")



