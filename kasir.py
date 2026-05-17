database_barang = [
    {
        "kode_barang": 1,
        "nama_barang": "Ayam",
        "kategori": "Makanan",
        "harga": 15000,
        "stok": 10
    },
    {
        "kode_barang": 2,
        "nama_barang": "Mizone",
        "kategori": "Minuman",
        "harga": 3000,
        "stok": 12
    },
    {
        "kode_barang": 3,
        "nama_barang": "Pensil",
        "kategori": "Alat Tulis",
        "harga": 2000,
        "stok": 20
    }
]
keranjang = []
opsi = ["Tambah Barang", "Tampilkan Semua Barang", "Cari Kategori", "beli Barang"]

def tambah_barang():
    kode_barang = int(input("Kode Barang: "))
    nama_barang = input("Nama Barang: ")
    kategori = input("Kategori: ")
    harga = int(input("Harga Satuan: "))
    stok = int(input("Stok Barang: "))
    # validasi 
    status = False
    for i in database_barang:
        if kode_barang == i['kode_barang']:
            status = True
            print("Kode barang sudah diapakai.")
    if not status:
        database_barang.append(
            {
                "kode_barang": kode_barang,
                "nama_barang": nama_barang,
                "kategori": kategori,
                "harga": harga,
                "stok": stok
            }
        )
        print("Barang sudah ditambahkan ke database.")

def tampilkan():
    for i in database_barang:
        print(f"""
Kode Barang         : {i['kode_barang']}
Nama Barang         : {i['nama_barang']}
Kategori Barang     : {i['kategori']}
Harga Satuan        : {i['harga']}
Stok Baranag        : {i['stok']}""")

def kategori():
    cari_kategori = input("Mau cari kategori barang apa?: ")
    ketemu = False
    for i in database_barang:
        if cari_kategori.lower() == i['kategori'].lower():
            ketemu = True
            print(f"""
Daftar Kategori {cari_kategori.capitalize()}:
Kode Barang         : {i['kode_barang']}
Nama Barang         : {i['nama_barang']}
Kategori Barang     : {i['kategori']}
Harga Satuan        : {i['harga']}
Stok Barang        : {i['stok']}""")
    if not ketemu:
        print(f"Kategori {cari_kategori.capitalize()} tidak tersedia.")
        
def beli():
    nama_barang = input("Masukan Nama Barang: ")
    jumlah = int(input("Jumlah: "))
    status = False
    for i in database_barang:
        if nama_barang.lower() == i['nama_barang'].lower():
            status = True
            if jumlah <= i['stok']:
                keranjang.append(
                    {
                        "nama_barang": nama_barang,
                        'jumlah': jumlah
                    }
                )
                i['stok'] -= jumlah
                print("Barang berhasil ditambahkan ke keranjang.")
            else:
                print("stok tidak cukup.")
    if not status:
        print("barang tidak tersedia.")

def tambah_keranjang():
    global database_barang
    nama_barang = input("Masukan Nama Barang: ")
    jumlah = int(input("Mau beli berapa?: "))
    ketemu = False
    for i in keranjang:
        if nama_barang.lower() == i['nama_barang'].lower():
            ketemu = True
            i['nama_barang'] = nama_barang
            i['jumlah'] += jumlah
            for k in database_barang:
                if nama_barang.lower() == k['nama_barang'].lower():
                    k['stok'] -= jumlah
    if not ketemu:
        print("not ketemu")
            
print("Selamat Datang Di Toko Kami")
for i in range(len(opsi)):
    print(f"{i+1}. {opsi[i]}")
    
while True:
    opsi = input("Pilih Opsi: ")
    if opsi == "1":
        tambah_barang()
    elif opsi == "2":
        tampilkan()
    elif opsi == "3":
        kategori()
    elif opsi == "4":
        beli()
        while True:
            lagi = input("Mau beli apa lagi?")
            if lagi == 'y':
                tambah_keranjang()
            else:
                print(keranjang)
                break
            
            