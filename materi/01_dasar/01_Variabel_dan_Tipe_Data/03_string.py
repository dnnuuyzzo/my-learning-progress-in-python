"""
===============================================
STRING DI PYTHON
===============================================

String adalah urutan karakter yang diapit oleh tanda kutip.
Bisa menggunakan kutip tunggal ('...'), ganda ("..."), atau tiga ("..." / '...')
"""

# =====================================
# 1. MEMBUAT STRING
# =====================================

# Menggunakan kutip tunggal
str1 = 'Hello, World!'

# Menggunakan kutip ganda
str2 = "Hello, Python!"

# Menggunakan kutip tiga (untuk multi-line)
str3 = """Ini adalah
string
multi-baris"""

str4 = '''Ini juga
multi-baris'''

print(str1)
print(str2)
print(str3)

# =====================================
# 2. ESCAPE CHARACTERS
# =====================================

print("\n=== Escape Characters ===")
print("Hello\tWorld")    # Tab
print("Hello\nWorld")    # Newline
print("Hello\\World")    # Backslash
print("Hello\"World\"")  # Kutip ganda
print('Hello\'World\'')  # Kutip tunggal

# Raw string (mengabaikan escape characters)
print(r"C:\Users\nama\folder")

# =====================================
# 3. STRING INDEXING
# =====================================

teks = "Python"
#       012345  (index positif)
#      -6-5-4-3-2-1 (index negatif)

print("\n=== String Indexing ===")
print(f"teks = '{teks}'")
print(f"teks[0] = '{teks[0]}'")   # P (karakter pertama)
print(f"teks[1] = '{teks[1]}'")   # y
print(f"teks[-1] = '{teks[-1]}'") # n (karakter terakhir)
print(f"teks[-2] = '{teks[-2]}'") # o

# =====================================
# 4. STRING SLICING
# =====================================

teks = "Hello, Python!"

print("\n=== String Slicing ===")
print(f"teks = '{teks}'")
print(f"teks[0:5] = '{teks[0:5]}'")    # Hello
print(f"teks[7:] = '{teks[7:]}'")      # Python!
print(f"teks[:5] = '{teks[:5]}'")      # Hello
print(f"teks[-7:-1] = '{teks[-7:-1]}'")# Python
print(f"teks[::2] = '{teks[::2]}'")    # Setiap karakter ke-2
print(f"teks[::-1] = '{teks[::-1]}'")  # Reverse string

# =====================================
# 5. STRING METHODS
# =====================================

teks = "  Hello, Python World!  "

print("\n=== String Methods ===")
print(f"Original: '{teks}'")
print(f"strip(): '{teks.strip()}'")       # Hapus spasi di awal/akhir
print(f"lower(): '{teks.lower()}'")       # Huruf kecil semua
print(f"upper(): '{teks.upper()}'")       # Huruf besar semua
print(f"title(): '{teks.title()}'")       # Huruf kapital setiap kata
print(f"capitalize(): '{teks.capitalize()}'")  # Kapital huruf pertama saja

teks2 = "Hello, Python!"
print(f"\nteks2 = '{teks2}'")
print(f"replace('Python', 'World'): '{teks2.replace('Python', 'World')}'")
print(f"split(','): {teks2.split(',')}")  # Split menjadi list
print(f"find('Python'): {teks2.find('Python')}")  # Index kemunculan
print(f"count('l'): {teks2.count('l')}")  # Hitung kemunculan

# =====================================
# 6. STRING FORMATTING
# =====================================

nama = "Budi"
umur = 25
tinggi = 175.5

print("\n=== String Formatting ===")

# Metode 1: Concatenation (+)
print("Nama: " + nama + ", Umur: " + str(umur))

# Metode 2: % operator (old style)
print("Nama: %s, Umur: %d" % (nama, umur))

# Metode 3: format() method
print("Nama: {}, Umur: {}".format(nama, umur))
print("Nama: {0}, Umur: {1}, Nama lagi: {0}".format(nama, umur))
print("Nama: {n}, Umur: {u}".format(n=nama, u=umur))

