"""
PANDUAN DECORATOR BAWAAN PYTHON (VERSI SUPER LENGKAP)
=====================================================
File ini berisi penjelasan mendalam tentang decorator bawaan Python.
Setiap topik akan memiliki:
1. Perbandingan (Tanpa Decorator vs Dengan Decorator)
2. Contoh Tambahan (Real-world use case)

Topik: @property, @staticmethod, @classmethod, @dataclass, @wraps, @lru_cache
"""

import functools
import time
from dataclasses import dataclass
from functools import lru_cache, wraps
from datetime import datetime

# ==============================================================================
# 1. @property (The Elegant Getter/Setter)
# ==============================================================================
print("\n" + "="*50)
print("1. @property - MENGELOLA AKSES ATRIBUT")
print("="*50)

# --- A. Tanpa @property (Gaya Lama) ---
class RekeningLama:
    def __init__(self, saldo):
        self._saldo = saldo # Disembunyikan secara konvensi

    def get_saldo(self):
        return f"Rp{self._saldo}"

    def set_saldo(self, nilai):
        if nilai < 0:
            print("Gagal: Saldo tidak boleh negatif!")
        else:
            self._saldo = nilai

print("\n[Tanpa @property]")
r_lama = RekeningLama(1000)
r_lama.set_saldo(2000) # Harus panggil fungsi
print(f"Saldo: {r_lama.get_saldo()}") 

# --- B. Dengan @property (Gaya Pythonic - Contoh 1) ---
class RekeningBaru:
    def __init__(self, saldo):
        self._saldo = saldo

    @property # Ini GETTER
    def saldo(self):
        return f"Rp{self._saldo}"

    @saldo.setter # Ini SETTER
    def saldo(self, nilai):
        if nilai < 0:
            print("Gagal: Saldo tidak boleh negatif!")
        else:
            self._saldo = nilai

print("\n[Dengan @property - Contoh 1]")
r_baru = RekeningBaru(1000)
r_baru.saldo = 5000 # Terlihat seperti variabel biasa, tapi validasi jalan!
print(f"Saldo: {r_baru.saldo}")

# --- C. Contoh 2: Property Read-Only (Hanya Lihat) ---
class Lingkaran:
    def __init__(self, radius):
        self.radius = radius

    @property
    def luas(self):
        # User tidak bisa mengubah luas secara langsung, hanya bergantung radius
        return 3.14 * (self.radius ** 2)
        

print("\n[Dengan @property - Contoh 2]")
lingkaran = Lingkaran(7)
print(f"Radius: {lingkaran.radius} -> Luas: {lingkaran.luas}")


# ==============================================================================
# 2. @staticmethod & 3. @classmethod
# ==============================================================================
print("\n" + "="*50)
print("2 & 3. @staticmethod & @classmethod")
print("="*50)

# --- A. Tanpa Decorator (Panggil Instance Method) ---
class KalkulatorLama:
    def tambah(self, a, b): # Harus bikin object dulu buat panggil ini
        return a + b

print("\n[Tanpa Decorator]")
k_lama = KalkulatorLama()
print(f"1 + 1 = {k_lama.tambah(1, 1)}")

# --- B. Dengan Decorator (Contoh 1: Staticmethod) ---
class Kalkulator:
    @staticmethod
    def kali(a, b): # Tidak butuh 'self' (object) atau 'cls' (class)
        return a * b

print("\n[Staticmethod - Contoh 1]")
print(f"5 x 5 = {Kalkulator.kali(5, 5)}") # Panggil langsung dari Class!

# --- C. Dengan Decorator (Contoh 2: Classmethod sebagai Factory) ---
class User:
    def __init__(self, nama, email):
        self.nama = nama
        self.email = email

    @classmethod
    def dari_string(cls, data_str):
        # Mengonversi string "nama,email" menjadi Object User
        nama, email = data_str.split(",")
        return cls(nama, email)

