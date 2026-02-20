# ============================================================================
#                    INHERITANCE (PEWARISAN) DI PYTHON
#                     Materi Super Lengkap untuk Pemula
# ============================================================================

# ============================================================================
# BAGIAN 1: APA ITU INHERITANCE?
# ============================================================================
"""
Inheritance (Pewarisan) adalah salah satu pilar utama OOP (Object-Oriented
Programming). Inheritance memungkinkan sebuah class (kelas anak/child) untuk
MEWARISI atribut dan method dari class lain (kelas induk/parent).

Analogi Sederhana:
- Bayangkan kamu punya "Kendaraan" sebagai kategori umum (Parent Class)
- "Mobil", "Motor", "Truk" adalah jenis spesifik dari Kendaraan (Child Class)
- Semua kendaraan punya roda, mesin, bisa berjalan → ini DIWARISKAN
- Tapi mobil punya pintu, motor punya stang → ini UNIK per child class

Manfaat Inheritance:
1. REUSABILITY   → Tidak perlu menulis ulang kode yang sama
2. ORGANISASI    → Kode lebih terstruktur dan rapi
3. EXTENSIBILITY → Mudah menambah fitur baru
4. MAINTAINABILITY → Mudah dipelihara dan di-update
"""


# ============================================================================
# BAGIAN 2: SYNTAX DASAR INHERITANCE
# ============================================================================
print("=" * 60)
print("BAGIAN 2: SYNTAX DASAR INHERITANCE")
print("=" * 60)

# --- Parent Class (Kelas Induk / Base Class / Super Class) ---
class Hewan:
    """Ini adalah Parent Class / Base Class"""

    def __init__(self, nama, suara):
        self.nama = nama      # atribut instance
        self.suara = suara

    def bersuara(self):
        print(f"{self.nama} berbunyi: {self.suara}!")

    def info(self):
        print(f"Saya adalah {self.nama}")


# --- Child Class (Kelas Anak / Derived Class / Sub Class) ---
# Cara mewarisi: tulis nama Parent di dalam kurung ()
class Kucing(Hewan):
    """Ini adalah Child Class yang mewarisi dari Hewan"""
    pass  # pass = tidak menambah apa-apa, murni warisan


# Penggunaan:
kucing = Kucing("Kitty", "Meow")  # __init__ dari Hewan dipakai
kucing.bersuara()   # Output: Kitty berbunyi: Meow!
kucing.info()       # Output: Saya adalah Kitty
print()


# ============================================================================
# BAGIAN 3: MENAMBAHKAN ATRIBUT & METHOD DI CHILD CLASS
# ============================================================================
print("=" * 60)
print("BAGIAN 3: MENAMBAHKAN ATRIBUT & METHOD DI CHILD CLASS")
print("=" * 60)

class Anjing(Hewan):
    """Child class dengan atribut dan method tambahan"""

    def __init__(self, nama, suara, ras):
        # super() digunakan untuk memanggil method dari Parent Class
        super().__init__(nama, suara)  # panggil __init__ Parent
        self.ras = ras  # atribut BARU khusus Anjing

    def fetch(self):
        """Method BARU khusus Anjing"""
        print(f"{self.nama} sedang mengambil bola! 🎾")

    def info_lengkap(self):
        print(f"Nama: {self.nama}, Ras: {self.ras}, Suara: {self.suara}")


anjing = Anjing("Buddy", "Guk guk", "Golden Retriever")
anjing.bersuara()       # Dari Parent → Buddy berbunyi: Guk guk!
anjing.fetch()          # Dari Child  → Buddy sedang mengambil bola! 🎾
anjing.info_lengkap()   # Dari Child
print()


# ============================================================================
# BAGIAN 4: FUNGSI super() SECARA MENDALAM
# ============================================================================
print("=" * 60)
print("BAGIAN 4: FUNGSI super() SECARA MENDALAM")
print("=" * 60)
"""
super() adalah fungsi bawaan Python yang mengembalikan objek sementara
dari Parent Class, sehingga kita bisa memanggil method Parent.

Kenapa pakai super()?
1. Menghindari penulisan nama Parent secara langsung (agar fleksibel)
2. Mendukung Multiple Inheritance dengan baik
3. Kode lebih bersih dan maintainable
"""

