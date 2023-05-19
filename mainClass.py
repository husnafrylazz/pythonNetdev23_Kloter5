class pinjamBuku:
    def __init__(self, kode, nama, judul_buku, tgl_pinjam): #definisikan atribut dan parameter
        self.kode = kode
        self.nama = nama
        self.judul_buku = judul_buku
        self.tgl_pinjam = tgl_pinjam
        self.tgl_kembali = self.tgl_pinjam + timedelta(days=7) #timedelta agar dapat menambahkan hari ke depan


