"""
File: __init__.py
File ini sangat penting! 
Fungsinya adalah untuk menandakan bahwa folder ini adalah sebuah 'Package' Python.

Apa saja yang bisa dilakukan di sini?
1. Inisialisasi: Kode di sini akan dijalankan saat package di-import.
2. Mempermudah import: Kita bisa mengekspos fungsi dari module di dalam ke level package.
"""

print("--- Package 'package' berhasil dipanggil! ---")

# Contoh mengekspos fungsi agar bisa diakses langsung dari 'package'
# Jadi daripada: import package.matematika
# Kita bisa: from package import tambah (setelah baris di bawah ini ditambahkan)
from .matematika import tambah, kurang
from .pesan import sapa
