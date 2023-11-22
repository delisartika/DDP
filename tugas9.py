def profil(nama, alamat, gender, umur, hoby):
    print("Nama:", nama)
    print("Alamat:", alamat)
    print("Jenis Kelamin:", gender)
    print("Umur:", umur)
    print("Hobi:", hoby)
profil("Delisa", "Depok", "Wanita", "18 tahun", "Shopping")

def kelulusan(nilai):
    if nilai < 60:
        print("Gagal")
    elif 61 <= nilai <= 70:
        print("Baik")
    elif 71 <= nilai <= 80:
        print("Sangat Baik")
    elif 81 <= nilai <= 100:
        print("Istimewa")
    else:
        print("Gagal")
kelulusan(60)

def ganjil(angka):
    for i in range(1, angka + 1, 2):
        print(i)
ganjil(100)