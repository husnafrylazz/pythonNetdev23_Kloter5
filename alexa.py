from datetime import datetime, timedelta

class WaktuPinjam:
    def __init__(self, tanggal_pinjam):
        self.tanggal_pinjam = datetime.strptime(tanggal_pinjam, '%Y-%m-%d').date()

    def hitung_selisih_hari(self):
        tanggal_hari_ini = datetime.now().date()
        selisih_hari = (tanggal_hari_ini - self.tanggal_pinjam).days
        return selisih_hari

def cari_data_peminjaman(kode_member, data_peminjaman):
    for peminjaman in data_peminjaman:
        data = peminjaman.split('|')
        if data[0] == kode_member:
            return {
                'Kode Member': data[0],
                'Nama Member': data[1],
                'Judul Buku': data[2],
                'Tanggal Mulai Peminjaman': data[3],
                'Tanggal Maks Peminjaman': data[4],
                'Tanggal Pengembalian': datetime.now().date().strftime("%Y-%m-%d"),
                'Terlambat': max(0, WaktuPinjam(data[4]).hitung_selisih_hari() - 7),
                'Denda': max(0, (WaktuPinjam(data[4]).hitung_selisih_hari() - 7) * 2000)
            }
    return None

def main():
    data_peminjaman = []
    while True:
        kode_member = input("Masukkan Kode Member: ")
        nama_member = input("Masukkan Nama Member: ")
        judul_buku = input("Masukkan Judul Buku: ")
        tanggal_peminjaman = datetime.now().date().strftime("%Y-%m-%d")
        tanggal_pengembalian = (datetime.now() + timedelta(days=7)).date().strftime("%Y-%m-%d")

        data_peminjaman.append(f"{kode_member}|{nama_member}|{judul_buku}|{tanggal_peminjaman}|{tanggal_pengembalian}")

        ulangi = input("Ulangi lagi (y/n): ")
        if ulangi.lower() != 'y':
            break

    print("\nOutput:")

    for peminjaman in data_peminjaman:
        print(peminjaman)

    kode_member_cari = input("\nMasukkan Kode Member: ")
    data_peminjaman_cari = cari_data_peminjaman(kode_member_cari, data_peminjaman)

    if data_peminjaman_cari is not None:
        print("\nData Peminjaman Buku")
        print(f"Kode Member: {data_peminjaman_cari['Kode Member']}")
        print(f"Nama Member: {data_peminjaman_cari['Nama Member']}")
        print(f"Judul Buku: {data_peminjaman_cari['Judul Buku']}")
        print(f"Tanggal Mulai Peminjaman: {data_peminjaman_cari['Tanggal Mulai Peminjaman']}")
        print(f"Tanggal Maks Peminjaman: {data_peminjaman_cari['Tanggal Maks Peminjaman']}")
        print(f"Tanggal Pengembalian: {data_peminjaman_cari['Tanggal Pengembalian']}")
        print(f"Terlambat: {data_peminjaman_cari['Terlambat']} hari")
        print(f"Denda: Rp{data_peminjaman_cari['Denda']}")
        print("Keterangan:")
        print("• Tanggal Pengembalian diambil dari tanggal ketika running program.")
        print("• Denda keterlambatan diasumsikan Rp 2.000/hari")
    else:
        print("Data peminjaman buku tidak ditemukan.")

if __name__ == '__main__':
    main()

