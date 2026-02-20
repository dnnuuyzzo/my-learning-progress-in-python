"""
===============================================
BOOLEAN DI PYTHON
===============================================

Boolean adalah tipe data yang hanya memiliki dua nilai:
- True (benar)
- False (salah)

Boolean sangat penting untuk kontrol alur program (if, while, dll)
"""

# =====================================
# 1. NILAI BOOLEAN DASAR
# =====================================

benar = True
salah = False

print(f"benar = {benar}, tipe: {type(benar)}")
print(f"salah = {salah}, tipe: {type(salah)}")

# =====================================
# 2. OPERATOR PERBANDINGAN
# =====================================

a = 10
b = 5

print("\n=== Operator Perbandingan ===")
print(f"a = {a}, b = {b}")
print(f"a == b (sama dengan): {a == b}")        # False
print(f"a != b (tidak sama dengan): {a != b}")   # True
print(f"a > b (lebih besar): {a > b}")          # True
print(f"a < b (lebih kecil): {a < b}")          # False
print(f"a >= b (lebih besar atau sama): {a >= b}")  # True
print(f"a <= b (lebih kecil atau sama): {a <= b}")  # False

# Perbandingan string (berdasarkan urutan leksikografis/alfabet)
print("\n=== Perbandingan String ===")
print(f"'apple' < 'banana': {'apple' < 'banana'}")  # True
print(f"'Python' == 'python': {'Python' == 'python'}")  # False (case-sensitive)

# =====================================
# 3. OPERATOR LOGIKA
# =====================================

x = True
y = False

print("\n=== Operator Logika ===")
print(f"x = {x}, y = {y}")

# AND - True jika keduanya True
print(f"x and y: {x and y}")  # False
print(f"True and True: {True and True}")  # True

# OR - True jika salah satu True
print(f"x or y: {x or y}")  # True
print(f"False or False: {False or False}")  # False

# NOT - Membalik nilai
print(f"not x: {not x}")  # False
print(f"not y: {not y}")  # True

# =====================================
# 4. TABEL KEBENARAN
# =====================================

print("\n=== Tabel Kebenaran AND ===")
print("A       | B       | A and B")
print("-" * 30)
print(f"True    | True    | {True and True}")
print(f"True    | False   | {True and False}")
print(f"False   | True    | {False and True}")
print(f"False   | False   | {False and False}")

print("\n=== Tabel Kebenaran OR ===")
print("A       | B       | A or B")
print("-" * 30)
print(f"True    | True    | {True or True}")
print(f"True    | False   | {True or False}")
print(f"False   | True    | {False or True}")
print(f"False   | False   | {False or False}")

# =====================================
# 5. EVALUASI BOOLEAN (TRUTHY DAN FALSY)
# =====================================

"""
Di Python, setiap nilai dapat dievaluasi sebagai boolean:

FALSY (dianggap False):
- False
- None
- 0 (nol, termasuk 0.0)
- "" (string kosong)
- [] (list kosong)
- {} (dictionary kosong)
- () (tuple kosong)
- set() (set kosong)

TRUTHY (dianggap True):
- Semua nilai selain yang falsy di atas
"""

print("\n=== Truthy dan Falsy ===")
print(f"bool(1): {bool(1)}")        # True
print(f"bool(0): {bool(0)}")        # False
print(f"bool(-1): {bool(-1)}")      # True
print(f"bool(''): {bool('')}")      # False
print(f"bool('hello'): {bool('hello')}")  # True
print(f"bool([]): {bool([])}")      # False
print(f"bool([1, 2]): {bool([1, 2])}")  # True
print(f"bool(None): {bool(None)}")  # False

# =====================================
# 6. SHORT-CIRCUIT EVALUATION
# =====================================

"""
Python menggunakan short-circuit evaluation:
- AND: Jika nilai pertama False, nilai kedua tidak dievaluasi
- OR: Jika nilai pertama True, nilai kedua tidak dievaluasi
"""

print("\n=== Short-Circuit Evaluation ===")

# AND mengembalikan nilai pertama yang False, atau nilai terakhir jika semua True
print(f"0 and 5: {0 and 5}")        # 0 (karena 0 adalah False)
print(f"3 and 5: {3 and 5}")        # 5 (keduanya True, kembalikan yang terakhir)
print(f"'' and 'hello': {'' and 'hello'}")  # '' (string kosong adalah False)

