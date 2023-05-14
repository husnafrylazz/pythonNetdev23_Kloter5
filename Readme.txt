Requirement Minimum
1. Menggunakan konsep OOP
2. Susun sebuah fungsi bernama WaktuPinjam(x) yang berfungsi untuk menghitung
selisih hari antara tanggal hari ini dan tanggal x (dalam format string
'YYYY-MM-DD'). Fungsi ini akan menghasilkan nilai bulat yang menunjukkan
selisih antara tanggal x dan tanggal hari ini.
Contoh:
Misalkan tanggal hari ini adalah tanggal ‘2023-04-10’, maka jika function dipanggil
dengan WaktuPinjam(‘2023-04-15’) akan mengembalikan nilai 5.
3. Dibutuhkan sebuah program Python untuk menyimpan informasi peminjaman buku di
sebuah perpustakaan. Informasi yang perlu disimpan meliputi kode anggota, nama
anggota, judul buku, tanggal peminjaman, dan tanggal maksimum pengembalian
(yaitu 7 hari setelah tanggal peminjaman). Berikut ini adalah tampilan program yang
diharapkan:
Masukkan Kode Member : A01
Masukkan Nama Member : Husna
Masukkan Judul Buku : Pemrograman Python
Ulangi lagi (y/n) : y
Masukkan Kode Member : A02
Masukkan Nama Member : Ramiza
Masukkan Judul Buku : Pemrograman Pascal
Ulangi lagi (y/n) : y
Masukkan Kode Member : A03
Masukkan Nama Member : Alesandora
Masukkan Judul Buku : Pemrograman C++
Ulangi lagi (y/n) : n
Outputnya seperti berikut:
A01|Husna|Pemrograman Python|2023-05-01|2023-05-06
A02|Ramiza|Pemrograman Pascal|2023-05-02|2023-05-08
A03|Alesandora|Pemrograman C++|2023-05-10|2023-05-12
4. Berdasarkan output data yang diperoleh dari program nomor 3, buatlah program
Python untuk mencari data peminjaman buku berdasarkan kode membernya. Berikut
ini output program ketika dijalankan:
Masukkan Kode Member : A02
Data Peminjaman Buku
Kode Member : A02
Nama Member : Ramiza
Judul Buku : Pemrograman Pascal
Tanggal Mulai Peminjaman : 2023-05-02
Tanggal Maks Peminjaman : 2023-05-09
Tanggal Pengembalian : 2023-05-12
Terlambat : 3 hari
Denda : Rp6.000
Keterangan:
● Tanggal Pengembalian diambil dari tanggal ketika running program.
● Denda keterlambatan diasumsikan Rp 2.000/hari
● Untuk menghitung selisih tanggal bisa menggunakan function
WaktuPinjam(x) yang sudah dibuat dari soal nomor 2.
