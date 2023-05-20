from datetime import datetime, timedelta

class Perpustakaan:
    def __init__(self):
        self.data_peminjaman = [] #array kosong untuk simpan data peminjam.

    def tambah_peminjaman(self, kode, nama, judul):
        tgl_pinjam = datetime.today().date() #tanggal hari peminjaman
        tgl_maks_kembali = (datetime.today().date + timedelta(days=7))
        self.data_peminjaman.append({
            'kode': kode,
            'nama': nama,
            'judul': judul,
            'tgl_pinjam': tgl_pinjam,
            'tgl_kembali': tgl_maks_kembali
        }) #append pada array data_peminjam yang berisi kode, nama, judul, tgl_pinjam, dan tgl_kembali.
        
    def cari_peminjaman(self, kode):
        for peminjaman in self.data_peminjaman:
            if peminjaman['kode'] == kode:
                return peminjaman
    
    def WaktuPinjam(self, x):
        tglKembali = datetime.strptime(x, '%Y-%m-%d')
        tglPinjam = datetime.today().date() + timedelta(days=7)
        selisih = (tglKembali.date() - tglPinjam).days
        return selisih
