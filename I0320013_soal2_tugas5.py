nama= input("Masukkan nama:")
nilai= int(input("Masukkan nilai:"))
if 85 <= nilai <= 100:
    print("Halo,",nama,"!","Nilai anda setelah dikonversi adalah A")
elif nilai >= 80:
    print("Halo,",nama,"!","Nilai anda setelah dikonversi adalah A-")
elif nilai >= 75:
    print("Halo,",nama,"!","Nilai anda setelah dikonversi adalah B+")
elif nilai >= 70:
    print("Halo,",nama,"!","Nilai anda setelah dikonversi adalah B")
elif nilai >= 65:
    print("Halo,",nama,"!","Nilai anda setelah dikonversi adalah C+")
elif nilai >= 60:
    print("Halo,",nama,"!","Nilai anda setelah dikonversi adalah C")
else:
    print("Halo,",nama,"!","Nilai anda setelah dikonversi adalah E")