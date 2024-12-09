nilai_ujian = []
nilai_tertinggi = []
nilai_terendah = []
nilai_ratarata = []

while True:

    print ("\n>>> MENU TINDAKAN <<<")
    print ("1. Input Nilai Ujian.")
    print ("2. Cek Nilai Tertinggi.")
    print ("3. Cek Nilai Terendah.")
    print ("4. Cek Nilai Rata-Rata.")
    print ("5. Keluar.")


    pilihan = input("\nPilih Tindakan (1/2/3/4): ") 
    if pilihan == "1":
        input_nilai = int (input("Input Nilai Ujian: "))
        nilai_ujian.append (input_nilai)
        print ("Nilai Yang Di Input:", nilai_ujian)
    elif pilihan == "2":
        nilai_tertinggi = max (nilai_ujian)
        print ("\nNilai Tertinggi:", nilai_tertinggi)
    elif pilihan == "3":
        nilai_terendah = min (nilai_ujian)
        print ("\nNilai Terendah:", nilai_terendah)
    elif pilihan == "4":
        nilai_ratarata = sum(nilai_ujian)/len(nilai_ujian)
        print ("\nNilai Rata-Rata:", nilai_ratarata)
    elif pilihan == "5":
        print ("Keluar Dari Program")
        break
