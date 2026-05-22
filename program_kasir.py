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
total = 0
opsi = ["Tambah Barang", "Tampilkan Semua Barang", "Cari Kategori", "beli Barang", "Pembayaran"]

# bagian Shabilla dari sini
def tambah_barang():
    kode_barang = int(input("Kode Barang: "))
    nama_barang = input("Nama Barang: ")
    kategori = input("Kategori: ")
    harga = int(input("Harga Satuan: "))
    stok = int(input("Stok Barang: "))
    
    # mengecek kode barang apakah sudah ada atau belum 
    status = False
    for i in database_barang:
        # kondisi kode barang sudah dipakai
        if kode_barang == i['kode_barang']:
            status = True
            print("Kode barang sudah dipakai.")
    # kondisi kode barang belum dipakai
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
# Samipai sini

# Bagian Tantri dari sini
def kategori():
    cari_kategori = input("Mau cari kategori barang apa?: ")
    ketemu = False
    for i in database_barang:
        # kondisi apabila kategori tersedia
        if cari_kategori.lower() == i['kategori'].lower():
            ketemu = True
            print(f"""
Daftar Kategori {cari_kategori.capitalize()}:
Kode Barang         : {i['kode_barang']}
Nama Barang         : {i['nama_barang']}
Kategori Barang     : {i['kategori']}
Harga Satuan        : {i['harga']}
Stok Barang        : {i['stok']}""")
    # konsdisi apabila kategori tidak ditemukan
    if not ketemu:
        print(f"Kategori {cari_kategori.capitalize()} tidak tersedia.")

def diskon():
    global total
    diskon = 0
    pajak = 0.11
    # kondisi apabila total belanja lebih dari 100.000
    if total > 100000:
        diskon = 0.1
    # kondsi apabila total belanja lebih dari 50.000
    elif total > 50000:
        diskon = 0.05
        
    total *= diskon
    # total_pajak = total * pajak
    # k['harga'] -= total_diskon
    # k['harga'] += total_pajak 
    return total
# Sampai Sini
       
def tambah_keranjang():
    global total
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
                        # k['harga'] += i['harga'] * jumlah
                        i['stok'] -= jumlah
                        total += i['harga'] * jumlah
                if not cek_keranjang:
                    keranjang.append(
                        {
                            "nama_barang": nama_barang,
                            "jumlah": jumlah,
                            "harga": i['harga']
                        }
                    )
                    i['stok'] -= jumlah
                    total += i['harga'] * jumlah
            else:
                print(f"Maaf, sisa stok {nama_barang} tidak mencukupi. sisa stok: {i['stok']}")
    if not ketemu:
        print("Maaf, barang tidak tersedia.")         

def bayar():
    global total
    if keranjang == []:
        print("Keranjang masih kosong, belanja dulu.")
        return
    # diskon()
    uang_pelanggan = int(input("Masukan uang pelanggan: "))
    if uang_pelanggan < total:
        print("Maaf, Uang tidak cukup untuk melakukan transaksi.")
    elif uang_pelanggan >= total and total != 0:
        kembalian = uang_pelanggan - total
        print(f"""
Uang Pelanggan          : {uang_pelanggan}
Total Belanja           : {total}
Uang Kembalian          : {kembalian}
Terima Kasih Sudah berbelanja, barang sudah dihapus dari keranjang
""")
        total = 0
        keranjang.clear()


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
                print("\n---------- DAFTAR PESANAN ----------")
                for i in range(len(keranjang)):
                    print(f"""
Pesanan             : {i+1}
Nama Barang         : {keranjang[i]['nama_barang'].capitalize()} x{keranjang[i]['jumlah']} Pcs
Harga Satuan        : Rp{int(keranjang[i]['harga'])}""")
                print(f"\nTotal Bayar         : RP{total}")
                bayar()
                break
    elif opsi == "5":
        bayar()
    else:
        print("rawr")