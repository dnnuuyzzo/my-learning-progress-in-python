"""
===============================================
VARIABEL DI PYTHON
===============================================

Variabel adalah tempat untuk menyimpan data.
Di Python, kita tidak perlu mendeklarasikan tipe data secara eksplisit.
"""

# =====================================
# 1. MEMBUAT VARIABEL
# =====================================

# Variabel dibuat saat pertama kali diberi nilai
nama = "Budi"
umur = 25
tinggi = 175.5
sudah_menikah = False

print("Nama:", nama)
print("Umur:", umur)
print("Tinggi:", tinggi)
print("Sudah Menikah:", sudah_menikah)

# =====================================
# 2. ATURAN PENAMAAN VARIABEL
# =====================================

"""
Aturan penamaan variabel:
1. Harus dimulai dengan huruf atau underscore (_)
2. Tidak boleh dimulai dengan angka
3. Hanya boleh mengandung huruf, angka, dan underscore
4. Case-sensitive (nama ≠ Nama ≠ NAMA)
5. Tidak boleh menggunakan kata kunci Python
"""

# Contoh yang BENAR:
nama_lengkap = "Budi Santoso"
_variabel_private = 100
namaDepan = "Budi"  # camelCase
nama_belakang = "Santoso"  # snake_case (direkomendasikan di Python)
KONSTANTA = 3.14  # Huruf kapital untuk konstanta
nama2 = "Dua"

# Contoh yang SALAH (jangan gunakan):
# 2nama = "Budi"  # Tidak boleh dimulai dengan angka
# nama-lengkap = "Budi"  # Tidak boleh menggunakan tanda hubung
# class = "Python"  # Tidak boleh menggunakan kata kunci

# =====================================
# 3. MULTIPLE ASSIGNMENT
# =====================================

# Memberikan nilai yang sama ke beberapa variabel
a = b = c = 100
print(f"a={a}, b={b}, c={c}")

# Memberikan nilai berbeda ke beberapa variabel sekaligus
x, y, z = 1, 2, 3
print(f"x={x}, y={y}, z={z}")

# Menukar nilai dua variabel
x, y = y, x
print(f"Setelah ditukar: x={x}, y={y}")

# =====================================
# 4. MEMERIKSA TIPE DATA
# =====================================

nama = "Python"
angka = 42
desimal = 3.14
boolean = True

print(type(nama))     # <class 'str'>
print(type(angka))    # <class 'int'>
print(type(desimal))  # <class 'float'>
print(type(boolean))  # <class 'bool'>

# =====================================
# 5. KONVERSI TIPE DATA (TYPE CASTING)
# =====================================

# String ke Integer
angka_str = "123"
angka_int = int(angka_str)
print(f"'{angka_str}' dikonversi menjadi {angka_int}")

# Integer ke String
angka = 456
angka_str = str(angka)
print(f"{angka} dikonversi menjadi '{angka_str}'")

# String ke Float
desimal_str = "3.14"
desimal_float = float(desimal_str)
print(f"'{desimal_str}' dikonversi menjadi {desimal_float}")

# Float ke Integer (membuang desimal)
desimal = 9.99
bulat = int(desimal)
print(f"{desimal} dikonversi menjadi {bulat}")

# =====================================
# 6. KONSTANTA
# =====================================

"""
Python tidak memiliki konstanta sejati.
Konvensi: gunakan HURUF_KAPITAL untuk menandakan konstanta.
"""

PI = 3.14159
MAX_SIZE = 100
DATABASE_NAME = "my_database"

# =====================================
# 7. VARIABEL GLOBAL VS LOKAL
# =====================================

variabel_global = "Saya global"

def fungsi_contoh():
    variabel_lokal = "Saya lokal"
    print(variabel_global)  # Bisa akses variabel global
    print(variabel_lokal)   # Bisa akses variabel lokal

fungsi_contoh()
print(variabel_global)  # Bisa akses variabel global
# print(variabel_lokal)  # ERROR: variabel lokal tidak bisa diakses di luar fungsi

# =============================================================================
# LATIHAN VARIABEL - 20 SOAL (4 TINGKAT KESULITAN)
# =============================================================================

"""
================================================================================
                        DAFTAR SOAL LATIHAN VARIABEL
================================================================================

🟢 BASIC (1-5) - Dasar-dasar Variabel
   1. Buat variabel 'nama' berisi nama lengkapmu, lalu print
   2. Buat variabel 'umur' berisi umurmu (integer), lalu print
   3. Buat variabel 'tinggi' berisi tinggi badanmu (float), lalu print
   4. Buat 3 variabel sekaligus: x=10, y=20, z=30 dalam satu baris
   5. Cek tipe data dari variabel: "Hello", 42, 3.14, True menggunakan type()

🟡 INTERMEDIATE (6-10) - Konversi & Operasi Variabel
   6. Konversi string "123" menjadi integer, lalu kalikan dengan 2
   7. Konversi integer 456 menjadi string, lalu gabungkan dengan " rupiah"
   8. Konversi float 9.99 menjadi integer (perhatikan hasilnya)
   9. Tukar nilai dua variabel a=5 dan b=10 tanpa variabel ketiga
   10. Buat variabel a=b=c=100, lalu ubah nilai c menjadi 200. Print semua.

🟠 ADVANCED (11-15) - Scope & Aturan Variabel
   11. Buat konstanta PI = 3.14159 dan GRAVITY = 9.8, hitung luas lingkaran r=7
   12. Buat fungsi yang mengakses variabel global dan lokal, print keduanya
   13. Identifikasi mana nama variabel yang VALID:
       a) nama_depan  b) 2nama  c) _private  d) nama-belakang  e) namaDepan
   14. Buat variabel dengan multiple assignment: first, *middle, last = [1,2,3,4,5]
   15. Gunakan global keyword untuk mengubah variabel global dari dalam fungsi

🔴 EXPERT (16-20) - Tantangan Variabel
   16. Buat program yang menerima input nama dan umur, hitung tahun lahir
   17. Konversi suhu: buat variabel celsius, hitung ke fahrenheit dan kelvin
   18. Buat variabel yang menyimpan hasil operasi: (10+5)*2 - 8/4 + 3**2
   19. Demonstrasikan perbedaan antara shallow copy dan referensi variabel pada list
   20. Buat program kalkulator sederhana dengan variabel: num1, num2, operator, result

================================================================================
"""

