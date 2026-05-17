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
        
def tambah_keranjang():
    nama_barang = input("Nama Barang: ")
    ketemu = False
    for i in database_barang:
        if nama_barang.lower() == i['nama_barang'].lower():
            jumlah = int(input("Mau beli berapa?: "))
            ketemu = True
            if jumlah <= i['stok']:
                cek_keranjang = False
                for k in keranjang:
                    if nama_barang.lower() == k['nama_barang'].lower():
                        cek_keranjang = True
                        k['nama_barang'] = nama_barang
                        k['jumlah'] += jumlah
                        i['stok'] -= jumlah
                if not cek_keranjang:
                    keranjang.append(
                        {
                            "nama_barang": nama_barang,
                            "jumlah": jumlah
                        }
                    )
                    i['stok'] -= jumlah
            else:
                print(f"Maaf, sisa stok {nama_barang} tidak mencukupi. sisa stok: {i['stok']}")
    if not ketemu:
        print("Maaf, barang tidak tersedia.")         


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
        tambah_keranjang()
        while True:
            beli_lagi = input("Mau beli lagi?(y): ")
            if beli_lagi == "y":
                tambah_keranjang()
            else:
                print(keranjang)
                break