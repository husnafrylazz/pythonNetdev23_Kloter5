class Member:
    def __init__(self, kode, nama):
        self.kode = kode
        self.nama = nama


class Pinjaman:
    def __init__(self, member, judul):
        self.member = member
        self.judul = judul


class Perpustakaan:
    def __init__(self):
        self.pinjaman = []

    def tambah_pinjaman(self, kode, nama, judul):
        member = Member(kode, nama)
        pinjaman = Pinjaman(member, judul)
        self.pinjaman.append(pinjaman)
        print("Pinjaman berhasil ditambahkan.")

    def tampilkan_pinjaman(self):
        print("Output Data Pinjaman:")
        for i, pinjaman in enumerate(self.pinjaman, start=1):
            print("", pinjaman.member.kode,"|",pinjaman.member.nama,"|",pinjaman.judul)
            print()

perpustakaan = Perpustakaan()

ulangi = "y"
while ulangi.lower() == "y":
    kode = input("Masukkan Kode Member: ")
    nama = input("Masukkan Nama Member: ")
    judul = input("Masukkan Judul Buku: ")

    perpustakaan.tambah_pinjaman(kode, nama, judul)

    ulangi = input("Ulangi lagi (y/n): ")

perpustakaan.tampilkan_pinjaman()