print("\n" + "=" * 60)
print("LATIHAN VARIABEL - Kerjakan di bawah ini!")
print("=" * 60)

# =============================================================================
# 🟢 BASIC (LEVEL 1-5)
# =============================================================================

# --- Soal 1 ---
print("\n📝 Soal 1: Buat variabel 'nama' berisi nama lengkapmu")
# Tulis jawabanmu di bawah:


# --- Soal 2 ---
print("\n📝 Soal 2: Buat variabel 'umur' berisi umurmu (integer)")
# Tulis jawabanmu di bawah:


# --- Soal 3 ---
print("\n📝 Soal 3: Buat variabel 'tinggi' berisi tinggi badanmu (float)")
# Tulis jawabanmu di bawah:


# --- Soal 4 ---
print("\n📝 Soal 4: Buat x=10, y=20, z=30 dalam satu baris")
# Tulis jawabanmu di bawah:


# --- Soal 5 ---
print("\n📝 Soal 5: Cek tipe data dari 'Hello', 42, 3.14, True")
# Tulis jawabanmu di bawah:


# =============================================================================
# 🟡 INTERMEDIATE (LEVEL 6-10)
# =============================================================================

# --- Soal 6 ---
print("\n📝 Soal 6: Konversi '123' ke integer, kalikan dengan 2")
# Tulis jawabanmu di bawah:


# --- Soal 7 ---
print("\n📝 Soal 7: Konversi 456 ke string, gabungkan dengan ' rupiah'")
# Tulis jawabanmu di bawah:


# --- Soal 8 ---
print("\n📝 Soal 8: Konversi 9.99 ke integer")
# Tulis jawabanmu di bawah:


# --- Soal 9 ---
print("\n📝 Soal 9: Tukar nilai a=5 dan b=10 tanpa variabel ketiga")
# Tulis jawabanmu di bawah:


# --- Soal 10 ---
print("\n📝 Soal 10: Buat a=b=c=100, ubah c=200, print semua")
# Tulis jawabanmu di bawah:


# =============================================================================
# 🟠 ADVANCED (LEVEL 11-15)
# =============================================================================

# --- Soal 11 ---
print("\n📝 Soal 11: Buat PI dan GRAVITY, hitung luas lingkaran r=7")
# Tulis jawabanmu di bawah:


# --- Soal 12 ---
print("\n📝 Soal 12: Buat fungsi dengan variabel global dan lokal")
# Tulis jawabanmu di bawah:


# --- Soal 13 ---
print("\n📝 Soal 13: Identifikasi nama variabel yang VALID (tulis dalam komentar)")
# a) nama_depan  b) 2nama  c) _private  d) nama-belakang  e) namaDepan
# Jawaban:


# --- Soal 14 ---
print("\n📝 Soal 14: Multiple assignment: first, *middle, last = [1,2,3,4,5]")
# Tulis jawabanmu di bawah:


# --- Soal 15 ---
print("\n📝 Soal 15: Gunakan global keyword untuk ubah variabel global")
# Tulis jawabanmu di bawah:


# =============================================================================
# 🔴 EXPERT (LEVEL 16-20)
# =============================================================================

# --- Soal 16 ---
print("\n📝 Soal 16: Input nama dan umur, hitung tahun lahir")
# Tulis jawabanmu di bawah (uncomment untuk mengaktifkan input):
# nama = input("Masukkan nama: ")
# umur = int(input("Masukkan umur: "))


# --- Soal 17 ---
print("\n📝 Soal 17: Konversi suhu - celsius ke fahrenheit dan kelvin")
# Rumus: F = C * 9/5 + 32, K = C + 273.15
# Tulis jawabanmu di bawah:


# --- Soal 18 ---
print("\n📝 Soal 18: Hitung (10+5)*2 - 8/4 + 3**2")
# Tulis jawabanmu di bawah:


# --- Soal 19 ---
print("\n📝 Soal 19: Demonstrasikan perbedaan referensi vs shallow copy list")
# Tulis jawabanmu di bawah:


# --- Soal 20 ---
print("\n📝 Soal 20: Kalkulator sederhana dengan num1, num2, operator, result")
# Tulis jawabanmu di bawah:


print("\n" + "=" * 60)
print("Selesaikan semua soal di atas! 💪")
print("=" * 60)
