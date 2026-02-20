"""
===============================================
LOOP WHILE DI PYTHON
===============================================

While loop menjalankan kode selama kondisi True.
"""

# =====================================
# 1. WHILE DASAR
# =====================================

counter = 0
while counter < 5:
    print(f"Counter: {counter}")
    counter += 1

# =====================================
# 2. WHILE DENGAN BREAK
# =====================================

print("\n=== While dengan Break ===")
while True:
    jawaban = "keluar"  # Simulasi input
    if jawaban.lower() == "keluar":
        print("Keluar dari loop")
        break
    print(f"Anda mengetik: {jawaban}")

# =====================================
# 3. WHILE DENGAN CONTINUE
# =====================================

print("\n=== While dengan Continue ===")
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i, end=" ")  # Hanya ganjil
print()

# =====================================
# 4. WHILE-ELSE
# =====================================

n = 5
while n > 0:
    print(n, end=" ")
    n -= 1
else:
    print("\nHitung mundur selesai!")

# =====================================
# 5. CONTOH: MENEBAK ANGKA
# =====================================

print("\n=== Game Tebak Angka ===")
angka_rahasia = 7
tebakan_max = 3
percobaan = 0

while percobaan < tebakan_max:
    tebakan = 5  # Simulasi input
    percobaan += 1
    
    if tebakan == angka_rahasia:
        print(f"Benar! Anda menebak dalam {percobaan} percobaan")
        break
    elif tebakan < angka_rahasia:
        print("Terlalu kecil!")
    else:
        print("Terlalu besar!")
else:
    print(f"Game over! Angkanya adalah {angka_rahasia}")

# =====================================
# 6. INFINITE LOOP (HATI-HATI!)
# =====================================

# JANGAN jalankan ini tanpa break:
# while True:
#     print("Loop forever...")

# Contoh penggunaan yang benar
counter = 0
while True:
    counter += 1
    if counter >= 5:
        break
    print(f"Iterasi ke-{counter}")

# =====================================
# 7. NESTED WHILE
# =====================================

print("\n=== Nested While ===")
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"({i},{j})", end=" ")
        j += 1
    print()
    i += 1

# =============================================================================
# LATIHAN WHILE LOOP - 20 SOAL (4 TINGKAT KESULITAN)
# =============================================================================

"""
================================================================================
                    DAFTAR SOAL LATIHAN WHILE LOOP
================================================================================

🟢 BASIC (1-5) - Dasar-dasar While Loop
   1. Print angka 1-10 menggunakan while loop
   2. Buat countdown dari 10 ke 0
   3. Hitung jumlah 1+2+3+...+100 dengan while
   4. Print "Hello" sebanyak 5 kali dengan while
   5. Buat counter yang berhenti di angka 50

🟡 INTERMEDIATE (6-10) - Break & Continue
   6. Gunakan break untuk keluar dari infinite loop
   7. Gunakan continue untuk skip angka kelipatan 3
   8. Buat menu dengan pilihan keluar (break saat pilih "exit")
   9. Hitung mundur dengan skip angka genap
   10. While-else: print pesan berbeda jika loop selesai normal vs break

🟠 ADVANCED (11-15) - Aplikasi While
   11. Hitung faktorial dengan while loop
   12. Buat program tebak angka (1-10) dengan batas percobaan
   13. Cari bilangan Fibonacci sampai < 100 dengan while
   14. Reverse angka: 12345 menjadi 54321 dengan while
   15. Hitung digit dalam angka (misal: 12345 = 5 digit)

🔴 EXPERT (16-20) - Tantangan While Loop
   16. Buat ATM sederhana: cek saldo, tarik, setor (loop sampai "keluar")
   17. Validasi input: minta angka positif, ulang jika salah
   18. Buat password checker dengan max 3 percobaan
   19. Cari GCD (Greatest Common Divisor) dua angka dengan algoritma Euclidean
   20. Buat program antrian: tambah, proses, tampilkan (loop sampai kosong)

================================================================================
"""

print("\n" + "=" * 60)
print("LATIHAN WHILE LOOP - Kerjakan di bawah ini!")
print("=" * 60)

# =============================================================================
# 🟢 BASIC (LEVEL 1-5)
# =============================================================================

# --- Soal 1 ---
print("\n📝 Soal 1: Print 1-10 dengan while")
# Tulis jawabanmu di bawah:


# --- Soal 2 ---
print("\n📝 Soal 2: Countdown 10 ke 0")
# Tulis jawabanmu di bawah:


# --- Soal 3 ---
print("\n📝 Soal 3: Jumlah 1+2+...+100")
# Tulis jawabanmu di bawah:


# --- Soal 4 ---
print("\n📝 Soal 4: Print 'Hello' 5 kali")
# Tulis jawabanmu di bawah:


# --- Soal 5 ---
print("\n📝 Soal 5: Counter sampai 50")
# Tulis jawabanmu di bawah:


# =============================================================================
# 🟡 INTERMEDIATE (LEVEL 6-10)
# =============================================================================

# --- Soal 6 ---
print("\n📝 Soal 6: Break dari infinite loop")
# Tulis jawabanmu di bawah:


# --- Soal 7 ---
print("\n📝 Soal 7: Continue skip kelipatan 3")
# Tulis jawabanmu di bawah:


# --- Soal 8 ---
print("\n📝 Soal 8: Menu dengan exit")
# Tulis jawabanmu di bawah (simulasi tanpa input):


# --- Soal 9 ---
print("\n📝 Soal 9: Countdown skip genap")
# Tulis jawabanmu di bawah:


# --- Soal 10 ---
print("\n📝 Soal 10: While-else")
# Tulis jawabanmu di bawah:


# =============================================================================
# 🟠 ADVANCED (LEVEL 11-15)
# =============================================================================

# --- Soal 11 ---
print("\n📝 Soal 11: Faktorial dengan while")
n = 5
# Tulis jawabanmu di bawah:


# --- Soal 12 ---
print("\n📝 Soal 12: Game tebak angka")
angka_rahasia = 7
max_percobaan = 3
# Tulis jawabanmu di bawah (simulasi):


# --- Soal 13 ---
print("\n📝 Soal 13: Fibonacci < 100")
# Tulis jawabanmu di bawah:


# --- Soal 14 ---
print("\n📝 Soal 14: Reverse angka 12345")
angka = 12345
# Tulis jawabanmu di bawah:


# --- Soal 15 ---
print("\n📝 Soal 15: Hitung jumlah digit")
angka = 123456
# Tulis jawabanmu di bawah:


# =============================================================================
# 🔴 EXPERT (LEVEL 16-20)
# =============================================================================

# --- Soal 16 ---
print("\n📝 Soal 16: ATM sederhana")
saldo = 1000000
# Tulis jawabanmu di bawah (simulasi menu):


# --- Soal 17 ---
print("\n📝 Soal 17: Validasi input positif")
# Tulis jawabanmu di bawah (simulasi):


# --- Soal 18 ---
print("\n📝 Soal 18: Password checker 3 percobaan")
password_benar = "rahasia123"
# Tulis jawabanmu di bawah (simulasi):


# --- Soal 19 ---
print("\n📝 Soal 19: GCD (Euclidean algorithm)")
a, b = 48, 18
# Tulis jawabanmu di bawah:


# --- Soal 20 ---
print("\n📝 Soal 20: Program antrian")
antrian = ["A", "B", "C", "D"]
# Tulis jawabanmu di bawah:


print("\n" + "=" * 60)
print("Selesaikan semua soal di atas! 💪")
print("=" * 60)