# OR mengembalikan nilai pertama yang True, atau nilai terakhir jika semua False
print(f"0 or 5: {0 or 5}")          # 5 (karena 0 adalah False, evaluasi yang kedua)
print(f"3 or 5: {3 or 5}")          # 3 (3 adalah True, langsung kembalikan)
print(f"'' or 'hello': {'' or 'hello'}")  # 'hello'

# Aplikasi praktis: nilai default
nama = "" or "Guest"
print(f"Nama: {nama}")  # Guest

# =====================================
# 7. OPERATOR is DAN is not
# =====================================

"""
== membandingkan nilai
is membandingkan identitas (apakah objek yang sama di memori)
"""

print("\n=== is vs == ===")

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a = {a}")
print(f"b = {b}")
print(f"c = a")

print(f"a == b: {a == b}")  # True (nilainya sama)
print(f"a is b: {a is b}")  # False (objek berbeda di memori)
print(f"a is c: {a is c}")  # True (objek yang sama)

# is biasanya digunakan untuk membandingkan dengan None
nilai = None
print(f"nilai is None: {nilai is None}")  # True

# =====================================
# 8. OPERATOR in DAN not in
# =====================================

print("\n=== in dan not in ===")

buah = ["apel", "jeruk", "mangga"]
print(f"buah = {buah}")
print(f"'apel' in buah: {'apel' in buah}")      # True
print(f"'pisang' in buah: {'pisang' in buah}")  # False
print(f"'pisang' not in buah: {'pisang' not in buah}")  # True

kata = "Python"
print(f"'th' in '{kata}': {'th' in kata}")  # True

# =====================================
# 9. KOMBINASI OPERATOR
# =====================================

print("\n=== Kombinasi Operator ===")

umur = 25
gaji = 5000000

# Contoh kondisi kompleks
memenuhi_syarat = umur >= 21 and gaji >= 4000000
print(f"Umur: {umur}, Gaji: {gaji}")
print(f"Memenuhi syarat (umur >= 21 dan gaji >= 4M): {memenuhi_syarat}")

# Dengan tanda kurung untuk kejelasan
nilai = 85
kehadiran = 90
status = (nilai >= 80 and kehadiran >= 85) or nilai >= 95
print(f"Nilai: {nilai}, Kehadiran: {kehadiran}%")
print(f"Lulus: {status}")

# =============================================================================
# LATIHAN BOOLEAN - 20 SOAL (4 TINGKAT KESULITAN)
# =============================================================================

"""
================================================================================
                        DAFTAR SOAL LATIHAN BOOLEAN
================================================================================

🟢 BASIC (1-5) - Dasar-dasar Boolean
   1. Buat variabel benar=True dan salah=False, print keduanya
   2. Bandingkan 10 > 5, 10 < 5, 10 == 10, 10 != 5
   3. Cek apakah "Python" == "python" (case-sensitive)
   4. Gunakan not untuk membalik True menjadi False
   5. Hitung hasil: True and True, True and False, False and False

🟡 INTERMEDIATE (6-10) - Operator Logika
   6. Hitung hasil: True or False, False or False, True or True
   7. Tentukan hasil: not (True and False)
   8. Buat ekspresi yang True jika angka antara 10 dan 20 (inklusif)
   9. Cek apakah 'Python' ada dalam list ['Java', 'Python', 'C++']
   10. Cek apakah 'Ruby' tidak ada dalam list ['Java', 'Python', 'C++']

🟠 ADVANCED (11-15) - Truthy & Falsy
   11. Cek nilai boolean dari: 0, 1, -1, "", "hello", [], [1,2]
   12. Jelaskan hasil dari: ([] or "default")
   13. Jelaskan hasil dari: ("hello" and "world")
   14. Buat kondisi: lulus jika (nilai >= 70 AND kehadiran >= 80) OR nilai >= 90
   15. Gunakan 'is' untuk membandingkan None: x = None, cek x is None

🔴 EXPERT (16-20) - Tantangan Boolean
   16. Buat truth table lengkap untuk AND dan OR (4 kombinasi masing-masing)
   17. Demonstrasikan short-circuit: (False and print("Tidak muncul"))
   18. Buat validasi: umur >= 17 AND punya_sim == True AND tidak_mabuk == True
   19. Bedakan == vs is: a=[1,2], b=[1,2], c=a. Bandingkan a==b, a is b, a is c
   20. Buat sistem login: valid jika (username=="admin" AND password=="123")
       ATAU is_guest==True

================================================================================
"""