# Metode 4: f-string (recommended, Python 3.6+)
print(f"Nama: {nama}, Umur: {umur}")
print(f"Tinggi: {tinggi:.1f} cm")  # 1 angka desimal
print(f"Tahun lahir: {2024 - umur}")  # Bisa hitung di dalam f-string

# Format angka
angka = 1234567.89
print(f"Format angka: {angka:,.2f}")  # 1,234,567.89
print(f"Persen: {0.857:.2%}")  # 85.70%
print(f"Padding: {42:05d}")  # 00042

# =====================================
# 7. STRING OPERATIONS
# =====================================

str1 = "Hello"
str2 = "World"

print("\n=== String Operations ===")
# Concatenation
print(f"Concatenation: {str1 + ' ' + str2}")

# Repetition
print(f"Repetition: {str1 * 3}")

# Membership
print(f"'ell' in '{str1}': {'ell' in str1}")
print(f"'xyz' in '{str1}': {'xyz' in str1}")

# Length
print(f"len('{str1}'): {len(str1)}")

# =====================================
# 8. STRING CHECKING METHODS
# =====================================

print("\n=== String Checking Methods ===")
print(f"'123'.isdigit(): {'123'.isdigit()}")      # True
print(f"'abc'.isalpha(): {'abc'.isalpha()}")      # True
print(f"'abc123'.isalnum(): {'abc123'.isalnum()}")# True
print(f"'   '.isspace(): {'   '.isspace()}")     # True
print(f"'Hello'.startswith('He'): {'Hello'.startswith('He')}")
print(f"'Hello'.endswith('lo'): {'Hello'.endswith('lo')}")

# =====================================
# 9. JOIN DAN SPLIT
# =====================================

print("\n=== Join dan Split ===")

# Split - memecah string menjadi list
kalimat = "apel,jeruk,mangga,pisang"
buah_list = kalimat.split(",")
print(f"Split: {buah_list}")

# Join - menggabungkan list menjadi string
buah_list = ["apel", "jeruk", "mangga", "pisang"]
gabungan = ", ".join(buah_list)
print(f"Join: {gabungan}")

# =============================================================================
# LATIHAN STRING - 20 SOAL (4 TINGKAT KESULITAN)
# =============================================================================

"""
================================================================================
                        DAFTAR SOAL LATIHAN STRING
================================================================================

🟢 BASIC (1-5) - Dasar-dasar String
   1. Buat string dengan kutip tunggal, ganda, dan tiga. Print semua.
   2. Ambil 5 karakter pertama dari "Pemrograman Python"
   3. Ambil karakter terakhir dari "Hello World" menggunakan index negatif
   4. Cari panjang string "Belajar Python Itu Menyenangkan"
   5. Gabungkan "Hello" dan "World" dengan spasi di tengah

🟡 INTERMEDIATE (6-10) - String Methods
   6. Ubah "hello world" menjadi "Hello World" (Title Case)
   7. Ubah "Python Programming" menjadi huruf kecil semua
   8. Hapus spasi di awal dan akhir dari "   Hello World   "
   9. Ganti kata "Python" dengan "Java" dalam "I love Python programming"
   10. Pecah "apel,jeruk,mangga,pisang" menjadi list menggunakan split()

🟠 ADVANCED (11-15) - Slicing & Formatting
   11. Balikkan string "Hello" menggunakan slicing [::-1]
   12. Ambil setiap karakter ke-2 dari "Programming" (step slicing)
   13. Hitung berapa kali huruf 'a' muncul dalam "banana"
   14. Buat f-string: "Nama: {nama}, Umur: {umur} tahun, Gaji: Rp {gaji:,.0f}"
   15. Cek apakah "Python" ada dalam kalimat "I love Python" menggunakan 'in'

🔴 EXPERT (16-20) - Tantangan String
   16. Validasi email: cek apakah string mengandung '@' dan '.'
   17. Ekstrak domain dari email "user@example.com" (ambil setelah @)
   18. Buat program yang mengecek apakah string adalah palindrome (misal: "katak")
   19. Format angka 1234567.89 menjadi "Rp 1,234,567.89"
   20. Buat template surat dengan placeholder: {nama}, {tanggal}, {pesan}

================================================================================
"""

