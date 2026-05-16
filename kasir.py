database = []
pilih_menu = ["Tambah Barang", "Tampilkan Semua Barang"]



def tambah_barang():
    id_barang = int(input("Masukan ID Barang: "))
    nama_barang = input("Nama Barang: ")
    kategori = input("Kategori: ")
    harga = int(input("Masukan Harga: "))
    stok = int(input("Stok: "))
    
    with open("kasir.txt", "r") as cek_data:
        status_ketemu = False
        tampilkan()
        for i in database:
            if nama_barang == i['nama_barang']:
                status_ketemu = True
                print("gagal, duplikat data")
                break
        if not status_ketemu:
            with open("kasir.txt", "a") as data_menu:
                data_menu.write(f"{id_barang},{nama_barang},{kategori},{harga},{stok}\n")    

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
    print("\nData berhasil ditampilkan.")
                
         
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