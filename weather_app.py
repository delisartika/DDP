# Kumpulan Module
import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap

# Funsi Untuk Mengetahui informasi tentang Cuaca
def get_weather(city):
    API_key = "1b2f8c4cbcbd0ee0ce628c4130e28dc2"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("Error", "City not found")
        return None
    
    # Mengurai respons JSON untuk mendapatkan informasi cuaca
    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    temperature = weather['main']['temp'] - 273.15
    description = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']

    # Dapatkan URL ikon dan kembalikan semua informasi cuaca
    icon_url = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url, temperature, description, city, country)

# fungsi untuk mengatur cuaca dan fungsi sebuah kota
def search():
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return
    # If kota yang ditemukan untuk menginformasikan cuaca
    icon_url, temperature, description, city, country = result
    location_label.configure(text=f"{city}, {country}")

    # gambar ikon cuaca dari URL dan perbarui label ikon
    image = Image.open(requests.get(icon_url, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon

    # update label suhu dan deskripsi
    temperature_label.configure(text=f"Suhu: {temperature:.2f}°C")
    description_label.configure(text=f"Deskripsi: {description}")

root = ttkbootstrap.Window(themename="morph")
root.title("App Cuaca")
root.geometry("500x500")

# widget entri -> untuk memasukkan nama kota
city_entry = ttkbootstrap.Entry(root, font="Helvetica, 18")
city_entry.pack(pady=10)

# widget tombol -> untuk mencari informasi cuaca
search_button = ttkbootstrap.Button(root, text="Search", command=search, bootstyle="blue")
search_button.pack(pady=10)

# widget label -> untuk menampilkan nama kota/negara
location_label = tk.Label(root, font="Helvetica, 25")
location_label.pack(pady=20)

# widget label -> untuk menampilkan ikon cuaca
icon_label = tk.Label(root)
icon_label.pack()

# widget label -> untuk menampilkan suhu
temperature_label = tk.Label(root, font="Helvetica, 20")
temperature_label.pack()

# widget label -> untuk menampilkan deskripsi cuaca
description_label = tk.Label(root, font="Helvetica, 20")
description_label.pack()

root.mainloop()