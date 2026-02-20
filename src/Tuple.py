# =============================================================================
# LATIHAN PYTHON: TUPLE
# =============================================================================
# Petunjuk: Kerjakan soal-soal di bawah ini untuk menguji pemahaman Anda
# tentang Tuple di Python.
# =============================================================================

# -----------------------------------------------------------------------------
# LEVEL: MUDAH (5 SOAL)
# -----------------------------------------------------------------------------

# 1. Buatlah sebuah tuple kosong bernama 'my_tuple'.
#    Tampilkan tipe datanya untuk memastikan itu adalah tuple.
my_tuple = (0,)
print(type(my_tuple))

# 2. Diberikan tuple: buah = ("apel", "mangga", "jeruk", "pisang")
#    Cetaklah elemen kedua dari tuple tersebut.
buah = ("apel", "mangga", "jeruk", "pisang")
print(buah[1])

# 3. Apa yang terjadi jika Anda mencoba menjalankan kode ini? Jelaskan alasannya.
#    angka = (1, 2, 3)
#    angka[0] = 10


# 4. Gunakan fungsi bawaan Python untuk menghitung ada berapa banyak elemen
#    di dalam tuple berikut: warna = ("merah", "hijau", "biru", "kuning", "putih")
warna = ("merah", "hijau", "biru", "kuning", "putih")
Soal_4 = len(warna)

# 5. Diberikan tuple: nilai = (10, 20, 30, 20, 40, 20)
#    Hitunglah berapa kali angka 20 muncul dalam tuple tersebut menggunakan method .count()
nilai = (10, 20, 30, 20, 40, 20)
Soal_5 = nilai.count(20)

# -----------------------------------------------------------------------------
# LEVEL: MENENGAH (5 SOAL)
# -----------------------------------------------------------------------------

# 6. Unpacking: Diberikan tuple koordinat = (100, 200, 300)
#    Pecahlah (unpack) isi tuple tersebut ke dalam tiga variabel: x, y, dan z.
#    Lalu cetak masing-masing variabel tersebut.
koordinat = (100, 200, 300)
x, y, z = koordinat

# 7. Gabungkan dua tuple berikut menjadi satu tuple baru bernama 'gabungan':
t1 = (1, 2, 3)
t2 = ("a", "b", "c")
gabungan = t1 + t2

# 8. Slicing: Diberikan tuple data = (10, 20, 30, 40, 50, 60, 70)
#    Ambil elemen dari indeks 2 sampai indeks 5 (elemen 50 termasuk).
data = (10, 20, 30, 40, 50, 60, 70)
slice = data[2:5]

# 9. Konversi: Ubahlah list berikut menjadi tuple:
#    list_data = [1, "Python", True, 3.14]
#    Simpan hasilnya dalam variabel 'tuple_data'.
list_data = [1, "Python", True, 3.14]
tuple_data = tuple(list_data)

# 10. Membership: Periksalah apakah string "Admin" ada di dalam tuple berikut:
#     users = ("User1", "User2", "Moderator", "Editor")
#     Tampilkan pesan "Ditemukan" jika ada, dan "Tidak Ditemukan" jika tidak ada.
users = ("User1", "User2", "Moderator", "Editor")
if "Admin" in users:
    print("Ditemukan")
else:
    print("Tidak ditemukan")

# -----------------------------------------------------------------------------
# LEVEL: SULIT (5 SOAL)
# -----------------------------------------------------------------------------

# 11. Nested Tuple: Diberikan tuple berikut:
#     data_siswa = ("Budi", (80, 85, 90), "Jakarta")
#     Bagaimana cara mengambil nilai 85 dari tuple tersebut?
data_siswa = ("Budi", (80, 85, 90), "Jakarta")
slicing_data = data_siswa[1][1]

# 12. Immutability Experiment: Diberikan tuple yang berisi list:
#     keranjang = (["Apel", "Mangga"], "Plastik")
#     Cobalah untuk menambahkan "Jeruk" ke dalam list yang ada di dalam tuple tersebut.
#     Apakah ini berhasil? Mengapa? (Tuliskan kodenya dan penjelasannya).
keranjang = (["Apel", "Mangga"], "Plastik")
keranjang[0].append("Jeruk")

# 13. Extended Unpacking: Diberikan tuple angka_banyak = (1, 2, 3, 4, 5, 6, 7, 8)
#     Ambil angka pertama ke variabel 'awal', angka terakhir ke variabel 'akhir',
#     dan sisa angka di tengahnya ke dalam satu list bernama 'tengah' menggunakan operator *.
angka_banyak = (1, 2, 3, 4, 5, 6, 7, 8)
awal, *tengah, akhir = angka_banyak

# 14. Sorting: Diberikan list berisi tuple yang merepresentasikan (nama, umur):
#     peserta = [("Andi", 25), ("Budi", 20), ("Caca", 22)]
#     Urutkan list tersebut berdasarkan UMUR (elemen kedua dari tuple) secara ascending.
peserta = [("Andi", 25), ("Budi", 20), ("Caca", 22)]
peserta = sorted(peserta, key= lambda x: x[1])

# 15. Tuple as Dictionary Key:
#     Mengapa tuple dapat digunakan sebagai key (kunci) dalam Dictionary, sedangkan list tidak bisa?
#     Berikan contoh kode sederhana pembuatan Dictionary dengan tuple sebagai key-nya.