"""
===============================================
DICTIONARY DI PYTHON
===============================================

Dictionary adalah struktur data key-value yang:
- Mutable (bisa diubah)
- Key harus unik dan immutable
- Terurut (Python 3.7+)
"""

# =====================================
# 1. MEMBUAT DICTIONARY
# =====================================

dict_kosong = {}
mahasiswa = {"nama": "Budi", "umur": 20, "jurusan": "IT"}
print(f"mahasiswa: {mahasiswa}")

# Menggunakan dict()
person = dict(nama="Ani", umur=25)
print(f"person: {person}")

# =====================================
# 2. MENGAKSES NILAI
# =====================================

print(f"mahasiswa['nama']: {mahasiswa['nama']}")
print(f"mahasiswa.get('umur'): {mahasiswa.get('umur')}")
print(f"mahasiswa.get('alamat', 'Tidak ada'): {mahasiswa.get('alamat', 'Tidak ada')}")

# =====================================
# 3. MENAMBAH DAN MENGUBAH
# =====================================

mahasiswa["alamat"] = "Jakarta"  # Menambah
mahasiswa["umur"] = 21          # Mengubah
print(f"Setelah update: {mahasiswa}")

# update() untuk beberapa item
mahasiswa.update({"ipk": 3.5, "semester": 5})
print(f"Setelah update(): {mahasiswa}")

# =====================================
# 4. MENGHAPUS ITEM
# =====================================

del mahasiswa["semester"]        # Hapus dengan del
ipk = mahasiswa.pop("ipk")      # Hapus dan return nilai
print(f"Setelah hapus: {mahasiswa}")

# =====================================
# 5. DICTIONARY METHODS
# =====================================

data = {"a": 1, "b": 2, "c": 3}
print(f"keys(): {list(data.keys())}")
print(f"values(): {list(data.values())}")
print(f"items(): {list(data.items())}")

# =====================================
# 6. ITERASI DICTIONARY
# =====================================

print("\n=== Iterasi ===")
for key in data:
    print(f"Key: {key}, Value: {data[key]}")

for key, value in data.items():
    print(f"{key} = {value}")

# =====================================
# 7. DICTIONARY COMPREHENSION
# =====================================

kuadrat = {x: x**2 for x in range(1, 6)}
print(f"kuadrat: {kuadrat}")

# =====================================
# 8. NESTED DICTIONARY
# =====================================

siswa = {
    "s001": {"nama": "Budi", "nilai": 85},
    "s002": {"nama": "Ani", "nilai": 90}
}
print(f"Nama s001: {siswa['s001']['nama']}")

# =============================================================================
# LATIHAN DICTIONARY - 20 SOAL (4 TINGKAT KESULITAN)
# =============================================================================

"""
================================================================================
                    DAFTAR SOAL LATIHAN DICTIONARY
================================================================================

🟢 BASIC (1-5) - Dasar-dasar Dictionary
   1. Buat dictionary mahasiswa dengan key: nama, umur, jurusan
   2. Akses nilai 'nama' dari dictionary mahasiswa
   3. Tambahkan key 'alamat' ke dictionary mahasiswa
   4. Ubah nilai 'umur' menjadi 21
   5. Hapus key 'jurusan' menggunakan del

🟡 INTERMEDIATE (6-10) - Methods Dictionary
   6. Gunakan get() untuk akses key yang tidak ada dengan nilai default
   7. Print semua keys dari dictionary menggunakan .keys()
   8. Print semua values menggunakan .values()
   9. Print semua items (key-value pairs) menggunakan .items()
   10. Gunakan update() untuk menambah beberapa key sekaligus

🟠 ADVANCED (11-15) - Iterasi & Comprehension
   11. Loop dictionary dan print "key: value" untuk setiap item
   12. Buat dictionary kuadrat {1:1, 2:4, 3:9, ...} sampai 10 dengan comprehension
   13. Filter dictionary: hanya ambil item dengan value > 50
   14. Gabungkan dua dictionary menggunakan ** unpacking atau |
   15. Cek apakah key 'email' ada dalam dictionary

🔴 EXPERT (16-20) - Nested & Kompleks
   16. Buat nested dictionary untuk data 3 siswa (nama, nilai matematika, nilai ipa)
   17. Akses nilai matematika dari siswa kedua di nested dictionary
   18. Buat dictionary dari dua list: keys=["a","b","c"] dan values=[1,2,3]
   19. Invert dictionary: swap key dan value {1:"a",2:"b"} -> {"a":1,"b":2}
   20. Buat counter: hitung frekuensi huruf di kata "mississippi"

================================================================================
"""

