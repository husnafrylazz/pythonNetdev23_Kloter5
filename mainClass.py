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
        day = random.randint(1, 30)  # tanggal 1-30
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
