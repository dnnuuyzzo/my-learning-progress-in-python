"""
============================================================
           MATERI BELAJAR: LAMBDA FUNCTION PYTHON
============================================================

1. APA ITU LAMBDA?
   Lambda function adalah fungsi anonim (tanpa nama) yang 
   sifatnya kecil, sederhana, dan biasanya hanya digunakan 
   satu kali.

2. SYNTAX DASAR:
   lambda arguments : expression

   * lambda: Keyword wajib.
   * arguments: Parameter (bisa lebih dari satu).
   * expression: Operasi/logika yang akan dikembalikan hasilnya.

============================================================
"""

# ----------------------------------------------------------
# CONTOH 1: Perbandingan Fungsi Biasa vs Lambda
# ----------------------------------------------------------

# Fungsi Biasa (def)
def tambah_sepuluh(x):
    return x + 10

# Fungsi Lambda
tambah_sepuluh_lambda = lambda x: x + 10

print("--- CONTOH 1 ---")
print(f"Hasil Fungsi Biasa: {tambah_sepuluh(5)}")
print(f"Hasil Lambda: {tambah_sepuluh_lambda(5)}")
print()


# ----------------------------------------------------------
# CONTOH 2: Lambda dengan Banyak Argumen
# ----------------------------------------------------------
kali = lambda a, b: a * b

print("--- CONTOH 2 ---")
print(f"Hasil Perkalian (5 * 3): {kali(5, 3)}")
print()


# ----------------------------------------------------------
# CONTOH 3: Lambda di dalam Higher-Order Functions
# ----------------------------------------------------------
# Lambda sangat kuat jika digunakan bersama function bawaan 
# Python seperti filter(), map(), dan sorted().

angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# A. MAP (Mengubah setiap elemen)
kuadrat = list(map(lambda x: x**2, angka))

# B. FILTER (Menyaring elemen berdasarkan kondisi)
genap = list(filter(lambda x: x % 2 == 0, angka))

print("--- CONTOH 3 ---")
print(f"Daftar Angka: {angka}")
print(f"Hasil MAP (Kuadrat): {kuadrat}")
print(f"Hasil FILTER (Genap): {genap}")
print()


# ----------------------------------------------------------
# CONTOH 4: Sorting dengan Lambda
# ----------------------------------------------------------
data_mahasiswa = [
    {"nama": "Budi", "nilai": 85},
    {"nama": "Ani", "nilai": 95},
    {"nama": "Caca", "nilai": 80}
]

# Sortir berdasarkan nilai (kecil ke besar)
data_mahasiswa.sort(key=lambda mhs: mhs['nilai'])

print("--- CONTOH 4 ---")
print("Data Mahasiswa (Sort by Nilai):")
for mhs in data_mahasiswa:
    print(f"- {mhs['nama']}: {mhs['nilai']}")
print()


# ----------------------------------------------------------
# KAPAN HARUS MENGGUNAKAN LAMBDA?
# ----------------------------------------------------------
"""
GUNAKAN LAMBDA JIKA:
1. Logikanya sangat sederhana (hanya satu baris).
2. Hanya dipakai sekali (misal sebagai argumen fungsi lain).
3. Ingin kode terlihat lebih ringkas.

JANGAN GUNAKAN LAMBDA JIKA:
1. Logikanya kompleks (banyak if-else atau loop).
2. Fungsi akan dipakai berulang kali di banyak tempat.
3. Mengurangi keterbacaan kode (malah jadi bingung).
"""


# ============================================================
#                    LATIHAN SOAL
# ============================================================
"""
Kerjakan 15 soal berikut untuk menguji pemahaman Anda tentang 
Lambda Function. Tulis jawaban Anda di bawah setiap soal.
"""

print("\n" + "="*60)
print("                  LATIHAN SOAL")
print("="*60 + "\n")

# ----------------------------------------------------------
# SOAL 1 - MUDAH
# ----------------------------------------------------------
"""
Buatlah lambda function yang menerima satu parameter (x) 
dan mengembalikan nilai x dikurangi 5.
"""
# Jawaban Anda:
# soal_1 = 
soal_1 = lambda x: x - 5

# ----------------------------------------------------------
# SOAL 2 - MUDAH
# ----------------------------------------------------------
"""
Buatlah lambda function yang menerima dua parameter (a, b) 
dan mengembalikan hasil pembagian a / b.
"""
# Jawaban Anda:
# soal_2 = 
soal_2 = lambda a, b: float(a / b)

# ----------------------------------------------------------
# SOAL 3 - MUDAH
# ----------------------------------------------------------
"""
Gunakan lambda dengan map() untuk mengubah list berikut 
menjadi list yang berisi nilai masing-masing dikali 3.
data = [2, 4, 6, 8, 10]
"""
# Jawaban Anda:
# data = [2, 4, 6, 8, 10]
# hasil_soal_3 = 
data = [2, 4, 6, 8, 10]
hasil_soal_3 = list(map(lambda x: x * 3, data))