class Kendaraan:
    def __init__(self, merk, tahun):
        self.merk = merk
        self.tahun = tahun
        print(f"[Kendaraan.__init__] Merk: {merk}, Tahun: {tahun}")

    def tampilkan(self):
        print(f"Kendaraan: {self.merk} ({self.tahun})")


class Mobil(Kendaraan):
    def __init__(self, merk, tahun, jumlah_pintu):
        # Cara 1: Menggunakan super() ✅ (RECOMMENDED)
        super().__init__(merk, tahun)
        self.jumlah_pintu = jumlah_pintu
        print(f"[Mobil.__init__] Pintu: {jumlah_pintu}")

    def tampilkan(self):
        super().tampilkan()  # panggil method Parent dulu
        print(f"Jumlah Pintu: {self.jumlah_pintu}")


class Motor(Kendaraan):
    def __init__(self, merk, tahun, cc):
        # Cara 2: Memanggil Parent langsung ⚠️ (TIDAK RECOMMENDED)
        Kendaraan.__init__(self, merk, tahun)
        self.cc = cc


mobil = Mobil("Toyota", 2024, 4)
mobil.tampilkan()
print()


# ============================================================================
# BAGIAN 5: METHOD OVERRIDING (Menimpa Method Parent)
# ============================================================================
print("=" * 60)
print("BAGIAN 5: METHOD OVERRIDING")
print("=" * 60)
"""
Method Overriding = Menulis ulang method Parent di Child Class
dengan implementasi yang berbeda.

Aturan:
- Nama method HARUS SAMA dengan yang ada di Parent
- Parameter boleh sama atau berbeda
- Child class akan menggunakan versinya sendiri
"""

class Bentuk:
    def __init__(self, nama):
        self.nama = nama

    def luas(self):
        print("Method ini harus di-override oleh child class!")
        return 0

    def info(self):
        print(f"Bentuk: {self.nama}, Luas: {self.luas()}")


class Persegi(Bentuk):
    def __init__(self, sisi):
        super().__init__("Persegi")
        self.sisi = sisi

    def luas(self):  # OVERRIDE method luas() dari Parent
        return self.sisi ** 2


class Lingkaran(Bentuk):
    def __init__(self, jari_jari):
        super().__init__("Lingkaran")
        self.jari_jari = jari_jari

    def luas(self):  # OVERRIDE method luas() dari Parent
        return 3.14159 * self.jari_jari ** 2


persegi = Persegi(5)
persegi.info()   # Bentuk: Persegi, Luas: 25

lingkaran = Lingkaran(7)
lingkaran.info() # Bentuk: Lingkaran, Luas: 153.93...
print()


# ============================================================================
# BAGIAN 6: JENIS-JENIS INHERITANCE
# ============================================================================
print("=" * 60)
print("BAGIAN 6: JENIS-JENIS INHERITANCE")
print("=" * 60)

# --- 6.1: Single Inheritance ---
# A → B (Satu parent, satu child)
print("\n--- 6.1: Single Inheritance ---")

class Buah:
    def __init__(self, nama):
        self.nama = nama

class Apel(Buah):  # Apel mewarisi Buah
    def warna(self):
        return "Merah"

apel = Apel("Apel Fuji")
print(f"{apel.nama} berwarna {apel.warna()}")


# --- 6.2: Multilevel Inheritance ---
# A → B → C (Rantai turunan)
print("\n--- 6.2: Multilevel Inheritance ---")

class Makhluk:
    def bernapas(self):
        print("Saya bernapas")

class Manusia(Makhluk):  # Manusia mewarisi Makhluk
    def bicara(self):
        print("Saya bisa bicara")

class Mahasiswa(Manusia):  # Mahasiswa mewarisi Manusia
    def belajar(self):
        print("Saya sedang belajar")

