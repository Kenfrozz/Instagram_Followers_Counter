import instaloader
import tkinter as tk
from tkinter import Label, Entry, Button

def get_follower_count():
    # Hesap adını al
    account_name = entry_account.get()

    # Hesap adını kontrol et
    if not account_name:
        result_label.config(text="Lütfen bir hesap adı girin.")
        return

    # Instaloader objesini oluştur
    L = instaloader.Instaloader()

    try:
        # Profili yükle
        profile = instaloader.Profile.from_username(L.context, account_name)

        # Takipçi sayısını al
        follower_count = profile.followers

        # Sonuçları etikete yazdır
        result_label.config(text=f"{account_name} Instagram hesabı {follower_count} takipçiye sahip.")
    except instaloader.exceptions.ProfileNotExistsException:
        result_label.config(text=f"{account_name} adlı hesap bulunamadı.")
    except Exception as e:
        result_label.config(text=f"Hata: {str(e)}")

# Ana uygulama penceresini oluştur
app = tk.Tk()
app.title("Instagram Takipçi Sayacı")

# Hesap adı giriş etiketi ve giriş kutusu
account_label = Label(app, text="Hesap Adı:")
account_label.pack()

entry_account = Entry(app)
entry_account.pack()

# Takipçi sayısını getir butonu
get_follower_button = Button(app, text="Takipçi Sayısını Getir", command=get_follower_count)
get_follower_button.pack()

# Sonuçları gösteren etiket
result_label = Label(app, text="")
result_label.pack()

# Uygulamayı başlat
app.mainloop()
