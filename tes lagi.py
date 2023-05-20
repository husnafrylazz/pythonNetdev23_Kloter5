from datetime import datetime, timedelta
import random

class Perpustakaan:
    def __init__(self):
        self.data_peminjaman = []

    @staticmethod
    def tanggal_pinjam_acak():
        skrg = datetime.now()
        year = skrg.year
        month = skrg.month
        day = random.randint(1, 20)  # tanggal 1-20
        tanggal_acak = datetime(year, month, day)
        return tanggal_acak.date()

    def tambah_peminjaman(self, kode, nama, judul):
        tgl_pinjam = self.tanggal_pinjam_acak()
        tgl_maks_kembali = tgl_pinjam + timedelta(days=7)
        self.data_peminjaman.append({
            'kode': kode,
            'nama': nama,
            'judul': judul,
            'tgl_pinjam': tgl_pinjam,
            'tgl_kembali': tgl_maks_kembali
        })

    def cari_peminjaman(self, kode):
        for peminjaman in self.data_peminjaman:
            if peminjaman['kode'] == kode:
                return peminjaman

    @staticmethod
    def WaktuPinjam(tglPinjam):
        tglKembali = datetime.today().date()
        selisih = (tglKembali - tglPinjam).days
        return selisih


def main():
    perpustakaan = Perpustakaan()

    print("===== Masukkan Data Peminjam =====")
    while True:
        kode = input("Masukkan Kode Member: ")
        nama = input("Masukkan Nama Member: ")
        judul = input("Masukkan Judul Buku: ")

        perpustakaan.tambah_peminjaman(kode, nama, judul)

        ulangi = input("Ulangi lagi (y/n): ")
        if ulangi.lower() != 'y':
            break

    print("\nData Peminjam: ")
    for peminjaman in perpustakaan.data_peminjaman:
        print(f"{peminjaman['kode']}|{peminjaman['nama']}|{peminjaman['judul']}|{peminjaman['tgl_pinjam']}|{peminjaman['tgl_kembali']}")

    print("\n===== Cari Data Peminjam =====")
    cari_kode = input("Masukkan Kode Member: ")
    peminjaman_ditemukan = perpustakaan.cari_peminjaman(cari_kode)

    if peminjaman_ditemukan:
        print("\nData Peminjaman Buku:")
        print("Kode Member: " + str(peminjaman_ditemukan['kode']))
        print("Nama Member: " + str(peminjaman_ditemukan['nama']))
        print("Judul Buku: " + str(peminjaman_ditemukan['judul']))
        print("Tanggal Mulai Peminjaman: " + str(peminjaman_ditemukan['tgl_pinjam']))
        print("Tanggal Maks Peminjaman: " + str(peminjaman_ditemukan['tgl_kembali']))

        terlambat = Perpustakaan.WaktuPinjam(peminjaman_ditemukan['tgl_pinjam'])
        denda = terlambat * 2000
        print("Terlambat: " + str(terlambat) + " hari")
        print("Denda: Rp " + str(denda))
    else:
        print("Data peminjaman tidak ditemukan.")

# Panggil fungsi main()
main()