mhs = Mahasiswa()
mhs.bernapas()  # dari Makhluk (kakek)
mhs.bicara()    # dari Manusia (orang tua)
mhs.belajar()   # dari Mahasiswa (diri sendiri)


# --- 6.3: Multiple Inheritance ---
# A, B → C (Satu child mewarisi beberapa parent)
print("\n--- 6.3: Multiple Inheritance ---")

class Perenang:
    def berenang(self):
        print("Saya bisa berenang 🏊")

class Pelari:
    def berlari(self):
        print("Saya bisa berlari 🏃")

class Atlet(Perenang, Pelari):  # Mewarisi DUA parent sekaligus!
    def info(self):
        print("Saya adalah atlet multitalenta!")

atlet = Atlet()
atlet.info()
atlet.berenang()  # dari Perenang
atlet.berlari()   # dari Pelari


# --- 6.4: Hierarchical Inheritance ---
# A → B, A → C (Satu parent, banyak child)
print("\n--- 6.4: Hierarchical Inheritance ---")

class Pegawai:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji

class Manager(Pegawai):
    def tugas(self):
        print(f"{self.nama} (Manager): Memimpin tim")

class Developer(Pegawai):
    def tugas(self):
        print(f"{self.nama} (Developer): Menulis kode")

class Designer(Pegawai):
    def tugas(self):
        print(f"{self.nama} (Designer): Mendesain UI/UX")

mgr = Manager("Andi", 15000000)
dev = Developer("Budi", 12000000)
dsg = Designer("Citra", 11000000)
mgr.tugas()
dev.tugas()
dsg.tugas()
print()


# ============================================================================
# BAGIAN 7: MRO (Method Resolution Order)
# ============================================================================
print("=" * 60)
print("BAGIAN 7: MRO (Method Resolution Order)")
print("=" * 60)
"""
MRO menentukan URUTAN Python mencari method ketika ada Multiple Inheritance.
Python menggunakan algoritma C3 Linearization.

Cara melihat MRO:
1. ClassName.__mro__
2. ClassName.mro()
"""

class A:
    def siapa(self):
        print("Saya A")

class B(A):
    def siapa(self):
        print("Saya B")

class C(A):
    def siapa(self):
        print("Saya C")

class D(B, C):  # D mewarisi B dan C
    pass

d = D()
d.siapa()  # Output: Saya B (karena B dicari lebih dulu)

# Lihat urutan MRO:
print("MRO dari D:", [cls.__name__ for cls in D.__mro__])
# Output: ['D', 'B', 'C', 'A', 'object']
print()


# ============================================================================
# BAGIAN 8: FUNGSI BAWAAN UNTUK INHERITANCE
# ============================================================================
print("=" * 60)
print("BAGIAN 8: FUNGSI BAWAAN UNTUK INHERITANCE")
print("=" * 60)

# isinstance() → Cek apakah objek adalah instance dari class tertentu
print("\n--- isinstance() ---")
print(f"isinstance(anjing, Anjing): {isinstance(anjing, Anjing)}")  # True
print(f"isinstance(anjing, Hewan): {isinstance(anjing, Hewan)}")    # True
print(f"isinstance(kucing, Anjing): {isinstance(kucing, Anjing)}")  # False

# issubclass() → Cek apakah class adalah subclass dari class lain
print("\n--- issubclass() ---")
print(f"issubclass(Anjing, Hewan): {issubclass(Anjing, Hewan)}")    # True
print(f"issubclass(Hewan, Anjing): {issubclass(Hewan, Anjing)}")    # False
print(f"issubclass(Mobil, Kendaraan): {issubclass(Mobil, Kendaraan)}")  # True

# hasattr() → Cek apakah objek memiliki atribut/method tertentu
print("\n--- hasattr() ---")
print(f"hasattr(anjing, 'ras'): {hasattr(anjing, 'ras')}")      # True
print(f"hasattr(kucing, 'ras'): {hasattr(kucing, 'ras')}")      # False
print(f"hasattr(anjing, 'fetch'): {hasattr(anjing, 'fetch')}")  # True
print()