print("\n" + "=" * 60)
print("LATIHAN DICTIONARY - Kerjakan di bawah ini!")
print("=" * 60)

# =============================================================================
# 🟢 BASIC (LEVEL 1-5)
# =============================================================================

# --- Soal 1 ---
print("\n📝 Soal 1: Buat dictionary mahasiswa")
# Tulis jawabanmu di bawah:
mahasiswa = {
   'nama':'Danuardi Saputro',
   'umur':20,
   'jurusan':'Teknik Informatika'
}

# --- Soal 2 ---
print("\n📝 Soal 2: Akses nilai 'nama'")
# Tulis jawabanmu di bawah:
nama_mahasiswa = mahasiswa['umur']

# --- Soal 3 ---
print("\n📝 Soal 3: Tambah key 'alamat'")
# Tulis jawabanmu di bawah:
mahasiswa['alamat'] = 'Tangerang Selatan'

# --- Soal 4 ---
print("\n📝 Soal 4: Ubah nilai 'umur'")
# Tulis jawabanmu di bawah:
mahasiswa['umur'] = 19

# --- Soal 5 ---
print("\n📝 Soal 5: Hapus key dengan del")
# Tulis jawabanmu di bawah:
del mahasiswa['jurusan']

# =============================================================================
# 🟡 INTERMEDIATE (LEVEL 6-10)
# =============================================================================

# --- Soal 6 ---
print("\n📝 Soal 6: Gunakan get() dengan default value")
# Tulis jawabanmu di bawah:
key_tidak_ada = mahasiswa.get('pekerjaan')

# --- Soal 7 ---
print("\n📝 Soal 7: Print semua keys")
# Tulis jawabanmu di bawah:
print(mahasiswa.keys())

# --- Soal 8 ---
print("\n📝 Soal 8: Print semua values")
# Tulis jawabanmu di bawah:
print(mahasiswa.values())

# --- Soal 9 ---
print("\n📝 Soal 9: Print semua items")
# Tulis jawabanmu di bawah:
print(mahasiswa.items())

# --- Soal 10 ---
print("\n📝 Soal 10: Gunakan update()")
# Tulis jawabanmu di bawah:
mahasiswa.update({"ipk":3.4, "akhlak":"baik"})

# =============================================================================
# 🟠 ADVANCED (LEVEL 11-15)
# =============================================================================

# --- Soal 11 ---
print("\n📝 Soal 11: Loop dictionary")
# Tulis jawabanmu di bawah:
for key in mahasiswa:
   print(f"{key} = {mahasiswa[key]}")

# --- Soal 12 ---
print("\n📝 Soal 12: Dictionary comprehension kuadrat 1-10")
# Tulis jawabanmu di bawah:
dictionary_comprehension = {i: i ** 2 for i in range(10)}

# --- Soal 13 ---
print("\n📝 Soal 13: Filter dictionary value > 50")
# Tulis jawabanmu di bawah:
dictionary_comprehension = {i: i ** 2 for i in range(10) if i ** 2 > 50}


# --- Soal 14 ---
print("\n📝 Soal 14: Gabungkan dua dictionary")
# Tulis jawabanmu di bawah:
dict_1 = {
   "nama": "Danuardi Saputro",
   "umur":20
}

dict_2 = {
   "universitas":"UIN JAKARTA",
   "status":"mahasiswa"
}

dict_gabungan = {**dict_1, **dict_2}

# --- Soal 15 ---
print("\n📝 Soal 15: Cek key exists")
# Tulis jawabanmu di bawah:
if "asal" in dict_gabungan:
   print("Ada")
else:
   print("Tidak ada")

# =============================================================================
# 🔴 EXPERT (LEVEL 16-20)
# =============================================================================

# --- Soal 16 ---
print("\n📝 Soal 16: Nested dictionary 3 siswa")
# Tulis jawabanmu di bawah:
mahasiswa = {
   "mahasiswa_1": {"nama":"Danu", "kelas":"C", "umur":20}
}

# --- Soal 17 ---
print("\n📝 Soal 17: Akses nested value")
# Tulis jawabanmu di bawah:


# --- Soal 18 ---
print("\n📝 Soal 18: Dict dari dua list")
keys = ["a", "b", "c"]
values = [1, 2, 3]
# Tulis jawabanmu di bawah:


# --- Soal 19 ---
print("\n📝 Soal 19: Invert dictionary")
# Tulis jawabanmu di bawah:


# --- Soal 20 ---
print("\n📝 Soal 20: Counter huruf 'mississippi'")
# Tulis jawabanmu di bawah:


print("\n" + "=" * 60)
print("Selesaikan semua soal di atas! 💪")
print("=" * 60)

