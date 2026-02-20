"""
===============================================
KONDISIONAL IF-ELSE DI PYTHON
===============================================

Digunakan untuk membuat keputusan berdasarkan kondisi.
"""

# =====================================
# 1. IF SEDERHANA
# =====================================

umur = 18
if umur >= 17:
    print("Anda boleh membuat SIM")

# =====================================
# 2. IF-ELSE
# =====================================

nilai = 65
if nilai >= 70:
    print("Lulus")
else:
    print("Tidak Lulus")

# =====================================
# 3. IF-ELIF-ELSE
# =====================================

nilai = 85

if nilai >= 90:
    grade = "A"
elif nilai >= 80:
    grade = "B"
elif nilai >= 70:
    grade = "C"
elif nilai >= 60:
    grade = "D"
else:
    grade = "E"

print(f"Nilai: {nilai}, Grade: {grade}")

# =====================================
# 4. NESTED IF
# =====================================

umur = 25
punya_sim = True

if umur >= 17:
    if punya_sim:
        print("Boleh menyetir")
    else:
        print("Perlu membuat SIM dulu")
else:
    print("Belum cukup umur")

# =====================================
# 5. KONDISI DENGAN OPERATOR LOGIKA
# =====================================

username = "admin"
password = "12345"

if username == "admin" and password == "12345":
    print("Login berhasil!")

hari = "Sabtu"
if hari == "Sabtu" or hari == "Minggu":
    print("Hari libur!")

# =====================================
# 6. TERNARY OPERATOR
# =====================================

umur = 20
status = "Dewasa" if umur >= 18 else "Anak-anak"
print(f"Status: {status}")

# Nested ternary
nilai = 75
grade = "A" if nilai >= 90 else "B" if nilai >= 80 else "C" if nilai >= 70 else "D"
print(f"Grade: {grade}")

# =====================================
# 7. TRUTHY DAN FALSY DALAM KONDISI
# =====================================

nama = "Budi"
if nama:  # String tidak kosong = True
    print(f"Halo, {nama}!")

data = []
if not data:  # List kosong = False
    print("Data kosong")

# =====================================
# 8. MATCH-CASE (Python 3.10+)
# =====================================

# CATATAN: Hanya tersedia di Python 3.10+
hari = "Senin"

match hari:
    case "Senin":
        print("Hari pertama kerja")
    case "Jumat":
        print("Hampir weekend!")
    case "Sabtu" | "Minggu":
        print("Weekend!")
    case _:
        print("Hari biasa")

# =============================================================================
# LATIHAN IF-ELSE - 20 SOAL (4 TINGKAT KESULITAN)
# =============================================================================

"""
================================================================================
                    DAFTAR SOAL LATIHAN IF-ELSE
================================================================================

🟢 BASIC (1-5) - Dasar-dasar Kondisional
   1. Cek apakah angka 10 lebih besar dari 5
   2. Buat if-else: print "Lulus" jika nilai >= 70, else "Tidak Lulus"
   3. Cek apakah angka genap atau ganjil
   4. Bandingkan dua string: "Python" dan "python" (case-sensitive)
   5. Cek apakah list kosong atau tidak

🟡 INTERMEDIATE (6-10) - If-Elif-Else
   6. Buat sistem grade: A (>=90), B (>=80), C (>=70), D (>=60), E (<60)
   7. Cek apakah angka positif, negatif, atau nol
   8. Buat kondisi dengan AND: umur >= 17 AND punya_sim == True
   9. Buat kondisi dengan OR: hari == "Sabtu" OR hari == "Minggu"
   10. Nested if: cek umur, lalu cek apakah punya SIM

🟠 ADVANCED (11-15) - Ternary & Match-Case
   11. Gunakan ternary: status = "Dewasa" if umur >= 18 else "Anak"
   12. Nested ternary untuk grade (A/B/C/D)
   13. Gunakan match-case untuk hari dalam seminggu
   14. Cek multiple kondisi: lulus jika (nilai>=70 AND hadir>=80) OR nilai>=90
   15. Validasi login: username=="admin" AND password=="123"

🔴 EXPERT (16-20) - Tantangan Kondisional
   16. Buat program cek tahun kabisat (habis dibagi 4, kecuali 100, kecuali 400)
   17. Buat kalkulator sederhana: input dua angka dan operator (+,-,*,/)
   18. Buat program cek segitiga valid (jumlah dua sisi harus > sisi ketiga)
   19. Buat sistem ATM: cek saldo cukup, batas tarik harian, pin benar
   20. Buat grading kompleks dengan plus/minus: A+, A, A-, B+, B, B-, dst

================================================================================
"""