print("\n" + "=" * 60)
print("LATIHAN STRING - Kerjakan di bawah ini!")
print("=" * 60)

# =============================================================================
# 🟢 BASIC (LEVEL 1-5)
# =============================================================================

# --- Soal 1 ---
print("\n📝 Soal 1: Buat string dengan kutip tunggal, ganda, dan tiga")
# Tulis jawabanmu di bawah:


# --- Soal 2 ---
print("\n📝 Soal 2: Ambil 5 karakter pertama dari 'Pemrograman Python'")
# Tulis jawabanmu di bawah:


# --- Soal 3 ---
print("\n📝 Soal 3: Ambil karakter terakhir dari 'Hello World'")
# Tulis jawabanmu di bawah:


# --- Soal 4 ---
print("\n📝 Soal 4: Cari panjang 'Belajar Python Itu Menyenangkan'")
# Tulis jawabanmu di bawah:


# --- Soal 5 ---
print("\n📝 Soal 5: Gabungkan 'Hello' dan 'World' dengan spasi")
# Tulis jawabanmu di bawah:


# =============================================================================
# 🟡 INTERMEDIATE (LEVEL 6-10)
# =============================================================================

# --- Soal 6 ---
print("\n📝 Soal 6: Ubah 'hello world' ke Title Case")
# Tulis jawabanmu di bawah:


# --- Soal 7 ---
print("\n📝 Soal 7: Ubah 'Python Programming' ke lowercase")
# Tulis jawabanmu di bawah:


# --- Soal 8 ---
print("\n📝 Soal 8: Hapus spasi dari '   Hello World   '")
# Tulis jawabanmu di bawah:


# --- Soal 9 ---
print("\n📝 Soal 9: Ganti 'Python' dengan 'Java' dalam kalimat")
# Tulis jawabanmu di bawah:


# --- Soal 10 ---
print("\n📝 Soal 10: Split 'apel,jeruk,mangga,pisang' menjadi list")
# Tulis jawabanmu di bawah:


# =============================================================================
# 🟠 ADVANCED (LEVEL 11-15)
# =============================================================================

# --- Soal 11 ---
print("\n📝 Soal 11: Balikkan string 'Hello'")
# Tulis jawabanmu di bawah:


# --- Soal 12 ---
print("\n📝 Soal 12: Ambil setiap karakter ke-2 dari 'Programming'")
# Tulis jawabanmu di bawah:


# --- Soal 13 ---
print("\n📝 Soal 13: Hitung huruf 'a' dalam 'banana'")
# Tulis jawabanmu di bawah:


# --- Soal 14 ---
print("\n📝 Soal 14: Buat f-string dengan nama, umur, gaji")
# Tulis jawabanmu di bawah:


# --- Soal 15 ---
print("\n📝 Soal 15: Cek apakah 'Python' ada dalam 'I love Python'")
# Tulis jawabanmu di bawah:


# =============================================================================
# 🔴 EXPERT (LEVEL 16-20)
# =============================================================================

# --- Soal 16 ---
print("\n📝 Soal 16: Validasi email (ada '@' dan '.')")
# Tulis jawabanmu di bawah:


# --- Soal 17 ---
print("\n📝 Soal 17: Ekstrak domain dari 'user@example.com'")
# Tulis jawabanmu di bawah:


# --- Soal 18 ---
print("\n📝 Soal 18: Cek palindrome untuk 'katak'")
# Tulis jawabanmu di bawah:


# --- Soal 19 ---
print("\n📝 Soal 19: Format 1234567.89 menjadi 'Rp 1,234,567.89'")
# Tulis jawabanmu di bawah:


# --- Soal 20 ---
print("\n📝 Soal 20: Template surat dengan placeholder")
# Tulis jawabanmu di bawah:


print("\n" + "=" * 60)
print("Selesaikan semua soal di atas! 💪")
print("=" * 60)
