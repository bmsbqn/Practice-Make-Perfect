item_belanja = []
item_dibeli = []

while True:
    print ("\nMENU PILIHAN")
    print ("1. Menambahkan Item Belanja.")
    print ("2. Menghapus Item Belanja.")
    print ("3. Menampilkan Daftar Belanja.")
    print ("4. Keluar.")
    
    pilihan = input("\nMasukan Pilihan Anda: ")
    
    if pilihan == "1":
        belanja = input("\nMasukan Daftar Belanja Anda: ")
        item_belanja.append (belanja)
    elif pilihan == "2":
        print ("\nHapus Item Belanja")
        belanja = input("Hapus Item: ")
        item_belanja.remove (belanja)
        item_dibeli.append (belanja)
    elif pilihan == "3":
        print ("\nDaftar Belanja Anda")
        print ("Item Belanja:", item_belanja)
        print ("Item Terbeli:", item_dibeli)
    elif pilihan == "4":
        print ("Keluar Dari Program.\n")
        break
    else :
        print ("\nPilihan Anda Tidak Valid!")
