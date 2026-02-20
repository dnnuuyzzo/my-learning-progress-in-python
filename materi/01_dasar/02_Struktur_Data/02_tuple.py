"""
===============================================
TUPLE DI PYTHON
===============================================

Tuple adalah struktur data yang:
- Menyimpan koleksi item secara terurut
- TIDAK BISA diubah (immutable)
- Bisa menyimpan tipe data berbeda
- Mengizinkan duplikat
"""

# =====================================
# 1. MEMBUAT TUPLE
# =====================================

tuple_kosong = ()
angka = (1, 2, 3, 4, 5)
buah = ("apel", "jeruk", "mangga")

# PENTING: Tuple satu elemen harus ada koma
satu_elemen = (5,)  # Ini tuple
bukan_tuple = (5)   # Ini integer

print(f"type(satu_elemen): {type(satu_elemen)}")
print(f"type(bukan_tuple): {type(bukan_tuple)}")

# Tuple packing (tanpa kurung)
koordinat = 10, 20, 30
print(f"koordinat: {koordinat}")

# =====================================
# 2. MENGAKSES DAN SLICING
# =====================================

buah = ("apel", "jeruk", "mangga", "pisang")
print(f"buah[0]: {buah[0]}")
print(f"buah[-1]: {buah[-1]}")
print(f"buah[1:3]: {buah[1:3]}")

# =====================================
# 3. TUPLE UNPACKING
# =====================================

koordinat = (10, 20, 30)
x, y, z = koordinat
print(f"x={x}, y={y}, z={z}")

# Swap nilai
a, b = 5, 10
a, b = b, a
print(f"Setelah swap: a={a}, b={b}")

# Extended unpacking
angka = (1, 2, 3, 4, 5)
pertama, *tengah, terakhir = angka
print(f"pertama={pertama}, tengah={tengah}, terakhir={terakhir}")

# =====================================
# 4. TUPLE METHODS
# =====================================

angka = (1, 2, 3, 2, 4, 2)
print(f"count(2): {angka.count(2)}")
print(f"index(3): {angka.index(3)}")

# =====================================
# 5. TUPLE SEBAGAI KEY DICTIONARY
# =====================================

lokasi = {
    (0, 0): "origin",
    (10, 20): "point A"
}
print(f"lokasi[(10, 20)]: {lokasi[(10, 20)]}")

# =============================================================================
# LATIHAN TUPLE - 20 SOAL (4 TINGKAT KESULITAN)
# =============================================================================

"""
================================================================================
                        DAFTAR SOAL LATIHAN TUPLE
================================================================================

🟢 BASIC (1-5) - Dasar-dasar Tuple
   1. Buat tuple berisi 5 nama kota, print elemen pertama dan terakhir
   2. Buat tuple satu elemen dengan benar (ingat: perlu koma!)
   3. Akses elemen ke-3 dari tuple ("a","b","c","d","e")
   4. Cari panjang tuple (1,2,3,4,5,6,7,8,9,10)
   5. Cek apakah "Python" ada dalam tuple ("Java","Python","C++")

🟡 INTERMEDIATE (6-10) - Slicing & Unpacking
   6. Ambil 3 elemen pertama dari (10,20,30,40,50) menggunakan slicing
   7. Balikkan tuple (1,2,3,4,5) menggunakan slicing
   8. Unpack tuple koordinat = (10, 20, 30) ke variabel x, y, z
   9. Swap nilai a=5 dan b=10 menggunakan tuple unpacking
   10. Gunakan extended unpacking: first, *middle, last = (1,2,3,4,5)

🟠 ADVANCED (11-15) - Tuple Methods & Konversi
   11. Hitung berapa kali angka 3 muncul di (1,2,3,3,3,4,5)
   12. Cari index pertama dari "jeruk" di ("apel","jeruk","mangga")
   13. Konversi list [1,2,3] menjadi tuple, lalu kembali ke list
   14. Gabungkan dua tuple (1,2,3) dan (4,5,6) menjadi satu
   15. Buat tuple berulang: ("Hi",) * 5

🔴 EXPERT (16-20) - Tantangan Tuple
   16. Gunakan tuple sebagai key dictionary: {(x,y): "value"}
   17. Buat fungsi yang return multiple values sebagai tuple
   18. Sort list of tuples [(3,"c"),(1,"a"),(2,"b")] berdasarkan elemen pertama
   19. Nested tuple: akses angka 6 dari ((1,2,3),(4,5,6),(7,8,9))
   20. Bandingkan memory usage antara list dan tuple dengan sys.getsizeof()

================================================================================
"""

print("\n" + "=" * 60)
print("LATIHAN TUPLE - Kerjakan di bawah ini!")
print("=" * 60)

