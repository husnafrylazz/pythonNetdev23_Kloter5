from datetime import datetime  # import modul datetime

class mainPerpus:
    def __init__(self, kode, nama, judul_buku, tgl_pinjam): #definisikan atribut dan parameter
        self.kode = kode
        self.nama = nama
        self.judul_buku = judul_buku
        self.tgl_pinjam = tgl_pinjam
        self.tgl_kembali = self.tgl_pinjam + timedelta(days=7) #timedelta agar dapat menambahkan hari ke depan

    def WaktuPinjam(self, x):
        tgl_kembali = datetime.strptime(x, '%y-%m-%d')  # konversi string ke format YYYY-MM-DD
        tgl_pinjam = datetime.today().date()  # untuk current date tanpa jam, menit, detik
        selisih = (tgl_kembali.date() - tgl_pinjam).days  # selisih dengan atribut .days agar jdi bil.bulat
        return selisih

