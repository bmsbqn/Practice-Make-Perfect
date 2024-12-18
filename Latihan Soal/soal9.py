nama_mahasiswa = []
nim_mahasiswa = []
nilai_mahasiswa = []

while True:
    print ("\n==============================")
    print ("=============MENU=============")
    print ("1. Input Data Dan Nilai Mahasiswa.")
    print ("2. Tampilkan Data Dan Nilai Mahasiswa.")
    print ("3. Cek Kelulusan Mahasiswa.")
    print ("4. Cek Nilai Tertinggi/Terendah Mahasiswa")
    print ("5. Cek Nilai Rata-Rata Mahasiswa")
    print ("6. Cek Kelas Lulus/Tidak Lulus.")
    print ("7. Keluar.")
    
    pilihan = input("Pilih Menu Tindakan (1/2/3/4/5/6/7): ")
    if pilihan == "1":
        jumlah_mahasiswa = int(input("Jumlah Siswa: "))
        for i in range (jumlah_mahasiswa):
            nama = input("Masukan Nama: ")
            nim = input("Masukan NIM: ")
            nilai = int(input("Masukan Nilai: "))
            nama_mahasiswa.append (nama)
            nim_mahasiswa.append (nim)
            nilai_mahasiswa.append (nilai)
    elif pilihan == "2":
        for i in range (len(nama_mahasiswa)):
            print ("\nNama: " + nama_mahasiswa[i] + "\nNIM: " + str (nim_mahasiswa[i]) + "\nNilai: " + str (nilai_mahasiswa[i]))
    elif pilihan == "3":
        for i in range (len(nama_mahasiswa)):
            status = ("LULUS") if nilai_mahasiswa[i] >= 70 else ("TIDAK LULUS")
            print ("\nNama: " + nama_mahasiswa[i] + "\nNIM: " + str (nim_mahasiswa[i]) + "\nNilai: " + str (nilai_mahasiswa[i]) + "\nStatus: " + status)
    elif pilihan == "4":
        print("\nNilai Tertinggi  : " + str(max(nilai_mahasiswa)))
        print("Nilai Terendah   : " + str(min(nilai_mahasiswa)))
    elif pilihan == "5":
        rata_rata = sum(nilai_mahasiswa)/len(nilai_mahasiswa)
        print ("Nilai Rata-Rata:", rata_rata)
    elif pilihan == "6":
        rata_rata = sum(nilai_mahasiswa)/len(nilai_mahasiswa)
        status_kelas = "Kelas Lulus" if rata_rata >= 70 else "Tidak Lulus"
        print ("Status Kelas:", status_kelas)
    elif pilihan == "7":
        print ("Keluar Dari Program!")
        break
    else:
        print ("Tidak Ada Dalam Tindakan!")
        break