# 🛒 Fiyat Takip Botu

Merhaba, bu proje kişisel bir ihtiyaçtan ortaya çıktı. E-ticaret sitelerindeki (Amazon, Trendyol vb.) fiyatları sürekli girip kontrol etmek yerine, bu işi benim yerime yapacak bir otomasyon geliştirmek istedim.

Bu projeyi geliştirirken Python, SQL veritabanı mantığı ve Web Scraping (Veri Kazıma) konularında kendimi geliştirmeyi hedefledim.

## 💡 Ne Yapıyor?
Bu bot, belirlediğim ürün linklerini arka planda sürekli tarıyor. Eğer bir indirim yakalarsa veya fiyat değişirse bana Windows üzerinden bildirim gönderiyor.

## 🛠️ Neler Kullandım?
Projeyi geliştirirken özellikle şunları tecrübe ettim:

* **Python:** Ana programlama dili.
* **SQLite:** Verileri (Linkleri, eski ve yeni fiyatları) tutmak için. Başta dosya sistemine kaydediyordum ama veriler artınca SQL kullanmanın daha verimli olduğunu gördüm.
* **Web Scraping & Anti-Bot:** Normal `requests` kütüphanesi ile veri çekerken bazı sitelerin bot korumasına takıldım. Bunu aşmak için `curl_cffi` kütüphanesini ve User-Agent rotasyonu (farklı tarayıcı kimlikleri) kullandım.
* **Plyer:** Masaüstü bildirimleri için.

## 🚀 Kurulum

Projeyi denemek isterseniz:

1.  Repoyu indirin.
2.  Gerekli kütüphaneleri kurun:
    `pip install -r requirements.txt` (veya `pip install beautifulsoup4 curl_cffi plyer`)
3.  Arayüz için `main.py` dosyasını, arka planda takip için `bot.py` dosyasını çalıştırın.

## 🔮 Gelecek Planlarım (To-Do)
Şu an proje sorunsuz çalışıyor ama ileride şunları eklemeyi düşünüyorum:
* [ ] Daha detaylı bir Admin Paneli (Belki Web tabanlı).
* [ ] Fiyat değişimlerini grafik olarak gösterme.
* [ ] Sadece masaüstü değil, e-posta ile bildirim gönderme.

---
*Bu proje Bilgisayar Programcılığı eğitimim sırasında geliştirdiğim kişisel projemdir.*