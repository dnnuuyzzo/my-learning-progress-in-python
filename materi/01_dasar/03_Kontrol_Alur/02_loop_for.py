"""
===============================================
LOOP FOR DI PYTHON
===============================================

For loop digunakan untuk iterasi sequence (list, tuple, string, dll).
"""

# =====================================
# 1. FOR LOOP DASAR
# =====================================

buah = ["apel", "jeruk", "mangga"]
for item in buah:
    print(f"Buah: {item}")

# Iterasi string
for char in "Python":
    print(char, end=" ")
print()

# =====================================
# 2. RANGE()
# =====================================

# range(stop)
for i in range(5):
    print(i, end=" ")  # 0 1 2 3 4
print()

# range(start, stop)
for i in range(1, 6):
    print(i, end=" ")  # 1 2 3 4 5
print()

# range(start, stop, step)
for i in range(0, 10, 2):
    print(i, end=" ")  # 0 2 4 6 8
print()

# range mundur
for i in range(5, 0, -1):
    print(i, end=" ")  # 5 4 3 2 1
print()

# =====================================
# 3. ENUMERATE()
# =====================================

buah = ["apel", "jeruk", "mangga"]
for index, item in enumerate(buah):
    print(f"{index}: {item}")

# Dengan start index berbeda
for index, item in enumerate(buah, start=1):
    print(f"{index}. {item}")

# =====================================
# 4. ZIP()
# =====================================

nama = ["Budi", "Ani", "Cici"]
nilai = [85, 90, 78]

for n, v in zip(nama, nilai):
    print(f"{n}: {v}")

# =====================================
# 5. NESTED FOR LOOP
# =====================================

print("\n=== Tabel Perkalian ===")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j}", end="\t")
    print()

# =====================================
# 6. BREAK DAN CONTINUE
# =====================================

print("\n=== Break ===")
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
print()

print("=== Continue ===")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end=" ")  # Hanya ganjil
print()

# =====================================
# 7. ELSE PADA FOR
# =====================================

for i in range(5):
    print(i, end=" ")
else:
    print("\nLoop selesai tanpa break")

# Dengan break, else tidak dijalankan
for i in range(5):
    if i == 3:
        break
else:
    print("Ini tidak akan muncul")

# =====================================
# 8. ITERASI DICTIONARY
# =====================================

data = {"nama": "Budi", "umur": 25, "kota": "Jakarta"}

for key in data:
    print(f"{key}: {data[key]}")

for key, value in data.items():
    print(f"{key} = {value}")

# =============================================================================
# LATIHAN FOR LOOP - 20 SOAL (4 TINGKAT KESULITAN)
# =============================================================================

"""
================================================================================
                    DAFTAR SOAL LATIHAN FOR LOOP
================================================================================

🟢 BASIC (1-5) - Dasar-dasar For Loop
   1. Print semua item dalam list ["apel", "jeruk", "mangga"]
   2. Print setiap karakter dari string "Python"
   3. Print angka 1 sampai 10 menggunakan range()
   4. Print angka genap dari 2 sampai 20
   5. Print angka mundur dari 10 ke 1

🟡 INTERMEDIATE (6-10) - Enumerate & Zip
   6. Gunakan enumerate() untuk print index dan item dari list buah
   7. Gunakan zip() untuk menggabungkan nama dan nilai siswa
   8. Hitung jumlah total dari list [10, 20, 30, 40, 50] dengan loop
   9. Cari nilai maksimum dari list tanpa menggunakan max()
   10. Buat tabel perkalian 1-5 menggunakan nested loop

🟠 ADVANCED (11-15) - Break, Continue, Else
   11. Gunakan break untuk berhenti saat menemukan angka 5
   12. Gunakan continue untuk skip angka genap, print hanya ganjil
   13. Gunakan else pada for loop (print "selesai" jika tidak break)
   14. Cari index dari elemen tertentu dalam list tanpa .index()
   15. Iterasi dictionary dan print key-value pairs

🔴 EXPERT (16-20) - Tantangan Loop
   16. Cetak angka 1-100 yang habis dibagi 3 DAN 5 (FizzBuzz logic)
   17. Buat pola segitiga bintang (tinggi 5)
   18. Cari semua bilangan prima dari 1-50
   19. Hitung faktorial dari 10 menggunakan for loop
   20. Buat spiral matrix atau pattern tertentu dengan nested loop

================================================================================
"""

