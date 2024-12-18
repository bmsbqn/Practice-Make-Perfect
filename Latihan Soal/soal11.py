# Soal 3: Buku Perpustakaan
# Sebuah perpustakaan ingin mencatat daftar buku yang dipinjam oleh pengunjung. Program ini harus:

# Meminta pengguna memasukkan nama buku yang dipinjam.
# Menghentikan proses input jika pengguna mengetikkan "selesai".
# Menampilkan daftar buku yang dipinjam.
# Menghitung total buku yang dipinjam.
# Kebutuhan Program:

# Gunakan list untuk menyimpan nama buku.
# Gunakan loop untuk proses input hingga pengguna mengetik "selesai".


buku_pinjam = []

while True:
  print ("PERPUSTAKAAN UINMA")
  print ("1. Pinjam Buku")
  print ("2. Daftar Buku Pinjam")
  print ("3. Keluar")
  
  pilihan = input ("\nMasukan Pilihan Anda: ")
  
  if pilihan == "1":
      buku = input("\nJudul Buku: ")
      buku_pinjam.append (buku)
  elif pilihan == "2":
    print ("\nDafta Buku Pinjam:", buku_pinjam)
  elif pilihan == "3":
    print ("\nTerima Kasih Sudah Berkunjung\n")
    break