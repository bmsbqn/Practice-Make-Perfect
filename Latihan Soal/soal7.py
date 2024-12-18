list1 = []
list2 = []

while True:
    print ("\nMENU TINDAKAN")
    print ("1. Input List Pertama.")
    print ("2. Input List Kedua.")
    print ("3. Tampilkan List.")
    print ("4. Gabungkan Kedua List.")
    print ("5. Keluar")
    pilihan = input("Masukan Pilihan Anda (1/2/3/4/5): ")
    if pilihan == "1":
        input1 = input("\nMasukan List: ")
        list1.append (input1)
    elif pilihan == "2":
        input2 = input("\nMasukan List: ")
        list2.append (input2)
    elif pilihan == "3":
        print ("\nList 1 :", list1)
        print ("List 2 :", list2)
    elif pilihan == "4":
        list3 = list1 + list2
        print ("\nList:", list3)
    elif pilihan == "5":
        print ("\nKeluar Dari Program")
        break
    else:
        print ("Pilihan Anda Tidak Valid!")