# ----------------------------------------------------------
# SOAL 4 - MUDAH
# ----------------------------------------------------------
"""
Gunakan lambda dengan filter() untuk menyaring angka ganjil 
dari list berikut:
angka = [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
# Jawaban Anda:
# angka = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# hasil_soal_4 = 
angka = [1, 2, 3, 4, 5, 6, 7, 8, 9]
hasil_soal_4 = list(filter(lambda x: x % 2 != 0, angka))

# ----------------------------------------------------------
# SOAL 5 - MUDAH
# ----------------------------------------------------------
"""
Buatlah lambda function yang menerima satu string dan 
mengembalikan panjang string tersebut.
"""
# Jawaban Anda:
# soal_5 = 
nama = "Danuardi Saputro"
soal_5 = lambda x: len(x)

# ----------------------------------------------------------
# SOAL 6 - SEDANG
# ----------------------------------------------------------
"""
Gunakan lambda dengan map() untuk mengubah semua string 
dalam list menjadi huruf kapital (uppercase).
kata = ["python", "lambda", "function"]
"""
# Jawaban Anda:
# kata = ["python", "lambda", "function"]
# hasil_soal_6 = 
kata = ["python", "lambda", "function"]
hasil_soal_6 = list(map(lambda x: x.upper(), kata))

# ----------------------------------------------------------
# SOAL 7 - SEDANG
# ----------------------------------------------------------
"""
Buatlah lambda function yang menerima tiga parameter (x, y, z) 
dan mengembalikan nilai rata-rata dari ketiganya.
"""
# Jawaban Anda:
# soal_7 = 
soal_7 = lambda x, y, z: (x + y + z) / 3  

# ----------------------------------------------------------
# SOAL 8 - SEDANG
# ----------------------------------------------------------
"""
Gunakan lambda dengan filter() untuk menyaring string yang 
panjangnya lebih dari 5 karakter.
daftar_kata = ["kucing", "anjing", "burung", "ikan", "gajah"]
"""
# Jawaban Anda:
daftar_kata = ["kucing", "anjing", "burung", "ikan", "gajah"]
hasil_soal_8 = list(filter(lambda x: len(x) > 5, daftar_kata))

# ----------------------------------------------------------
# SOAL 9 - SEDANG
# ----------------------------------------------------------
"""
Sortir list dictionary berikut berdasarkan umur (dari muda ke tua):
orang = [
    {"nama": "Ali", "umur": 25},
    {"nama": "Budi", "umur": 30},
    {"nama": "Citra", "umur": 22}
]
"""

# Jawaban Anda:
orang = [
    {"nama": "Ali", "umur": 25},
    {"nama": "Budi", "umur": 30},
    {"nama": "Citra", "umur": 22}
]

orang.sort(key= lambda x: x["umur"])


# ----------------------------------------------------------
# SOAL 10 - SEDANG
# ----------------------------------------------------------
"""
Buatlah lambda function yang menerima satu angka dan 
mengembalikan True jika angka tersebut habis dibagi 5, 
False jika tidak.
"""
# Jawaban Anda:
soal_10 = lambda x: x % 5 == 0

# ----------------------------------------------------------
# SOAL 11 - SEDANG
# ----------------------------------------------------------
"""
Gunakan lambda dengan map() untuk mengubah list angka 
menjadi list string dengan format "Angka: X".
nilai = [10, 20, 30, 40]
Hasil yang diharapkan: ["Angka: 10", "Angka: 20", "Angka: 30", "Angka: 40"]
"""
# Jawaban Anda:
nilai = [10, 20, 30, 40]
hasil_soal_11 = list(map(lambda x: str(f"Angka: {x}"), nilai))

# ---------------------------------------------a-------------
# SOAL 12 - MENENGAH
# ----------------------------------------------------------
"""
Gunakan lambda dengan filter() untuk menyaring angka yang 
merupakan kelipatan 3 ATAU kelipatan 5 dari list berikut:
angka = [1, 3, 5, 6, 9, 10, 12, 15, 18, 20]
"""
# Jawaban Anda:
angka = [1, 3, 5, 6, 9, 10, 12, 15, 18, 20]
hasil_soal_12 = list(filter(lambda x: x % 3 == 0 or x % 5 == 0, angka))

# ----------------------------------------------------------
# SOAL 13 - MENENGAH
# ----------------------------------------------------------
"""
Sortir list tuple berikut berdasarkan elemen kedua (index 1):
data = [(1, 5), (3, 2), (2, 8), (4, 1)]
Hasil yang diharapkan: [(4, 1), (3, 2), (1, 5), (2, 8)]
"""
# Jawaban Anda:
data = [(1, 5), (3, 2), (2, 8), (4, 1)]
hasil_soal_13 = sorted(data, key= lambda x: x[1])

# ----------------------------------------------------------
# SOAL 14 - MENENGAH
# ----------------------------------------------------------
"""
Gunakan lambda dengan map() dan filter() secara bersamaan:
1. Filter angka yang lebih besar dari 5
2. Kemudian kalikan setiap angka dengan 2
angka = [2, 4, 6, 8, 10, 12]
"""
# Jawaban Anda:
angka = [2, 4, 6, 8, 10, 12]
hasil_soal_14 = list(map(lambda x: x * 5, filter(lambda x: x > 5, angka)))

# ----------------------------------------------------------
# SOAL 15 - MENENGAH
# ----------------------------------------------------------
"""
Buatlah lambda function yang menerima satu parameter (angka) 
dan mengembalikan "Positif" jika angka > 0, "Negatif" jika 
angka < 0, dan "Nol" jika angka == 0.
Hint: Gunakan conditional expression dalam lambda.
"""
# Jawaban Anda:
soal_15 = lambda x: "Positif" if x > 0 else ("Negatif" if angka < 0 else "Nol")

print("\n" + "="*60)
print("     Selamat mengerjakan! Semoga berhasil! 🚀")
print("="*60)