# =============================================================================
# 🟢 BASIC (LEVEL 1-5)
# =============================================================================

# --- Soal 1 ---
print("\n📝 Soal 1: Buat tuple 5 nama kota")
# Tulis jawabanmu di bawah:
nama_kota = ("Jakarta", "Bandung", "Surabaya", "Yogyakarta", "Medan")
print(nama_kota[0])
print(nama_kota[-1])

# --- Soal 2 ---
print("\n📝 Soal 2: Buat tuple satu elemen dengan benar")
# Tulis jawabanmu di bawah:
nama_kota = ("Jakarta",)

# --- Soal 3 ---
print("\n📝 Soal 3: Akses elemen ke-3 dari tuple")
# Tulis jawabanmu di bawah:
huruf = ("a", "b", "c", "d", "e")
elemen_ketiga = huruf[2]

# --- Soal 4 ---
print("\n📝 Soal 4: Cari panjang tuple")
# Tulis jawabanmu di bawah:
angka = (1,2,3,4,5,6,7,8,9,10)
panjang_angka = len(angka)

# --- Soal 5 ---
print("\n📝 Soal 5: Cek membership dengan 'in'")
# Tulis jawabanmu di bawah:
bahasa_pemrograman = ("Java","Python","C++")
cek = "Python" in bahasa_pemrograman

# =============================================================================
# 🟡 INTERMEDIATE (LEVEL 6-10)
# =============================================================================

# --- Soal 6 ---
print("\n📝 Soal 6: Slicing 3 elemen pertama")
# Tulis jawabanmu di bawah:
angka = (10,20,30,40,50)
tiga_angka_pertama = angka[:2]

# --- Soal 7 ---
print("\n📝 Soal 7: Balikkan tuple dengan slicing")
# Tulis jawabanmu di bawah:
angka = (1,2,3,4,5)
angka = angka[::-1]

# --- Soal 8 ---
print("\n📝 Soal 8: Unpack koordinat ke x, y, z")
# Tulis jawabanmu di bawah:
koordinat = (10, 20, 30)
x, y, z = koordinat

# --- Soal 9 ---
print("\n📝 Soal 9: Swap a=5 dan b=10")
# Tulis jawabanmu di bawah:
a, b = 5, 10
b, a = 10, 5

# --- Soal 10 ---
print("\n📝 Soal 10: Extended unpacking")
# Tulis jawabanmu di bawah:
angka = (1,2,3,4,5)
first, *middle, last = angka

# =============================================================================
# 🟠 ADVANCED (LEVEL 11-15)
# =============================================================================

# --- Soal 11 ---
print("\n📝 Soal 11: Hitung kemunculan angka 3")
# Tulis jawabanmu di bawah:
angka = (1,2,3,3,3,4,5)
jumlah_angka_3 = angka.count(3)

# --- Soal 12 ---
print("\n📝 Soal 12: Cari index 'jeruk'")
# Tulis jawabanmu di bawah:
buah = ("apel","jeruk","mangga")
jeruk = buah.index("jeruk")

# --- Soal 13 ---
print("\n📝 Soal 13: Konversi list <-> tuple")
# Tulis jawabanmu di bawah:
angka_list = [1,2,3]
angka_tuple = tuple(angka_list)
angka_list = list(angka_tuple)

# --- Soal 14 ---
print("\n📝 Soal 14: Gabung dua tuple")
# Tulis jawabanmu di bawah:
tuple_1 = (1,2,3)
tuple_2 = (4,5,6)
tuple_gabungan = tuple_1 + tuple_2

# --- Soal 15 ---
print("\n📝 Soal 15: Tuple berulang")
# Tulis jawabanmu di bawah:
tuple_berulang = ("Hi",) * 5

# =============================================================================
# 🔴 EXPERT (LEVEL 16-20)
# =============================================================================

# --- Soal 16 ---
print("\n📝 Soal 16: Tuple sebagai key dictionary")
# Tulis jawabanmu di bawah:


# --- Soal 17 ---
print("\n📝 Soal 17: Fungsi return multiple values")
# Tulis jawabanmu di bawah:


# --- Soal 18 ---
print("\n📝 Soal 18: Sort list of tuples")
# Tulis jawabanmu di bawah:


# --- Soal 19 ---
print("\n📝 Soal 19: Akses nested tuple")
# Tulis jawabanmu di bawah:


# --- Soal 20 ---
print("\n📝 Soal 20: Bandingkan memory list vs tuple")
# import sys
# Tulis jawabanmu di bawah:


print("\n" + "=" * 60)
print("Selesaikan semua soal di atas! 💪")
print("=" * 60)

