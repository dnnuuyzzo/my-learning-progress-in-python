"""
===============================================
TIPE DATA NUMERIK DI PYTHON
===============================================

Python memiliki 3 tipe data numerik:
1. int (Integer) - Bilangan bulat
2. float (Floating Point) - Bilangan desimal
3. complex - Bilangan kompleks
"""

# =====================================
# 1. INTEGER (int)
# =====================================

# Integer adalah bilangan bulat (positif atau negatif) tanpa desimal
bilangan_positif = 100
bilangan_negatif = -50
nol = 0
bilangan_besar = 999999999999999999999  # Python bisa handle angka sangat besar

print(f"Positif: {bilangan_positif}, Tipe: {type(bilangan_positif)}")
print(f"Negatif: {bilangan_negatif}")
print(f"Bilangan besar: {bilangan_besar}")

# Sistem bilangan lain
biner = 0b1010       # Binary (basis 2) = 10
oktal = 0o17         # Octal (basis 8) = 15
heksadesimal = 0xFF  # Hexadecimal (basis 16) = 255

print(f"Binary 0b1010 = {biner}")
print(f"Octal 0o17 = {oktal}")
print(f"Hex 0xFF = {heksadesimal}")

# =====================================
# 2. FLOAT (Floating Point)
# =====================================

# Float adalah bilangan dengan titik desimal
pi = 3.14159
suhu = -40.5
desimal_kecil = 0.000001

print(f"\nPI: {pi}, Tipe: {type(pi)}")
print(f"Suhu: {suhu}")

# Notasi ilmiah (scientific notation)
angka_besar = 1.5e10   # 1.5 × 10^10 = 15000000000
angka_kecil = 2.5e-5   # 2.5 × 10^-5 = 0.000025

print(f"1.5e10 = {angka_besar}")
print(f"2.5e-5 = {angka_kecil}")

# Perhatian: Float memiliki keterbatasan presisi
hasil = 0.1 + 0.2
print(f"0.1 + 0.2 = {hasil}")  # 0.30000000000000004

# =====================================
# 3. COMPLEX (Bilangan Kompleks)
# =====================================

# Bilangan kompleks memiliki bagian real dan imaginer
kompleks1 = 3 + 4j
kompleks2 = complex(2, 5)  # 2 + 5j

print(f"\nKompleks: {kompleks1}, Tipe: {type(kompleks1)}")
print(f"Bagian real: {kompleks1.real}")
print(f"Bagian imaginer: {kompleks1.imag}")

# =====================================
# 4. OPERASI ARITMATIKA
# =====================================

a = 15
b = 4

print(f"\n=== Operasi Aritmatika (a={a}, b={b}) ===")
print(f"Penjumlahan: {a} + {b} = {a + b}")
print(f"Pengurangan: {a} - {b} = {a - b}")
print(f"Perkalian: {a} * {b} = {a * b}")
print(f"Pembagian: {a} / {b} = {a / b}")  # Selalu menghasilkan float
print(f"Pembagian Bulat: {a} // {b} = {a // b}")  # Floor division
print(f"Modulus: {a} % {b} = {a % b}")  # Sisa bagi
print(f"Pangkat: {a} ** {b} = {a ** b}")  # 15^4

# =====================================
# 5. OPERATOR ASSIGNMENT GABUNGAN
# =====================================

x = 10
print(f"\n=== Operator Assignment (x awal = {x}) ===")

x += 5   # x = x + 5
print(f"x += 5 → x = {x}")

x -= 3   # x = x - 3
print(f"x -= 3 → x = {x}")

x *= 2   # x = x * 2
print(f"x *= 2 → x = {x}")

x /= 4   # x = x / 4
print(f"x /= 4 → x = {x}")

x //= 2  # x = x // 2
print(f"x //= 2 → x = {x}")

x **= 3  # x = x ** 3
print(f"x **= 3 → x = {x}")

# =====================================
# 6. FUNGSI MATEMATIKA BUILT-IN
# =====================================

