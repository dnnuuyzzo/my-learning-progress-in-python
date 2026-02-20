"""
===============================================
CLASS DAN OBJECT DI PYTHON
===============================================

OOP (Object-Oriented Programming) adalah paradigma pemrograman
yang mengorganisir kode ke dalam objek.
"""

# =====================================
# 1. MEMBUAT CLASS
# =====================================

class Mobil:
    pass  # Class kosong

# Membuat object (instance)
mobil1 = Mobil()
print(f"Type: {type(mobil1)}")

# =====================================
# 2. CONSTRUCTOR (__init__)
# =====================================

class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
    
    def perkenalan(self):
        print(f"Halo, saya {self.nama} dari {self.jurusan}")

mhs1 = Mahasiswa("Budi", "12345", "Informatika")
mhs2 = Mahasiswa("Ani", "12346", "Matematika")

print(f"Nama: {mhs1.nama}")
mhs1.perkenalan()
mhs2.perkenalan()

# =====================================
# 3. ATRIBUT DAN METHOD
# =====================================

class Persegi:
    # Class attribute
    jumlah_sisi = 4
    
    def __init__(self, panjang_sisi):
        # Instance attribute
        self.sisi = panjang_sisi
    
    # Instance method
    def hitung_luas(self):
        return self.sisi ** 2
    
    def hitung_keliling(self):
        return self.sisi * self.jumlah_sisi

p1 = Persegi(5)
print(f"Luas: {p1.hitung_luas()}")
print(f"Keliling: {p1.hitung_keliling()}")
print(f"Jumlah sisi: {Persegi.jumlah_sisi}")

# =====================================
# 4. ENCAPSULATION
# =====================================

class BankAccount:
    def __init__(self, nama, saldo_awal):
        self.nama = nama
        self._saldo = saldo_awal  # Protected (konvensi)
        self.__pin = "1234"       # Private (name mangling)
    
    def cek_saldo(self):
        return self._saldo
    
    def setor(self, jumlah):
        if jumlah > 0:
            self._saldo += jumlah
            return True
        return False
    
    def tarik(self, jumlah):
        if 0 < jumlah <= self._saldo:
            self._saldo -= jumlah
            return True
        return False

akun = BankAccount("Budi", 1000000)
print(f"Saldo awal: {akun.cek_saldo()}")
akun.setor(500000)
print(f"Setelah setor: {akun.cek_saldo()}")
akun.tarik(200000)
print(f"Setelah tarik: {akun.cek_saldo()}")

# =====================================
# 5. PROPERTY DECORATOR
# =====================================

class Lingkaran:
    def __init__(self, jari_jari):
        self._jari_jari = jari_jari
    
    @property
    def jari_jari(self):
        return self._jari_jari
    
    @jari_jari.setter
    def jari_jari(self, nilai):
        if nilai > 0:
            self._jari_jari = nilai
        else:
            raise ValueError("Jari-jari harus positif")
    
    @property
    def luas(self):
        return 3.14159 * self._jari_jari ** 2
    
    @property
    def keliling(self):
        return 2 * 3.14159 * self._jari_jari

lingkaran = Lingkaran(5)
print(f"Jari-jari: {lingkaran.jari_jari}")
print(f"Luas: {lingkaran.luas:.2f}")
lingkaran.jari_jari = 10
print(f"Luas baru: {lingkaran.luas:.2f}")

# =====================================
# 6. CLASS METHOD DAN STATIC METHOD
# =====================================

class Karyawan:
    jumlah_karyawan = 0
    
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji
        Karyawan.jumlah_karyawan += 1
    
    @classmethod
    def get_jumlah(cls):
        return cls.jumlah_karyawan
    
    @staticmethod
    def info_perusahaan():
        return "PT Python Indonesia"

k1 = Karyawan("Budi", 5000000)
k2 = Karyawan("Ani", 6000000)

print(f"Jumlah karyawan: {Karyawan.get_jumlah()}")
print(f"Perusahaan: {Karyawan.info_perusahaan()}")

# =====================================
# LATIHAN
# =====================================

"""
Latihan 1: Buat class Buku dengan atribut judul, penulis, tahun
Latihan 2: Buat class Segitiga dengan method hitung_luas
Latihan 3: Buat class TodoList dengan method add, remove, show
"""
