nama_barang = []
harga_barang = []

while True:
  print ("\nMENU TINDAKAN")
  print ("1. Masukan Barang dengan Harga.")
  print ("2. Tampilkan List Barang Dengan Harga.")
  print ("3. Total Harga Seluruh Barang.") 
  print ("4. Cek Harga Barang Tertinggi/Terendah.") 
  print ("5. Keluar Dari Program.")
  
  pilihan = input("\nPilih Tindakan (1/2/3/4/5): ")
  if pilihan == "1":
    barang = input ("\nInput Nama Barang: ")
    harga = int(input("Input Harga Barang: Rp."))
    nama_barang.append (barang)
    harga_barang.append (harga)
  elif pilihan == "2":
    for i in range (len(nama_barang)):
      print ("\nNama Barang: ", nama_barang[i], "\nHarga Barang: Rp.",harga_barang[i])
  elif pilihan == "3":
    total_harga = sum(harga_barang)
    print ("Total: Rp.",total_harga)
  elif pilihan == "4":
    print ("\nHarga Tertinggi:", max(harga_barang),"\nHarga Terendah:", min(harga_barang))
  elif pilihan == "5":
    print ("Keluar Dari Program!")
    break
  else:
    print ("Pilihan Anda Tidak Valid!")