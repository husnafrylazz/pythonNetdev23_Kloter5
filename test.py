class Buku:
    def __init__(self, judul):
        self.judul = judul

    def __str__(self):
        return self.judul


data_buku = []

jumlah_data = int(input("Masukkan Jumlah Data: "))

for _ in range(jumlah_data):
    nama = input("Masukkan Nama Peminjam: ")
    judul = input("Masukkan Judul Buku: ")
    buku = Buku(judul)
    data_buku.append((nama, buku))

print("Data Buku:")
for nama, buku in data_buku:
    print("Nama Peminjam:", nama)
    print("Judul Buku:", buku)
    print()
