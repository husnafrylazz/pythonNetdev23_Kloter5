from datetime import datetime, timedelta
import random

class Perpustakaan:
    def __init__(self):
        self.data_peminjaman = []
        self.tgl_maks_kembali = None

    @staticmethod
    def tanggal_pinjam_acak():
        skrg = datetime.now()
        year = skrg.year
        month = skrg.month
        day = random.randint(1, 14)
        tanggal_acak = datetime(year, month, day)
        return tanggal_acak.date()

    def tambah_peminjaman(self, kode, nama, judul):
        tgl_pinjam = self.tanggal_pinjam_acak()
        self.tgl_maks_kembali = tgl_pinjam + timedelta(days=7)
        self.data_peminjaman.append({
            'kode': kode,
            'nama': nama,
            'judul': judul,
            'tgl_pinjam': tgl_pinjam,
            'tgl_kembali': self.tgl_maks_kembali
        })

    def cari_peminjaman(self, kode):
        for peminjaman in self.data_peminjaman:
            if peminjaman['kode'] == kode:
                return peminjaman

    def WaktuPinjam(self, x):
        selisih = (x - self.tgl_maks_kembali).days
        return selisih


def main():
    perpustakaan = Perpustakaan()

    print("===== Masukkan Data Peminjam =====")
    while True:
        kode = input("Masukkan Kode Member\t: ")
        nama = input("Masukkan Nama Member\t: ")
        judul = input("Masukkan Judul Buku\t\t: ")

        perpustakaan.tambah_peminjaman(kode, nama, judul)

        ulangi = input("Ulangi lagi (y/n): ")
        if ulangi.lower() != 'y':
            break

    print("\nData Peminjam: ")
    for peminjaman in perpustakaan.data_peminjaman:
        print(f"{peminjaman['kode']}|{peminjaman['nama']}|{peminjaman['judul']}|{peminjaman['tgl_pinjam']}|{peminjaman['tgl_kembali']}")

    print("\n===== Cari Data Peminjam =====")
    cari_kode = input("Masukkan Kode Member\t: ")
    print(cari_kode)
    peminjaman_ditemukan = perpustakaan.cari_peminjaman(cari_kode)

    if peminjaman_ditemukan:
        print("\n===== Data Peminjaman Buku =====")
        print("Kode Member\t\t\t\t: " + str(peminjaman_ditemukan['kode']))
        print("Nama Member\t\t\t\t: " + str(peminjaman_ditemukan['nama']))
        print("Judul Buku\t\t\t\t: " + str(peminjaman_ditemukan['judul']))
        print("Tanggal Mulai Peminjaman: " + str(peminjaman_ditemukan['tgl_pinjam']))
        print("Tanggal Maks Peminjaman\t: " + str(peminjaman_ditemukan['tgl_kembali']))

        selisih = datetime.today().date()
        terlambat = perpustakaan.WaktuPinjam(selisih)
        denda = terlambat * 2000
        print("Tanggal Pengembalian\t: " + str(selisih))
        print("Terlambat\t\t\t\t: " + str(terlambat) + " hari")
        print("Denda\t\t\t\t\t: Rp " + str(denda))
    else:
        print("Data peminjaman tidak ditemukan.")

main()