print("\n" + "=" * 60)
print("LATIHAN BOOLEAN - Kerjakan di bawah ini!")
print("=" * 60)

# =============================================================================
# 🟢 BASIC (LEVEL 1-5)
# =============================================================================

# --- Soal 1 ---
print("\n📝 Soal 1: Buat benar=True dan salah=False")
# Tulis jawabanmu di bawah:


# --- Soal 2 ---
print("\n📝 Soal 2: Bandingkan 10>5, 10<5, 10==10, 10!=5")
# Tulis jawabanmu di bawah:


# --- Soal 3 ---
print("\n📝 Soal 3: Cek 'Python' == 'python'")
# Tulis jawabanmu di bawah:


# --- Soal 4 ---
print("\n📝 Soal 4: Gunakan not untuk membalik True")
# Tulis jawabanmu di bawah:


# --- Soal 5 ---
print("\n📝 Soal 5: True and True, True and False, False and False")
# Tulis jawabanmu di bawah:


# =============================================================================
# 🟡 INTERMEDIATE (LEVEL 6-10)
# =============================================================================

# --- Soal 6 ---
print("\n📝 Soal 6: True or False, False or False, True or True")
# Tulis jawabanmu di bawah:


# --- Soal 7 ---
print("\n📝 Soal 7: Hitung not (True and False)")
# Tulis jawabanmu di bawah:


# --- Soal 8 ---
print("\n📝 Soal 8: Ekspresi True jika angka antara 10 dan 20")
angka = 15  # Coba dengan angka lain juga
# Tulis jawabanmu di bawah:


# --- Soal 9 ---
print("\n📝 Soal 9: Cek 'Python' in ['Java', 'Python', 'C++']")
# Tulis jawabanmu di bawah:


# --- Soal 10 ---
print("\n📝 Soal 10: Cek 'Ruby' not in list")
# Tulis jawabanmu di bawah:


# =============================================================================
# 🟠 ADVANCED (LEVEL 11-15)
# =============================================================================

# --- Soal 11 ---
print("\n📝 Soal 11: Cek bool() dari 0, 1, -1, '', 'hello', [], [1,2]")
# Tulis jawabanmu di bawah:


# --- Soal 12 ---
print("\n📝 Soal 12: Jelaskan ([] or 'default') dalam komentar")
# Tulis jawabanmu di bawah:


# --- Soal 13 ---
print("\n📝 Soal 13: Jelaskan ('hello' and 'world') dalam komentar")
# Tulis jawabanmu di bawah:


# --- Soal 14 ---
print("\n📝 Soal 14: Kondisi lulus (nilai>=70 AND kehadiran>=80) OR nilai>=90")
nilai = 75
kehadiran = 85
# Tulis jawabanmu di bawah:


# --- Soal 15 ---
print("\n📝 Soal 15: x = None, cek x is None")
# Tulis jawabanmu di bawah:


# =============================================================================
# 🔴 EXPERT (LEVEL 16-20)
# =============================================================================

# --- Soal 16 ---
print("\n📝 Soal 16: Truth table untuk AND dan OR")
# Tulis jawabanmu di bawah:


# --- Soal 17 ---
print("\n📝 Soal 17: Short-circuit evaluation demo")
# Tulis jawabanmu di bawah:


# --- Soal 18 ---
print("\n📝 Soal 18: Validasi mengemudi")
umur = 20
punya_sim = True
tidak_mabuk = True
# Tulis jawabanmu di bawah:


# --- Soal 19 ---
print("\n📝 Soal 19: Bedakan == vs is pada list")
# Tulis jawabanmu di bawah:


# --- Soal 20 ---
print("\n📝 Soal 20: Sistem login dengan username/password atau guest")
username = "admin"
password = "123"
is_guest = False
# Tulis jawabanmu di bawah:


print("\n" + "=" * 60)
print("Selesaikan semua soal di atas! 💪")
print("=" * 60)
