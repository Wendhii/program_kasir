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
data_admin = [
    {
        "nama": "Muhammad Wendy",
        "status": "Pegawai"
    },
    {
        "nama": "Shabilla",
        "status": "Pegawai"
    },
    {
        "nama": "Tantri",
        "status": "Pegawai"
    }
    
]
nama_kasir = "Belum Login"
keranjang = []
total = 0
opsi = ["Login","Tambah Barang", "Tampilkan Semua Barang", "Cari Kategori", "beli Barang", "Pembayaran", "Keluar Program"]

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

def admin(nama_admin):
    global nama_kasir
    status = False
    for i in data_admin:
        if nama_admin.lower() in i['nama'].lower():
            nama_kasir = nama_admin
            print(f"Login Berhasil\nAnda memiliki akses ke Opsi 2.")
            status = True
    if not status:
        print("Login Gagal. Anda tidak punya akses ke Opsi 2.")
    return

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

def fungsi_diskon():
    total_akhir = total
    nilai_diskon = 0
    pajak = 0.11
    # kondisi apabila total belanja lebih dari 100.000
    if total_akhir > 100000:
        nilai_diskon = 0.1
    # kondsi apabila total belanja lebih dari 50.000
    elif total_akhir > 50000:
        nilai_diskon = 0.05
    total_diskon = total_akhir * nilai_diskon
    total_akhir -= total_diskon
    total_pajak = total_akhir * pajak
    total_akhir = total_akhir + total_pajak
    return total_akhir, nilai_diskon, total_diskon, pajak, total_pajak
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
    total_bayar, diskon, total_diskon, pajak, total_pajak= fungsi_diskon()
    uang_pelanggan = int(input("Masukan uang pelanggan: "))
    if uang_pelanggan < total_bayar:
        print("Maaf, Uang tidak cukup untuk melakukan transaksi.")
    elif uang_pelanggan >= total_bayar:
        kembalian = uang_pelanggan - total_bayar
        struk(total_bayar, uang_pelanggan, kembalian, diskon, total_diskon, pajak, total_pajak)
        total = 0
        keranjang.clear()
    return

def struk (total_bayar, uang_pelanggan, kembalian, diskon, total_diskon, pajak, total_pajak):
    print(f"""
========================================
               KING STORE
========================================
Kasir   : {nama_kasir}
----------------------------------------""")
    for i in keranjang:
        nama_dan_jumlah = f"{i['nama_barang']} x{i['jumlah']} Pcs"
        harga_satuan = f"{i['harga']}"
        print(f"{nama_dan_jumlah:<23} : {harga_satuan:>10}")
    print(f"""----------------------------------------
{'Diskon':<23} : {int(diskon * 100):>10}%
{'Total Diskon':<23} : {total_diskon:>10}
{'Pajak':<23} : {int(pajak * 100):>10}%
{'Total Pajak':<23} : {total_pajak:>10}""")
    print(f"""----------------------------------------
{'Total Belanja':<23} : {f"RP.{total_bayar}":>10}
{'Uang Pelanggan':<23} : {f"RP.{uang_pelanggan}":>10}
{'Kembalian':<23} : {f"RP.{kembalian}":>10}
========================================
       TERIMA KASIH SUDAH BELANJA""")

print(f"""========================================
       Selamat Datang Di Toko Kami
========================================""")            
for i in range(len(opsi)):
    print(f"{i+1}. {opsi[i]}")
while True:
    print("========================================")
    opsi = input("Pilih Opsi: ")
    print("========================================")
    if opsi == "1":
        admin_login = input("Nama Kasir: ")
        admin(admin_login)
    elif opsi == "2":
        if nama_kasir == "Belum Login":
            print("Maaf, Hanya Kasir yang bisa menambahkan barang. Login Dulu")
        else:
            tambah_barang()
    elif opsi == "3":
        tampilkan()
    elif opsi == "4":
        kategori()
    elif opsi == "5":
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
    elif opsi == "6":
        bayar()
    elif opsi == "7":
        print("Keluar dari program")
        break
    else:
        print("rawr")