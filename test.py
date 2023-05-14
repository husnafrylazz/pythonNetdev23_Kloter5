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

    def tampilkan_pinjaman(self, kode):
        for pinjaman in self.pinjaman:
            if pinjaman.member.kode == kode:
                print("Kode Member\t\t:", pinjaman.member.kode)
                print("Nama Member\t\t:", pinjaman.member.nama)
                print("Judul Buku\t\t:", pinjaman.judul)
                return

        print("\nData peminjaman tidak ditemukan.")


perpustakaan = Perpustakaan()

ulangi = "y"
while ulangi.lower() == "y":
    kode = input("\nMasukkan Kode Member: ")
    nama = input("Masukkan Nama Member: ")
    judul = input("Masukkan Judul Buku: ")

    perpustakaan.tambah_pinjaman(kode, nama, judul)
    perpustakaan.tampilkan_pinjaman(kode)
    ulangi = input("Ulangi lagi (y/n): ")
    print("Ulangi lagi (y/n)\t: ", ulangi)

kode_member = input("\nMasukkan Kode Member: ")
print("\n\nMasukkan Kode Member\t: ", kode_member)
perpustakaan.tampilkan_pinjaman(kode_member)
