"""
===============================================
INHERITANCE DAN POLYMORPHISM
===============================================
"""

# =====================================
# 1. INHERITANCE (Pewarisan)
# =====================================

class Hewan:
    def __init__(self, nama):
        self.nama = nama
    
    def suara(self):
        return "Suara hewan"
    
    def info(self):
        return f"Ini adalah {self.nama}"

class Kucing(Hewan):
    def __init__(self, nama, warna):
        super().__init__(nama)  # Panggil constructor parent
        self.warna = warna
    
    def suara(self):  # Override method
        return "Meow!"

class Anjing(Hewan):
    def suara(self):
        return "Guk guk!"

kucing = Kucing("Kitty", "Putih")
anjing = Anjing("Buddy")

print(f"{kucing.nama} bersuara: {kucing.suara()}")
print(f"{anjing.nama} bersuara: {anjing.suara()}")
print(f"Warna kucing: {kucing.warna}")

# =====================================
# 2. MULTI-LEVEL INHERITANCE
# =====================================

class Kendaraan:
    def __init__(self, merk):
        self.merk = merk

class Mobil(Kendaraan):
    def __init__(self, merk, model):
        super().__init__(merk)
        self.model = model

class MobilSport(Mobil):
    def __init__(self, merk, model, top_speed):
        super().__init__(merk, model)
        self.top_speed = top_speed

sport = MobilSport("Ferrari", "F8", 340)
print(f"{sport.merk} {sport.model}, Top Speed: {sport.top_speed} km/h")

# =====================================
# 3. MULTIPLE INHERITANCE
# =====================================

class Terbang:
    def terbang(self):
        return "Sedang terbang!"

class Berenang:
    def berenang(self):
        return "Sedang berenang!"

class Bebek(Hewan, Terbang, Berenang):
    def suara(self):
        return "Kwek kwek!"

bebek = Bebek("Donald")
print(f"{bebek.nama}: {bebek.suara()}")
print(bebek.terbang())
print(bebek.berenang())

# MRO (Method Resolution Order)
print(f"MRO: {Bebek.__mro__}")

# =====================================
# 4. POLYMORPHISM
# =====================================

def buat_suara(hewan):
    """Fungsi yang menerima berbagai tipe hewan"""
    print(f"{hewan.nama} bersuara: {hewan.suara()}")

hewan_list = [
    Kucing("Kitty", "Putih"),
    Anjing("Buddy"),
    Bebek("Donald")
]

for hewan in hewan_list:
    buat_suara(hewan)

# =====================================
# 5. ABSTRACT CLASS
# =====================================

from abc import ABC, abstractmethod

class Bentuk(ABC):
    @abstractmethod
    def luas(self):
        pass
    
    @abstractmethod
    def keliling(self):
        pass

class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi
    
    def luas(self):
        return self.sisi ** 2
    
    def keliling(self):
        return 4 * self.sisi

class Lingkaran(Bentuk):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari
    
    def luas(self):
        return 3.14159 * self.jari_jari ** 2
    
    def keliling(self):
        return 2 * 3.14159 * self.jari_jari

# bentuk = Bentuk()  # Error: tidak bisa instantiate abstract class

persegi = Persegi(5)
lingkaran = Lingkaran(7)

print(f"Luas persegi: {persegi.luas()}")
print(f"Luas lingkaran: {lingkaran.luas():.2f}")

# =====================================
# 6. MAGIC METHODS (Dunder Methods)
# =====================================

class Vektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Vektor({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Vektor({self.x}, {self.y})"
    
    def __add__(self, other):
        return Vektor(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __len__(self):
        return int((self.x**2 + self.y**2)**0.5)

v1 = Vektor(3, 4)
v2 = Vektor(1, 2)
v3 = v1 + v2

print(f"v1: {v1}")
print(f"v1 + v2 = {v3}")
print(f"len(v1) = {len(v1)}")

# =====================================
# LATIHAN
# =====================================

"""
Latihan 1: Buat hierarki class: Pegawai -> Manager -> Direktur
Latihan 2: Buat abstract class Pembayaran dengan method bayar()
Latihan 3: Implementasikan __add__ untuk class Uang
"""
