from datetime import datetime #import modul datetime

def WaktuPinjam(x): 
    tgl_kembali = datetime.strptime(x, '%Y-%m-%d') #konversi string ke format YYYY-MM-DD

    tgl_pinjam = datetime.today().date() #untuk current date

    selisih = (tgl_kembali.date() - tgl_pinjam).days

    return selisih

tgl_pinjam = datetime.today().date().strftime('%Y-%m-%d') #kebalikan strptime, konversi format datetime YYYY-MM-DD ke string
tgl_kembali = input("Tanggal pengembalian (YYYY-MM-DD): ")
selisih = WaktuPinjam(tgl_kembali)

print("Tanggal peminjaman: " + tgl_pinjam)
print("Selisih hari: " + str(selisih))
