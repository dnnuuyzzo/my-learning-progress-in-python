"""
===============================================
FILE HANDLING DI PYTHON
===============================================
"""

import os

# Pastikan folder output ada
os.makedirs("output", exist_ok=True)

# =====================================
# 1. MEMBUKA DAN MEMBACA FILE
# =====================================

# Mode membuka file:
# 'r' - Read (default)
# 'w' - Write (overwrite)
# 'a' - Append
# 'x' - Create (error jika sudah ada)
# 'b' - Binary mode
# 't' - Text mode (default)

# Membuat file contoh
with open("output/contoh.txt", "w") as f:
    f.write("Baris pertama\n")
    f.write("Baris kedua\n")
    f.write("Baris ketiga\n")

# Cara 1: Baca seluruh isi
with open("output/contoh.txt", "r") as file:
    isi = file.read()
    print("=== Seluruh isi ===")
    print(isi)

# Cara 2: Baca per baris
with open("output/contoh.txt", "r") as file:
    print("=== Per baris ===")
    for baris in file:
        print(baris.strip())

# Cara 3: Baca semua baris ke list
with open("output/contoh.txt", "r") as file:
    baris_list = file.readlines()
    print(f"=== List baris ===\n{baris_list}")

# =====================================
# 2. MENULIS KE FILE
# =====================================

# Write mode (overwrite)
with open("output/hasil.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Python File Handling\n")

# Append mode
with open("output/hasil.txt", "a") as file:
    file.write("Baris tambahan\n")

# Menulis list
baris = ["Satu\n", "Dua\n", "Tiga\n"]
with open("output/list.txt", "w") as file:
    file.writelines(baris)

print("File berhasil ditulis!")

# =====================================
# 3. CONTEXT MANAGER (with)
# =====================================

# Dengan 'with', file otomatis ditutup meskipun ada error
# Ini cara yang DIREKOMENDASIKAN

with open("output/contoh.txt", "r") as f:
    data = f.read()
    # File otomatis ditutup setelah blok selesai

# Tanpa 'with' (tidak direkomendasikan)
# f = open("contoh.txt", "r")
# data = f.read()
# f.close()  # Harus ditutup manual

# =====================================
# 4. BEKERJA DENGAN PATH
# =====================================

# Cek file ada
print(f"\ncontoh.txt ada: {os.path.exists('output/contoh.txt')}")

# Mendapatkan direktori saat ini
print(f"Direktori saat ini: {os.getcwd()}")

# Bergabung path dengan aman
path = os.path.join("output", "subfolder", "file.txt")
print(f"Path gabungan: {path}")

# =====================================
# 5. EXCEPTION HANDLING UNTUK FILE
# =====================================

try:
    with open("file_tidak_ada.txt", "r") as f:
        isi = f.read()
except FileNotFoundError:
    print("\nFile tidak ditemukan!")
except PermissionError:
    print("\nTidak punya izin akses!")
except Exception as e:
    print(f"\nError: {e}")

# =====================================
# 6. MEMBACA FILE CSV SEDERHANA
# =====================================

# Membuat CSV sederhana
with open("output/data.csv", "w") as f:
    f.write("nama,umur,kota\n")
    f.write("Budi,25,Jakarta\n")
    f.write("Ani,22,Bandung\n")
    f.write("Cici,28,Surabaya\n")

# Membaca CSV sederhana
print("\n=== Data CSV ===")
with open("output/data.csv", "r") as f:
    header = f.readline().strip().split(",")
    print(f"Header: {header}")
    
    for baris in f:
        data = baris.strip().split(",")
        print(f"  {data}")

# =====================================
# 7. COPY FILE
# =====================================

import shutil

# Copy file
shutil.copy("output/contoh.txt", "output/contoh_backup.txt")
print("\nFile berhasil di-copy!")

# =====================================
# LATIHAN
# =====================================

"""
Latihan 1: Buat program untuk menghitung jumlah baris dalam file
Latihan 2: Buat program untuk mencari kata tertentu dalam file
Latihan 3: Buat program untuk menggabungkan beberapa file text
"""
