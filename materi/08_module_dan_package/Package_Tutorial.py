"""
============================================================
TUTORIAL LENGKAP: PYTHON PACKAGE, IMPORT, AS, & FROM
============================================================

Halo! Di sini kita akan belajar gimana cara kerja package di Python.
Bayangkan Package itu seperti FOLDER, dan Module itu seperti FILE .py di dalamnya.

------------------------------------------------------------
1. APA ITU __init__.py?
------------------------------------------------------------
- File ini WAJIB ada di dalam folder supaya Python tahu kalau folder itu adalah Package.
- Kalau tidak ada file ini, folder itu cuma folder biasa (Namespace Package di Python 3, tapi tetap disarankan ada).
- File ini akan dijalankan PERTAMA KALI saat package di-import.

------------------------------------------------------------
2. CARA IMPORT (Berbagai Variasi)
------------------------------------------------------------
"""

# --- CARA A: Import Standar (Import Seluruh Module) ---
# Format: import nama_package.nama_module
import package.matematika
import package.pesan

print("\n--- Menggunakan Cara A ---")
hasil = package.matematika.tambah(10, 5)
print(f"10 + 5 = {hasil}")
print(package.pesan.sapa("Danu"))


# --- CARA B: Menggunakan 'as' (Alias / Nama Samaran) ---
# Berguna kalau nama module-nya panjang atau mau disingkat.
import package.matematika as math
import package.pesan as msg

print("\n--- Menggunakan Cara B (as) ---")
print(f"PI: {math.constant_pi}")
print(msg.selamat_tinggal())


# --- CARA C: Menggunakan 'from' (Import Spesifik) ---
# Kita ambil yang kita butuhkan saja, jadi tidak perlu ngetik nama package lagi.
from package.matematika import kurang
from package.pesan import sapa

print("\n--- Menggunakan Cara C (from ... import ...) ---")
print(f"10 - 3 = {kurang(10, 3)}")
print(sapa("Programmer"))


# --- CARA D: Import dari __init__.py ---
# Karena di __init__.py kita sudah 'mengangkat' fungsi tambah ke level package,
# kita bisa langsung panggil dari package-nya.
import package

print("\n--- Menggunakan Cara D (Melalui __init__.py) ---")
# Fungsi 'tambah' sudah tersedia di namespace 'package' karena di-import di __init__.py
print(f"Tambah lewat package: {package.tambah(50, 50)}")


"""
============================================================
RINGKASAN SINGKAT:
1. 'import package.module' -> Harus panggil lengkap (package.module.fungsi)
2. 'import package as p'   -> Panggil pakai alias (p.fungsi)
3. 'from package import f' -> Panggil fungsinya langsung (f())
4. '__init__.py'          -> 'KTP' folder biar jadi Package + tempat inisialisasi.
============================================================
"""
