"""
===============================================
REGEX - REGULAR EXPRESSION
===============================================
"""

import re

# =====================================
# 1. PATTERN MATCHING DASAR
# =====================================

teks = "Nomor telepon saya 081234567890"

# search() - mencari pattern pertama
hasil = re.search(r'\d+', teks)
if hasil:
    print(f"Ditemukan: {hasil.group()}")

# findall() - mencari semua
angka = re.findall(r'\d+', "Harga: 100, Diskon: 20")
print(f"Semua angka: {angka}")

# =====================================
# 2. POLA REGEX UMUM
# =====================================

"""
\d - digit (0-9)
\w - word character (a-z, A-Z, 0-9, _)
\s - whitespace
.  - karakter apapun
^  - awal string
$  - akhir string
*  - 0 atau lebih
+  - 1 atau lebih
?  - 0 atau 1
{n} - tepat n kali
[abc] - salah satu dari a, b, c
(abc) - group
"""

# =====================================
# 3. VALIDASI EMAIL
# =====================================

def validasi_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

print(f"test@email.com valid: {validasi_email('test@email.com')}")
print(f"invalid-email valid: {validasi_email('invalid-email')}")

# =====================================
# 4. REPLACE DENGAN REGEX
# =====================================

teks = "Harga: 100 rupiah, Total: 500 rupiah"
hasil = re.sub(r'\d+', 'XXX', teks)
print(f"Setelah replace: {hasil}")

# =====================================
# 5. SPLIT DENGAN REGEX
# =====================================

teks = "apel,jeruk;mangga:pisang"
buah = re.split(r'[,;:]', teks)
print(f"Split: {buah}")

# =====================================
# 6. GROUPS
# =====================================

teks = "Nama: Budi, Umur: 25"
match = re.search(r'Nama: (\w+), Umur: (\d+)', teks)
if match:
    print(f"Nama: {match.group(1)}")
    print(f"Umur: {match.group(2)}")