print("\n" + "=" * 60)
print("LATIHAN IF-ELSE - Kerjakan di bawah ini!")
print("=" * 60)

# =============================================================================
# 🟢 BASIC (LEVEL 1-5)
# =============================================================================

# --- Soal 1 ---
print("\n📝 Soal 1: Cek 10 > 5")
# Tulis jawabanmu di bawah:


# --- Soal 2 ---
print("\n📝 Soal 2: Lulus/Tidak berdasarkan nilai")
nilai = 65
# Tulis jawabanmu di bawah:


# --- Soal 3 ---
print("\n📝 Soal 3: Genap atau ganjil")
angka = 7
# Tulis jawabanmu di bawah:


# --- Soal 4 ---
print("\n📝 Soal 4: Bandingkan 'Python' dan 'python'")
# Tulis jawabanmu di bawah:


# --- Soal 5 ---
print("\n📝 Soal 5: Cek list kosong")
data = []
# Tulis jawabanmu di bawah:


# =============================================================================
# 🟡 INTERMEDIATE (LEVEL 6-10)
# =============================================================================

# --- Soal 6 ---
print("\n📝 Soal 6: Sistem grade A/B/C/D/E")
nilai = 85
# Tulis jawabanmu di bawah:


# --- Soal 7 ---
print("\n📝 Soal 7: Positif/Negatif/Nol")
angka = -5
# Tulis jawabanmu di bawah:


# --- Soal 8 ---
print("\n📝 Soal 8: Kondisi dengan AND")
umur = 20
punya_sim = True
# Tulis jawabanmu di bawah:


# --- Soal 9 ---
print("\n📝 Soal 9: Kondisi dengan OR")
hari = "Sabtu"
# Tulis jawabanmu di bawah:


# --- Soal 10 ---
print("\n📝 Soal 10: Nested if (umur & SIM)")
# Tulis jawabanmu di bawah:


# =============================================================================
# 🟠 ADVANCED (LEVEL 11-15)
# =============================================================================

# --- Soal 11 ---
print("\n📝 Soal 11: Ternary operator")
umur = 20
# Tulis jawabanmu di bawah:


# --- Soal 12 ---
print("\n📝 Soal 12: Nested ternary untuk grade")
nilai = 85
# Tulis jawabanmu di bawah:


# --- Soal 13 ---
print("\n📝 Soal 13: Match-case hari")
hari = "Senin"
# Tulis jawabanmu di bawah:


# --- Soal 14 ---
print("\n📝 Soal 14: Multiple kondisi untuk lulus")
nilai = 75
hadir = 85
# Tulis jawabanmu di bawah:


# --- Soal 15 ---
print("\n📝 Soal 15: Validasi login")
username = "admin"
password = "123"
# Tulis jawabanmu di bawah:


# =============================================================================
# 🔴 EXPERT (LEVEL 16-20)
# =============================================================================

# --- Soal 16 ---
print("\n📝 Soal 16: Cek tahun kabisat")
tahun = 2024
# Tulis jawabanmu di bawah:


# --- Soal 17 ---
print("\n📝 Soal 17: Kalkulator sederhana")
num1 = 10
num2 = 5
operator = "+"
# Tulis jawabanmu di bawah:


# --- Soal 18 ---
print("\n📝 Soal 18: Validasi segitiga")
sisi1, sisi2, sisi3 = 3, 4, 5
# Tulis jawabanmu di bawah:


# --- Soal 19 ---
print("\n📝 Soal 19: Sistem ATM")
saldo = 1000000
tarik = 500000
pin = "1234"
pin_input = "1234"
# Tulis jawabanmu di bawah:


# --- Soal 20 ---
print("\n📝 Soal 20: Grade dengan plus/minus")
nilai = 87
# Tulis jawabanmu di bawah:


print("\n" + "=" * 60)
print("Selesaikan semua soal di atas! 💪")
print("=" * 60)