print("\n[Classmethod - Contoh 2]")
u = User.dari_string("Danu,danu@mail.com")
print(f"User: {u.nama} ({u.email})")


# ==============================================================================
# 4. @dataclass (Simpel & Cepat)
# ==============================================================================
print("\n" + "="*50)
print("4. @dataclass - BOILERPLATE KILLER")
print("="*50)

# --- A. Tanpa @dataclass (Melelahkan) ---
class BarangLama:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
    def __repr__(self): # Supaya pas di-print gak muncul <__main__.Barang object...>
        return f"BarangLama(nama='{self.nama}', harga={self.harga})"

print("\n[Tanpa @dataclass]")
b1 = BarangLama("Kopi", 5000)
print(b1)

# --- B. Dengan @dataclass (Contoh 1) ---
@dataclass
class BarangBaru:
    nama: str
    harga: int

print("\n[Dengan @dataclass - Contoh 1]")
b2 = BarangBaru("Teh", 3000)
print(b2) # Otomatis dapet tampilan bagus tanpa bikin __repr__!

# --- C. Contoh 2: Default Nilai & Logic ---
@dataclass
class Hero:
    nama: str
    health: int = 100
    level: int = 1

print("\n[Dengan @dataclass - Contoh 2]")
h = Hero("Zilong")
print(h)


# ==============================================================================
# 5. @wraps (Pelindung Identitas Fungsi)
# ==============================================================================
print("\n" + "="*50)
print("5. @wraps - IDENTITY PROTECTOR")
print("="*50)

