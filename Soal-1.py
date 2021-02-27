print("Selamat Datang!")
menu=[]
menu0="\n ---Menu---"
menu1="1. Daftar Kontak"
menu2="2. Tambah Kontak"
menu3="3. Keluar \n"
menu.append(menu0)
menu.append(menu1)
menu.append(menu2)
menu.append(menu3)
for y in menu:
    print(y)

kontak={}
loop=0
while loop!=3:
    loop=0
    x=int(input("### Pilihan menu: "))
    
    if x==1:
        if kontak=={}:
            print("\n XXX Kontak kosong XXXX \n")
        else:    
            for nama,no_hp in kontak.items():
                print(nama,no_hp)
        
    elif x==2:
        nama=input("Nama: ")
        no_hp=input("Nomor HP: ")
        kontak[nama]=no_hp
        print("\n ***Kontak berhasil ditambahkan*** \n")

    elif x<1 or x>3:
        print("Menu tidak tersedia.")

    else:
        print("---Terima kasih, keluar program---")
        loop=3
    
    for y in menu:
        if x!=3:
            print(y)
    




