list_genap = []
list_ganjil = []

while True:
    print ("\nMENU PILIHAN")
    print ("1. Input Angka.")
    print ("2. Tampilkan Hasil.")
    print ("3. Keluar.")
    print ("_______________________________")
    pilihan = input("Masukan Pilihan Anda (1/2/3): ")
    if pilihan == "1":
        angka = int (input("Masukan Angka: "))
        if angka % 2 == 0:
            list_genap.append (angka)
        else:
            list_ganjil.append (angka)
    if pilihan == "2":
        print ("\nGenap:", list_genap)
        print ("Ganjil:", list_ganjil)
    if pilihan == "3":
        print ("\n> Keluar Dari Program! <\n")
        break