# --- A. Tanpa @wraps (Masalah Identitas) ---
def log_tanpa_wraps(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@log_tanpa_wraps
def rahasia():
    """Dokumentasi fungsi rahasia."""
    pass

print("\n[Tanpa @wraps]")
print(f"Nama fungsi: {rahasia.__name__}") # Ups! Jadi 'wrapper'

# --- B. Dengan @wraps (Contoh 1) ---
def log_pake_wraps(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Log: Memanggil {func.__name__}...")
        return func(*args, **kwargs)
    return wrapper

@log_pake_wraps
def tambah(a, b):
    return a + b

print("\n[Dengan @wraps - Contoh 1]")
print(f"Nama fungsi: {tambah.__name__}") # Tetap 'tambah'!

# --- C. Contoh 2: Menjaga Docstring (Penjelasan Fungsi) ---
@log_pake_wraps
def fungsi_penting():
    """Ini docstring yang sangat penting."""
    pass

print("\n[With @wraps - Contoh 2]")
print(f"Docstring: {fungsi_penting.__doc__}")


# ==============================================================================
# 6. @lru_cache (Penyimpan Memori / Cache)
# ==============================================================================
print("\n" + "="*50)
print("6. @lru_cache - SPEED BOOSTER")
print("="*50)

# --- A. Tanpa @lru_cache (Lambat) ---
def fibo_lambat(n):
    if n < 2: return n
    return fibo_lambat(n-1) + fibo_lambat(n-2)

print("\n[Tanpa @lru_cache]")
print("Menghitung Fibonacci 30... (Tunggu sebentar)")
start = time.time()
fibo_lambat(30)
print(f"Waktu: {time.time() - start:.4f} detik")

# --- B. Dengan @lru_cache (Contoh 1) ---
@lru_cache(maxsize=None)
def fibo_cepat(n):
    if n < 2: return n
    return fibo_cepat(n-1) + fibo_cepat(n-2)

print("\n[Dengan @lru_cache - Contoh 1]")
start = time.time()
fibo_cepat(30)
print(f"Waktu: {time.time() - start:.4f} detik (Instan!)")

# --- C. Contoh 2: Fungsi Berat (Simulasi Download/Proses) ---
@lru_cache(maxsize=32)
def ambil_data_berat(user_id):
    print(f"  > Mengambil data user {user_id} dari 'database'...")
    time.sleep(1) # Pura-puranya lama
    return {"id": user_id, "status": "Aktif"}

print("\n[Dengan @lru_cache - Contoh 2]")
ambil_data_berat(1) # Pertama kali bakal lambat
ambil_data_berat(1) # Kedua kali bakal instan!


# ==============================================================================
# TANTANGAN / LATIHAN (15 SOAL)
# ==============================================================================
"""
--- LEVEL: MUDAH ---

1. [PROPERTIES] Buat class `Rekening` dengan atribut `_saldo`. Gunakan @property 
   untuk mengambil saldo dan setter untuk menambah saldo. Pastikan di setter 
   tidak bisa memasukkan angka negatif.

2. [DATACLASS] Buat dataclass `Produk` yang punya nama, harga, dan stok. 
   Tambahkan method di dalamnya untuk menghitung total nominal stok (harga * stok).

3. [STATICMETHOD] Buat class `Kalkulator` yang punya @staticmethod `tambah` dan `kali`.

4. [WRAPS] Buat decorator custom `@hitung_panggilan` yang mengeprint "Fungsi X dipanggil" 
   setiap kali dijalankan. Pastikan identitas fungsi tetap terjaga pakai `@wraps`.

5. [LRU_CACHE] Gunakan `@lru_cache` pada fungsi `faktorial(n)`. Bandingkan hasilnya 
   saat dipanggil berulang kali.

--- LEVEL: SEDANG ---

6. [DATACLASS] Buat dataclass `Siswa` dengan atribut: nama (str), umur (int), 
   dan nilai (list of int). Tambahkan method `rata_rata()` untuk menghitung rata-rata nilai.

7. [PROPERTIES] Buat class `Lingkaran` yang menerima `radius`. Berikan property 
   `luas` yang menghitung (3.14 * r * r). Luas ini harus READ-ONLY (tidak punya setter).

8. [CLASSMETHOD] Buat class `User`. Punya atribut `username` dan `email`. 
   Buat classmethod `dari_string(data_str)` yang menerima input "danu,danu@mail.com" 
   dan mengembalikan object User.

9. [LRU_CACHE] Buat fungsi `get_data_api(id)` yang pura-puranya mengambil data dari internet 
   (pakai time.sleep(2)). Gunakan cache supaya kalau ID yang sama dipanggil, gak nunggu lagi.

10. [PROPERTIES] Buat class `Suhu`. Simpan dalam `_celsius`. Buat property `fahrenheit`.
    Jika kita SET `fahrenheit`, dia otomatis mengonversi dan menyimpan nilainya ke `_celsius`.

--- LEVEL: SULIT ---

11. [DATACLASS + PROPERTIES] Buat dataclass `PersegiPanjang` dengan `panjang` dan `lebar`.
    Tambahkan property `apakah_persegi` yang mengembalikan True jika panjang == lebar.

12. [CLASSMETHOD] Buat class `Database`. Gunakan classmethod untuk membuat "Koneksi" 
    yang berbeda, misalnya `Database.sebagai_admin()` dan `Database.sebagai_user()`.

13. [STATICMETHOD] Buat class `Validator` dengan staticmethod `cek_email(email)` 
    dan `cek_password(pw)`. Password minimal 8 karakter.

14. [COMBINATION] Buat class `Perpustakaan`. Gunakan @classmethod untuk inisialisasi 
    perpustakaan dengan koleksi buku default ("Python 101", "Data Science"). 
    Gunakan @staticmethod untuk mengecek apakah ID Buku valid (misal: harus diawali "LIB-").

15. [ADVANCED LRU] Implementasikan fungsi rekursif `fibonacci(n)` dengan `@lru_cache`. 
    Coba hitung `fibonacci(50)`. Tanpa cache ini akan sangat lama, dengan cache akan instan!
"""

print("\n" + "="*50)
print("SIAP UNTUK LATIHAN? 🚀")
print("Kerjakan 15 soal di atas di bawah ini!")
print("="*50)

# --- TEMPAT MENCOBA LATIHAN ---

# 1. [PROPERTIES] Buat class `Rekening` dengan atribut `_saldo`. Gunakan @property untuk mengambil saldo dan setter untuk menambah saldo. Pastikan di setter tidak bisa memasukkan angka negatif.

class Rekening:
    def __init__(self, saldo):
        self._saldo = saldo
    
    @property
    def saldo(self):
        return "Rp {:,}".format(self._saldo)

    @saldo.setter
    def saldo(self, nilai):
        if nilai < 0:
            print("Tidak boleh negatif")
        else:
            self._saldo = nilai

# 2. [DATACLASS] Buat dataclass `Produk` yang punya nama, harga, dan stok. Tambahkan method di dalamnya untuk menghitung total nominal stok (harga * stok).

@dataclass
class Produk:
    _nama : str
    _harga : float
    _stok : int = 1

    @property
    def total_nominal(self):
        return self._harga * self._stok

# 3. [STATICMETHOD] Buat class `Kalkulator` yang punya @staticmethod `tambah` dan `kali`.
class Kalkulator:
    @staticmethod
    def tambah(*args):
        hasil = 0
        for x in args:
            hasil += x
        return hasil

    @staticmethod
    def kali(*args):
        hasil = 1
        for x in args:
            hasil *= x
        return hasil

# 4. [WRAPS] Buat decorator custom `@hitung_panggilan` yang mengeprint "Fungsi X dipanggil" setiap kali dijalankan. Pastikan identitas fungsi tetap terjaga pakai `@wraps`.

def hitung_panggilan(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Fungsi {func.__name__} dipanggil")
        count += 1
    return wrapper

# 5. [LRU_CACHE] Gunakan `@lru_cache` pada fungsi `faktorial(n)`. Bandingkan hasilnya saat dipanggil berulang kali.

@lru_cache(maxsize=None)
def faktorial(n):
    if n < 1: return n
    return n * faktorial(n-1)

# 6. [DATACLASS] Buat dataclass `Siswa` dengan atribut: nama (str), umur (int), dan nilai (list of int). Tambahkan method `rata_rata()` untuk menghitung rata-rata nilai.

@dataclass
class Siswa:
    nama: str
    umur: int
    nilai: list[int]

    def rata_rata(self):
        if not self.nilai: return 0
        return sum(self.nilai) / len(self.nilai)

# 7. [PROPERTIES] Buat class `Lingkaran` yang menerima `radius`. Berikan property `luas` yang menghitung (3.14 * r * r). Luas ini harus READ-ONLY (tidak punya setter).

@dataclass
class Lingkaran:
    _radius: int
    @property
    def luas(self):
        return 3.14 * self._radius ** 2

# 8. [CLASSMETHOD] Buat class `User`. Punya atribut `username` dan `email`. Buat classmethod `dari_string(data_str)` yang menerima input "danu,danu@mail.com" dan mengembalikan object User.

class User:
    def __init__(self, username, email):
        self._username = username
        self._email = email

    @classmethod
    def dari_string(cls, data_str):
        username, email = data_str.split(",")
        return cls(username, email)

# 9. [LRU_CACHE] Buat fungsi `get_data_api(id)` yang pura-puranya mengambil data dari internet (pakai time.sleep(2)). Gunakan cache supaya kalau ID yang sama dipanggil, gak nunggu lagi.

from functools import lru_cache

@lru_cache
def get_data_api(id):
    time.sleep(2)
    return {
        "id":id,
        "status":"Aktif"
    }

# 10. [PROPERTIES] Buat class `Suhu`. Simpan dalam `_celsius`. Buat property `fahrenheit`.Jika kita SET `fahrenheit`, dia otomatis mengonversi dan menyimpan nilainya ke `_celsius`.

class Suhu:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        return (9/5) * self._celsius + 32

    @fahrenheit.setter
    def fahrenheit(self, input):
        self._celsius = (imput - 32) * 5/9