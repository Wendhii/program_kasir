database = []
pilih_menu = ["Tambah Barang", "Tampilkan Semua Barang", "Cari berdasarkan kategori"]


             
            

def tambah_barang():
    id_barang = int(input("Masukan ID Barang: "))
    nama_barang = input("Nama Barang: ")
    kategori = input("Kategori: ")
    harga = int(input("Masukan Harga: "))
    stok = int(input("Stok: "))
    # validasi admin
    user_admin = input("Masukan Nama Admin: ")
    status_admin = False
    with open("admin.txt", "r") as admin:
        for i in admin:
            data_admin = i.split(",")
            if user_admin.lower() in data_admin:
                status_admin = True        
                status_ketemu = False
                for i in database:
                    if id_barang == int(i['id_barang']):
                        status_ketemu = True
                        print("gagal, duplikat data")
                        break
                if not status_ketemu:
                    with open("kasir.txt", "a") as data_menu:
                        data_menu.write(f"{id_barang},{nama_barang},{kategori},{harga},{stok}\n")  
        if not status_admin:
            print("Hanya Admin yang bisa menambahkan barang.")  

def tampilkan():
    with open("kasir.txt", "r") as ambil_data:
        for i in ambil_data:
            data = i.strip().split(",")
            database.append(
                {
                    "id_barang": data[0],
                    "nama_barang": data[1],
                    "kategori": data[2],
                    "harga": data[3],
                    "stok": data[4]
                }
            )

def kategori():
    user_kategori = input("Masukan Kategori Barang: ")
    ketemu = False
    with open("kasir.txt", "r") as data:
        for i in data:
            cari_kategori = i.strip().split(",")
            if user_kategori.lower() in cari_kategori[2].lower():
                print(f"""
Kategori {user_kategori.capitalize()} Ditemukan:
ID Barang       : {cari_kategori[0]}
Nama Barang     : {cari_kategori[1]}
Kategori        : {cari_kategori[2]}
Harga           : {cari_kategori[3]}
Stok            : {cari_kategori[4]}""")
                ketemu = True
                # break
        if not ketemu:
            print(f"Maaf, kategori {user_kategori.capitalize()} tidak ditemukan!")
               
         
for i in range(len(pilih_menu)):
    print(f"{i+1}. {pilih_menu[i]}")
    
while True:
    menu = input("Pilih Menu: ")
    if menu == "1":
        tambah_barang()
    elif menu == "2":
        tampilkan()
        for i in database:
            print(f"""
ID          : {i['id_barang']}
Nama Barang : {i['nama_barang']}
Kategori    : {i['kategori']}
Harga       : {i['harga']}
Stok        : {i['stok']}""")
    elif menu == "3":
        kategori()