from datetime import datetime, timedelta

class Perpustakaan:
    def __init__(self):
        self.data_peminjaman = [] #array kosong untuk simpan data peminjam.

    def tambah_peminjaman(self, kode, nama, judul):
        tgl_pinjam = datetime.now().strftime('%Y-%m-%d') #ubah jadi string dengan format YYYY-MM-DD.
        tgl_maks_kembali = (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')
        self.data_peminjaman.append({
            'kode': kode,
            'nama': nama,
            'judul': judul,
            'tgl_pinjam': tgl_pinjam,
            'tgl_kembali': tgl_maks_kembali
        }) #append pada array data_peminjam yang berisi kode, nama, judul, tgl_pinjam, dan tgl_kembali.

    def WaktuPinjam(self, x):
        tglKembali = datetime.strptime(x, '%Y-%m-%d')
        tglPinjam = datetime.now()
        selisih = (tglKembali - tglPinjam).days
        return selisih