print("\n" + "=" * 60)
print("LATIHAN FOR LOOP - Kerjakan di bawah ini!")
print("=" * 60)

# =============================================================================
# 🟢 BASIC (LEVEL 1-5)
# =============================================================================

# --- Soal 1 ---
print("\n📝 Soal 1: Print semua item list buah")
buah = ["apel", "jeruk", "mangga"]
# Tulis jawabanmu di bawah:


# --- Soal 2 ---
print("\n📝 Soal 2: Print setiap karakter 'Python'")
# Tulis jawabanmu di bawah:


# --- Soal 3 ---
print("\n📝 Soal 3: Print 1-10 dengan range()")
# Tulis jawabanmu di bawah:


# --- Soal 4 ---
print("\n📝 Soal 4: Print genap 2-20")
# Tulis jawabanmu di bawah:


# --- Soal 5 ---
print("\n📝 Soal 5: Countdown 10 ke 1")
# Tulis jawabanmu di bawah:


# =============================================================================
# 🟡 INTERMEDIATE (LEVEL 6-10)
# =============================================================================

# --- Soal 6 ---
print("\n📝 Soal 6: Enumerate pada list buah")
# Tulis jawabanmu di bawah:


# --- Soal 7 ---
print("\n📝 Soal 7: Zip nama dan nilai")
nama = ["Budi", "Ani", "Cici"]
nilai = [85, 90, 78]
# Tulis jawabanmu di bawah:


# --- Soal 8 ---
print("\n📝 Soal 8: Hitung total list dengan loop")
angka = [10, 20, 30, 40, 50]
# Tulis jawabanmu di bawah:


# --- Soal 9 ---
print("\n📝 Soal 9: Cari max tanpa fungsi max()")
data = [45, 23, 78, 12, 56]
# Tulis jawabanmu di bawah:


# --- Soal 10 ---
print("\n📝 Soal 10: Tabel perkalian 1-5")
# Tulis jawabanmu di bawah:


# =============================================================================
# 🟠 ADVANCED (LEVEL 11-15)
# =============================================================================

# --- Soal 11 ---
print("\n📝 Soal 11: Break saat menemukan 5")
# Tulis jawabanmu di bawah:


# --- Soal 12 ---
print("\n📝 Soal 12: Continue skip genap")
# Tulis jawabanmu di bawah:


# --- Soal 13 ---
print("\n📝 Soal 13: For-else")
# Tulis jawabanmu di bawah:


# --- Soal 14 ---
print("\n📝 Soal 14: Cari index elemen")
items = ["a", "b", "c", "d", "e"]
cari = "c"
# Tulis jawabanmu di bawah:


# --- Soal 15 ---
print("\n📝 Soal 15: Iterasi dictionary")
person = {"nama": "Budi", "umur": 25, "kota": "Jakarta"}
# Tulis jawabanmu di bawah:


# =============================================================================
# 🔴 EXPERT (LEVEL 16-20)
# =============================================================================

# --- Soal 16 ---
print("\n📝 Soal 16: FizzBuzz (habis dibagi 3 DAN 5)")
# Tulis jawabanmu di bawah:


# --- Soal 17 ---
print("\n📝 Soal 17: Segitiga bintang tinggi 5")
# Tulis jawabanmu di bawah:


# --- Soal 18 ---
print("\n📝 Soal 18: Bilangan prima 1-50")
# Tulis jawabanmu di bawah:


# --- Soal 19 ---
print("\n📝 Soal 19: Faktorial 10")
# Tulis jawabanmu di bawah:


# --- Soal 20 ---
print("\n📝 Soal 20: Pattern/Pola angka")
# Contoh output:
# 1
# 12
# 123
# 1234
# Tulis jawabanmu di bawah:


print("\n" + "=" * 60)
print("Selesaikan semua soal di atas! 💪")
print("=" * 60)

