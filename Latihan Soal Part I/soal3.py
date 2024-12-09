input_angka = []
balik_angka = []

while True:
    print ("\nMENU TINDAKAN")
    print ("1. Input Angka.")
    print ("2. Tampilkan Hasil Input.")
    print ("3. Membalikkan Hasil Input.")
    print ("4. Keluar.")
    
    pilihan = input("Masukan Pilihan (1/2/3/4): ")
    if pilihan == "1":
        angka = int (input("Masukan Angka: "))
        input_angka.append (angka)
    elif pilihan == "2":
        print ("Hasil Input:", input_angka)
    elif pilihan == "3":
        for i in range(len(input_angka)-1,-1,-1):
            balik_angka.append (input_angka[i])
        print ("Hasil Membalikan Angka:", balik_angka)
    elif pilihan == "4":
        print ("Keluar Dari Program!")
        break
    else:
        print ("Pilihan Anda Tidak Valid!")
