from plyer import notification

def bildirimGonder(baslik, mesaj):
    try:
        notification.notify(
            title = baslik,
            message = mesaj,
            app_name = "Fiyat Takip Botu",
            timeout = 10
        )
        print(f"Bildirim gönderildi: {mesaj}")
    except Exception as e:
        print(f"Bildirim hatası: {e}")

if __name__ == "__main__":
    bildirimGonder("Test", "Test Bildirimi")