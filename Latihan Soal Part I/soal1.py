siswa_in = []
siswa_out = []

while True:
    print("""
Daftar Nama Peserta Ujian
==========================
1. Masukkan Nama Peserta Ujian
2. Tampilkan Daftar Nama Peserta Ujian
3. Keluarkan Peserta dari Daftar
4. Keluar
""")
    pilihan = input("Pilih Tindakan (1/2/3/4): ")
    
    if pilihan == "1":
        nama = input("Masukkan Nama Peserta: ")
        siswa_in.append(nama)
        # print(nama + " berhasil ditambahkan.")
    
    elif pilihan == "2":
        print("\nDaftar Nama Peserta Ujian:")
        if siswa_in:
            i = 1
            for nama in siswa_in:
                print(str(i) + ". " + nama)
                i += 1
        else:
            print("Tidak ada peserta dalam daftar.")
        print("")
    
    elif pilihan == "3":
        if not siswa_in:
            print("Daftar peserta kosong. Tidak ada peserta yang dapat dikeluarkan.\n")
            continue
        print("\nDaftar Nama Peserta Ujian:")
        i = 1
        for nama in siswa_in:
            print(str(i) + ". " + nama)
            i += 1
        nama = input("Masukkan Nama Peserta yang Akan Dikeluarkan: ")
        if nama in siswa_in:
            siswa_in.remove(nama)
            siswa_out.append(nama)
            print(nama + " berhasil dikeluarkan.\n")
        else:
            print("Nama tidak ditemukan dalam daftar.\n")
    
    elif pilihan == "4":
        print("\nProgram selesai.")
        break
    
    else:
        print("Pilihan tidak valid. Coba lagi.\n")
