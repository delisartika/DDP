kendaraan=["namaKendaraan","JenisKendaraan","ccKendaraan","warna kendaraan","roda kendaraan"]
kendaraan.append(100)
kendaraan.append("motor")
kendaraan.insert(2,"honda")
print(kendaraan)

menghitung = input ("Anda ingin menghitung luas bangun datar apa?")
match menghitung:
    case "1":
        sisi= int(input("masukkan nilai sisi"))
        luas= sisi*sisi
        print("luas persegi",persegi)
    case "2":
        jari_jari= int(input("masukkan nilai jari jari"))
        luas=3.14*jari_jari*jari_jari
        print("luas lingkaran",lingkaran)
    case "3":
        alas= int(input("masukkan nilai alas"))
        tinggi= int(input("masukkan nilai tinggi"))
        luas= 0.5*alas*tinggi
        print("luas segitiga",segitiga)
    case _:
        print("salah pilih pilihan")