print("\n=== Fungsi Matematika Built-in ===")
print(f"abs(-10) = {abs(-10)}")  # Nilai absolut
print(f"pow(2, 3) = {pow(2, 3)}")  # Pangkat
print(f"round(3.7) = {round(3.7)}")  # Pembulatan
print(f"round(3.14159, 2) = {round(3.14159, 2)}")  # Pembulatan ke 2 desimal
print(f"min(1, 5, 3) = {min(1, 5, 3)}")  # Nilai minimum
print(f"max(1, 5, 3) = {max(1, 5, 3)}")  # Nilai maksimum
print(f"sum([1, 2, 3, 4, 5]) = {sum([1, 2, 3, 4, 5])}")  # Jumlah dari list

# =====================================
# 7. MODULE MATH
# =====================================

import math

print("\n=== Modul Math ===")
print(f"math.pi = {math.pi}")
print(f"math.e = {math.e}")
print(f"math.sqrt(16) = {math.sqrt(16)}")  # Akar kuadrat
print(f"math.ceil(4.2) = {math.ceil(4.2)}")  # Pembulatan ke atas
print(f"math.floor(4.8) = {math.floor(4.8)}")  # Pembulatan ke bawah
print(f"math.factorial(5) = {math.factorial(5)}")  # Faktorial
print(f"math.log(100, 10) = {math.log(100, 10)}")  # Logaritma
print(f"math.sin(math.radians(90)) = {math.sin(math.radians(90))}")  # Sin 90°

# =============================================================================
# LATIHAN TIPE DATA NUMERIK - 20 SOAL (4 TINGKAT KESULITAN)
# =============================================================================

"""
================================================================================
                    DAFTAR SOAL LATIHAN TIPE DATA NUMERIK
================================================================================

🟢 BASIC (1-5) - Dasar-dasar Numerik
   1. Buat variabel integer positif, negatif, dan nol. Print semua.
   2. Buat variabel float untuk PI (3.14159) dan suhu (-40.5). Print semua.
   3. Hitung hasil: 15 + 7, 20 - 8, 6 * 9, 50 / 4
   4. Hitung 17 // 5 (pembagian bulat) dan 17 % 5 (modulus). Jelaskan hasilnya.
   5. Hitung 2 pangkat 10 menggunakan operator **

🟡 INTERMEDIATE (6-10) - Operasi Lanjutan
   6. Hitung luas lingkaran dengan jari-jari 7 (gunakan math.pi)
   7. Konversi suhu 100°F ke Celsius. Rumus: C = (F - 32) × 5/9
   8. Hitung akar kuadrat dari 144 tanpa math.sqrt() (Hint: pangkat 0.5)
   9. Gunakan round() untuk membulatkan 3.7, 3.2, dan 3.5
   10. Buat variabel dengan notasi ilmiah: 1.5e6 dan 2.5e-4. Print nilainya.

🟠 ADVANCED (11-15) - Fungsi Matematika
   11. Dari list [45, 23, 78, 12, 56], cari min, max, dan sum
   12. Gunakan abs() untuk nilai absolut dari -25, -3.14, dan 0
   13. Gunakan math.ceil() dan math.floor() untuk 4.2 dan 4.8
   14. Hitung faktorial dari 7 menggunakan math.factorial()
   15. Konversi biner 0b1101 ke desimal, dan desimal 25 ke biner (bin())

🔴 EXPERT (16-20) - Tantangan Numerik
   16. Hitung hipotenusa segitiga dengan sisi 3 dan 4 (teorema Pythagoras)
   17. Buat kalkulator BMI: berat(kg) / tinggi(m)². Gunakan input().
   18. Hitung compound interest: A = P(1 + r/n)^(nt) untuk P=1000, r=0.05, n=12, t=5
   19. Konversi sudut 45° ke radian dan hitung sin, cos, tan-nya
   20. Buat program menghitung cicilan KPR: M = P[r(1+r)^n]/[(1+r)^n-1]
       (P=500jt, bunga=8%/tahun, tenor=20 tahun)

================================================================================
"""