# ============================================================================
# BAGIAN 9: ABSTRACT CLASS (Kelas Abstrak)
# ============================================================================
print("=" * 60)
print("BAGIAN 9: ABSTRACT CLASS")
print("=" * 60)
"""
Abstract Class = Class yang TIDAK BISA di-instansiasi secara langsung.
Digunakan sebagai "template" yang WAJIB di-override oleh child class.

Gunakan modul abc (Abstract Base Classes) dari Python.
"""
from abc import ABC, abstractmethod

class BangunDatar(ABC):  # Mewarisi ABC = jadi Abstract Class
    """Abstract Class - tidak bisa dibuat objeknya langsung"""

    def __init__(self, nama):
        self.nama = nama

    @abstractmethod  # Decorator ini WAJIB di-override
    def luas(self):
        pass

    @abstractmethod
    def keliling(self):
        pass

    def deskripsi(self):  # Method biasa (tidak wajib di-override)
        print(f"Bangun: {self.nama}")
        print(f"  Luas: {self.luas():.2f}")
        print(f"  Keliling: {self.keliling():.2f}")


class PersegiPanjang(BangunDatar):
    def __init__(self, panjang, lebar):
        super().__init__("Persegi Panjang")
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):  # WAJIB di-override
        return self.panjang * self.lebar

    def keliling(self):  # WAJIB di-override
        return 2 * (self.panjang + self.lebar)


class Segitiga(BangunDatar):
    def __init__(self, alas, tinggi, sisi_a, sisi_b, sisi_c):
        super().__init__("Segitiga")
        self.alas = alas
        self.tinggi = tinggi
        self.sisi_a = sisi_a
        self.sisi_b = sisi_b
        self.sisi_c = sisi_c

    def luas(self):
        return 0.5 * self.alas * self.tinggi

    def keliling(self):
        return self.sisi_a + self.sisi_b + self.sisi_c


pp = PersegiPanjang(10, 5)
pp.deskripsi()

sg = Segitiga(6, 8, 6, 8, 10)
sg.deskripsi()

# Coba buat objek dari Abstract Class → akan ERROR:
try:
    bd = BangunDatar("Test")
except TypeError as e:
    print(f"\n❌ Error: {e}")
    print("   → Abstract class tidak bisa di-instansiasi!")
print()


# ============================================================================
# BAGIAN 10: ENCAPSULATION DALAM INHERITANCE
# ============================================================================
print("=" * 60)
print("BAGIAN 10: ENCAPSULATION DALAM INHERITANCE")
print("=" * 60)
"""
Tingkat akses atribut di Python:
- public    : self.nama       → bisa diakses dari mana saja
- protected : self._nama      → disarankan hanya diakses dari class & child
- private   : self.__nama     → hanya bisa diakses dari dalam class itu sendiri
"""

class Akun:
    def __init__(self, username, email, password):
        self.username = username     # public
        self._email = email          # protected (konvensi, tetap bisa diakses)
        self.__password = password   # private (name mangling)

    def get_password(self):
        return "***" + self.__password[-3:]  # hanya tampilkan 3 karakter terakhir


class AkunPremium(Akun):
    def __init__(self, username, email, password, level):
        super().__init__(username, email, password)
        self.level = level

    def tampilkan(self):
        print(f"Username : {self.username}")      # ✅ public - bisa diakses
        print(f"Email    : {self._email}")         # ⚠️ protected - bisa tapi tidak disarankan
        # print(f"Password : {self.__password}")   # ❌ ERROR - private!
        print(f"Password : {self.get_password()}")  # ✅ pakai method parent
        print(f"Level    : {self.level}")


akun = AkunPremium("danua", "danua@email.com", "rahasia123", "Gold")
akun.tampilkan()
print()


# ============================================================================
# BAGIAN 11: PROPERTY & INHERITANCE
# ============================================================================
print("=" * 60)
print("BAGIAN 11: PROPERTY & INHERITANCE")
print("=" * 60)

