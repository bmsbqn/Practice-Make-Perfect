list_nilai = []

while True:
    print ("\nMENU TINDAKAN")
    print ("1. Tambahkan Nilai Dalam List.")
    print ("2. Cek Nilai Dalam List.")
    print ("3. Keluar.")
    
    tindakan = input("\nPilih Tindakan (1/2/3): ")
    if tindakan == "1":
        nilai = input("\nTambhkan Nilai: ")
        list_nilai.append (nilai)
    elif tindakan == "2":
        cek_nilai = input("\nTambahkan Nilai: ")
        index = list_nilai.index (cek_nilai)
        if index == cek_nilai:
            print ("Indeks Elemen", nilai, "Adalah", index)
        else:
            print ("Indeks Tidak Ada dalam list")
    elif tindakan == "3":
        print ("\nKeluar Dari Program!")
        break
    else:
        print ("\nPilihan Anda Tidak Valid!")