print("\n" + "=" * 60)
print("LATIHAN TIPE DATA NUMERIK - Kerjakan di bawah ini!")
print("=" * 60)

# =============================================================================
# 🟢 BASIC (LEVEL 1-5)
# =============================================================================

# --- Soal 1 ---
print("\n📝 Soal 1: Buat integer positif, negatif, dan nol")
# Tulis jawabanmu di bawah:


# --- Soal 2 ---
print("\n📝 Soal 2: Buat float untuk PI dan suhu negatif")
# Tulis jawabanmu di bawah:


# --- Soal 3 ---
print("\n📝 Soal 3: Hitung 15+7, 20-8, 6*9, 50/4")
# Tulis jawabanmu di bawah:


# --- Soal 4 ---
print("\n📝 Soal 4: Hitung 17//5 dan 17%5, jelaskan hasilnya")
# Tulis jawabanmu di bawah:


# --- Soal 5 ---
print("\n📝 Soal 5: Hitung 2 pangkat 10")
# Tulis jawabanmu di bawah:


# =============================================================================
# 🟡 INTERMEDIATE (LEVEL 6-10)
# =============================================================================

# --- Soal 6 ---
print("\n📝 Soal 6: Luas lingkaran r=7 (gunakan math.pi)")
# Tulis jawabanmu di bawah:


# --- Soal 7 ---
print("\n📝 Soal 7: Konversi 100°F ke Celsius")
# Tulis jawabanmu di bawah:


# --- Soal 8 ---
print("\n📝 Soal 8: Akar kuadrat 144 tanpa math.sqrt()")
# Tulis jawabanmu di bawah:


# --- Soal 9 ---
print("\n📝 Soal 9: Bulatkan 3.7, 3.2, dan 3.5 dengan round()")
# Tulis jawabanmu di bawah:


# --- Soal 10 ---
print("\n📝 Soal 10: Notasi ilmiah 1.5e6 dan 2.5e-4")
# Tulis jawabanmu di bawah:


# =============================================================================
# 🟠 ADVANCED (LEVEL 11-15)
# =============================================================================

# --- Soal 11 ---
print("\n📝 Soal 11: Min, max, sum dari [45, 23, 78, 12, 56]")
# Tulis jawabanmu di bawah:


# --- Soal 12 ---
print("\n📝 Soal 12: Nilai absolut dari -25, -3.14, 0")
# Tulis jawabanmu di bawah:


# --- Soal 13 ---
print("\n📝 Soal 13: math.ceil() dan math.floor() untuk 4.2 dan 4.8")
# Tulis jawabanmu di bawah:


# --- Soal 14 ---
print("\n📝 Soal 14: Faktorial dari 7")
# Tulis jawabanmu di bawah:


# --- Soal 15 ---
print("\n📝 Soal 15: Konversi biner 0b1101 ke desimal, 25 ke biner")
# Tulis jawabanmu di bawah:


# =============================================================================
# 🔴 EXPERT (LEVEL 16-20)
# =============================================================================

# --- Soal 16 ---
print("\n📝 Soal 16: Hipotenusa segitiga sisi 3 dan 4")
# Tulis jawabanmu di bawah:


# --- Soal 17 ---
print("\n📝 Soal 17: Kalkulator BMI")
# Tulis jawabanmu di bawah:


# --- Soal 18 ---
print("\n📝 Soal 18: Compound interest P=1000, r=0.05, n=12, t=5")
# Rumus: A = P(1 + r/n)^(nt)
# Tulis jawabanmu di bawah:


# --- Soal 19 ---
print("\n📝 Soal 19: Konversi 45° ke radian, hitung sin/cos/tan")
# Tulis jawabanmu di bawah:


# --- Soal 20 ---
print("\n📝 Soal 20: Cicilan KPR P=500jt, bunga=8%, tenor=20 tahun")
# Rumus: M = P[r(1+r)^n]/[(1+r)^n-1]
# Tulis jawabanmu di bawah:


print("\n" + "=" * 60)
print("Selesaikan semua soal di atas! 💪")
print("=" * 60)