class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self._harga = harga

    @property
    def harga(self):
        return self._harga

    @harga.setter
    def harga(self, nilai):
        if nilai < 0:
            raise ValueError("Harga tidak boleh negatif!")
        self._harga = nilai


class ProdukDiskon(Produk):
    def __init__(self, nama, harga, diskon_persen):
        super().__init__(nama, harga)
        self.diskon_persen = diskon_persen

    @property
    def harga_diskon(self):
        potongan = self._harga * (self.diskon_persen / 100)
        return self._harga - potongan

    def tampilkan(self):
        print(f"Produk     : {self.nama}")
        print(f"Harga Asli : Rp{self.harga:,.0f}")
        print(f"Diskon     : {self.diskon_persen}%")
        print(f"Harga Final: Rp{self.harga_diskon:,.0f}")


pd = ProdukDiskon("Laptop ASUS", 15000000, 20)
pd.tampilkan()
print()


# ============================================================================
# BAGIAN 12: CONTOH PROYEK MINI - Sistem Perpustakaan
# ============================================================================
print("=" * 60)
print("BAGIAN 12: CONTOH PROYEK MINI - Sistem Perpustakaan")
print("=" * 60)

class ItemPerpustakaan(ABC):
    _counter = 0

    def __init__(self, judul, tahun):
        ItemPerpustakaan._counter += 1
        self.id = ItemPerpustakaan._counter
        self.judul = judul
        self.tahun = tahun
        self.tersedia = True

    @abstractmethod
    def tipe(self):
        pass

    def pinjam(self):
        if self.tersedia:
            self.tersedia = False
            print(f"✅ '{self.judul}' berhasil dipinjam!")
        else:
            print(f"❌ '{self.judul}' sedang tidak tersedia!")

    def kembalikan(self):
        self.tersedia = True
        print(f"🔄 '{self.judul}' berhasil dikembalikan!")

    def __str__(self):
        status = "Tersedia" if self.tersedia else "Dipinjam"
        return f"[{self.tipe()}] {self.judul} ({self.tahun}) - {status}"


class Buku(ItemPerpustakaan):
    def __init__(self, judul, tahun, penulis, halaman):
        super().__init__(judul, tahun)
        self.penulis = penulis
        self.halaman = halaman

    def tipe(self):
        return "Buku"


class Majalah(ItemPerpustakaan):
    def __init__(self, judul, tahun, edisi):
        super().__init__(judul, tahun)
        self.edisi = edisi

    def tipe(self):
        return "Majalah"


class DVD(ItemPerpustakaan):
    def __init__(self, judul, tahun, durasi_menit):
        super().__init__(judul, tahun)
        self.durasi_menit = durasi_menit

    def tipe(self):
        return "DVD"


# Demo penggunaan:
buku1 = Buku("Laskar Pelangi", 2005, "Andrea Hirata", 529)
majalah1 = Majalah("National Geographic", 2024, "Edisi Januari")
dvd1 = DVD("Filosofi Kopi", 2015, 117)

koleksi = [buku1, majalah1, dvd1]

print("\n📚 Koleksi Perpustakaan:")
for item in koleksi:
    print(f"  {item}")

print()
buku1.pinjam()
buku1.pinjam()      # Coba pinjam lagi
buku1.kembalikan()
buku1.pinjam()      # Sekarang bisa lagi


# ============================================================================
# RINGKASAN
# ============================================================================
print("\n" + "=" * 60)
print("📝 RINGKASAN INHERITANCE DI PYTHON")
print("=" * 60)
print("""
1. Inheritance = mewarisi atribut & method dari class lain
2. Syntax: class Child(Parent)
3. super() = memanggil method dari Parent class
4. Method Overriding = menulis ulang method Parent di Child
5. Jenis: Single, Multilevel, Multiple, Hierarchical
6. MRO = urutan pencarian method (C3 Linearization)
7. isinstance() & issubclass() untuk pengecekan
8. Abstract Class (ABC) = template yang wajib di-override
9. Encapsulation: public, _protected, __private
10. Property bisa diwariskan dan di-extend
""")
