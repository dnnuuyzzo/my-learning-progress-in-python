# ============================================================================
#          15 SOAL LATIHAN INHERITANCE PYTHON (Pemula)
# ============================================================================
# Petunjuk:
# - Kerjakan setiap soal di bawah komentar masing-masing
# - Jalankan file ini untuk melihat hasil
# - Jawaban ada di bagian paling bawah (JANGAN INTIP DULU!)
# ============================================================================


# ============================================================================
# SOAL 1: Single Inheritance Dasar ⭐
# ============================================================================
"""
Buat class `Hewan` dengan:
- Atribut: nama, jenis
- Method: info() → print "Nama: {nama}, Jenis: {jenis}"

Buat class `Kucing` yang mewarisi `Hewan` dengan:
- Atribut tambahan: warna
- Method: makan() → print "{nama} sedang makan ikan"

Buat objek Kucing dan panggil info() serta makan()
"""
# Tulis jawaban SOAL 1 di sini:

class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis
    def info(self):
        print(f"Nama: {self.nama}, Jenis: {self.jenis}")

class Kucing(Hewan):
    def __init__(self, nama, jenis, warna):
        super().__init__(nama, jenis)
        self.warna = warna
    def makan(self):
        print(f"{self.nama} sedang makan ikan")

my_cat = Kucing("Genki", "Anggora", "Oranye")
my_cat.info()
my_cat.makan()

# ============================================================================
# SOAL 2: super().__init__() ⭐
# ============================================================================
"""
Buat class `Kendaraan` dengan:
- Atribut: merk, tahun
- Method: info() → print "Merk: {merk}, Tahun: {tahun}"

Buat class `Mobil(Kendaraan)` dengan:
- Atribut tambahan: warna, jumlah_pintu
- Gunakan super().__init__() untuk inisialisasi atribut parent
- Method: klakson() → print "Tin tin!"

Buat objek Mobil("Toyota", 2024, "Hitam", 4) dan panggil semua method
"""
# Tulis jawaban SOAL 2 di sini:

class Kendaraan:
    def __init__(self, merk, tahun):
        self.merk = merk
        self.tahun = tahun
    def info(self):
        print(f"Merk: {self.merk}, Tahun: {self.tahun}")

class Mobil(Kendaraan):
    def __init__(self, merk, tahun, warna, jumlah_pintu):
        super().__init__(merk, tahun)
    def klakson(self):
        print("Tin tin!")

my_car = Mobil("Toyota", 2024, "Hitam", 4)
my_car.info()
my_car.klakson()


# ============================================================================
# SOAL 3: Method Overriding ⭐
# ============================================================================
"""
Buat class `Bentuk` dengan:
- Method: luas() → return 0
- Method: tampilkan() → print "Luas = {luas()}"

Buat class `Persegi(Bentuk)` dengan:
- Atribut: sisi
- Override method luas() → return sisi * sisi

Buat class `PersegiPanjang(Bentuk)` dengan:
- Atribut: panjang, lebar
- Override method luas() → return panjang * lebar

Buat objek keduanya dan panggil tampilkan()
"""
# Tulis jawaban SOAL 3 di sini:

class Bentuk:
    def luas(self):
        return 0
    def tampilkan(self):
        print(f"Luas = {self.luas()}")

class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi
    def luas(self):
        return self.sisi * self.sisi

class PersegiPanjang(Bentuk):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    def luas(self):
        return self.panjang * self.lebar

p = Persegi(10)
pp = PersegiPanjang(5, 2)
p.tampilkan()
pp.tampilkan()

# ============================================================================
# SOAL 4: Multilevel Inheritance ⭐⭐
# ============================================================================
"""
Buat rantai inheritance 3 level:
- Class `Makhluk` → method bernapas() → print "Bernapas..."
- Class `Hewan2(Makhluk)` → method bergerak() → print "Bergerak..."
- Class `Burung(Hewan2)` → method terbang() → print "Terbang..."

Buat objek Burung dan panggil ketiga method tersebut
"""
# Tulis jawaban SOAL 4 di sini:

class Makhluk:
    def bernapas(self):
        print("Bernapas...")

class Hewan2(Makhluk):
    def bergerak(self):
        print("Bergerak...")

class Burung(Hewan2):
    def terbang(self):
        print("Terbang...")

my_bird = Burung()
my_bird.bernapas()
my_bird.bergerak()
my_bird.terbang()

# ============================================================================
# SOAL 5: Multiple Inheritance ⭐⭐
# ============================================================================
"""
Buat class `BisaBerenang` dengan method berenang() → print "🏊 Berenang!"
Buat class `BisaTerbang` dengan method terbang() → print "🦅 Terbang!"
Buat class `Bebek(BisaBerenang, BisaTerbang)` dengan:
- Atribut: nama
- Method: perkenalan() → print "Saya {nama}, bebek multitalenta!"

Buat objek Bebek dan panggil semua method
"""
# Tulis jawaban SOAL 5 di sini:

class BisaBerenang:
    def berenang(self):
        print("🏊 Berenang!")

class BisaTerbang:
    def terbang(self):
        print("🦅 Terbang!")

class Bebek(BisaBerenang, BisaTerbang):
    def __init__(self, nama):
        self.nama = nama
    def perkenalan(self):
        print(f"Saya {self.nama}, bebek multitalenta!")

my_duck = Bebek("Quack")
my_duck.berenang()
my_duck.terbang()
my_duck.perkenalan()

# ============================================================================
# SOAL 6: isinstance() dan issubclass() ⭐⭐
# ============================================================================
"""
Gunakan class dari SOAL 4 (Makhluk, Hewan2, Burung).
Buat objek `elang = Burung()`

Cetak hasil dari:
1. isinstance(elang, Burung)
2. isinstance(elang, Hewan2)
3. isinstance(elang, Makhluk)
4. issubclass(Burung, Makhluk)
5. issubclass(Makhluk, Burung)
"""
# Tulis jawaban SOAL 6 di sini:

elang = Burung()
print(isinstance(elang, Burung))
print(isinstance(elang, Hewan2))
print(isinstance(elang, Makhluk))
print(issubclass(Burung, Makhluk))
print(issubclass(Makhluk, Burung))

# ============================================================================
# SOAL 7: Hierarchical Inheritance ⭐⭐
# ============================================================================
"""
Buat class `Smartphone` dengan:
- Atribut: merk, ram (dalam GB)
- Method: telepon() → print "{merk} sedang menelepon..."

Buat 3 child class:
- `iPhone(Smartphone)` → method facetime() → print "FaceTime aktif!"
- `Samsung(Smartphone)` → method dex_mode() → print "DeX Mode aktif!"  
- `Xiaomi(Smartphone)` → method ir_blaster() → print "IR Blaster aktif!"

Buat masing-masing 1 objek dan panggil telepon() + method uniknya
"""
# Tulis jawaban SOAL 7 di sini:

class Smartphone:
    def __init__(self, merk, ram):
        self.merk = merk
        self.ram = ram
    def telepon(self):
        print(f"{self.merk} sedang menelepon...")

class iPhone(Smartphone):
    def __init__(self, merk, ram):
        super().__init__(merk, ram)
    def facetime(self):
        print("FaceTime aktif!")

class Samsung(Smartphone):
    def __init__(self, merk, ram):
        super().__init__(merk, ram)
    def dex_mode(self):
        print("DeX Mode aktif!")

class Xiaomi(Smartphone):
    def __init__(self, merk, ram):
        super().__init__(merk, ram)
    def ir_blaster(self):
        print("IR Blaster aktif!")

my_iphone = iPhone("iPhone 17 Pro Max", 32)
my_iphone.telepon()
my_iphone.facetime()

my_samsung = Samsung("Samsung Zfold", 32)
my_samsung.telepon()
my_samsung.dex_mode()

my_xiaomi = Xiaomi("Redmi 13 Pro", 16)
my_xiaomi.telepon()
my_xiaomi.ir_blaster()

# ============================================================================
# SOAL 8: Encapsulation + Inheritance ⭐⭐
# ============================================================================
"""
Buat class `RekeningBank` dengan:
- Atribut: pemilik (public), _bank (protected), __saldo (private)
- Method: lihat_saldo() → return __saldo
- Method: setor(jumlah) → tambah __saldo, print konfirmasi
- Method: tarik(jumlah) → kurangi __saldo jika cukup, print konfirmasi

Buat class `RekeningTabungan(RekeningBank)`:
- Atribut tambahan: bunga_persen
- Method: hitung_bunga() → return __saldo * bunga_persen / 100
  (Hint: gunakan self.lihat_saldo() karena __saldo private)

Demo: buat objek, setor, tarik, dan hitung bunga
"""
# Tulis jawaban SOAL 8 di sini:

class RekeningBank():
    def __init__(self, pemilik, bank, saldo):
        self.pemilik = pemilik
        self._bank = bank
        self.__saldo = saldo
    def lihat_saldo(self):
        return self.__saldo
    def setor(self, jumlah):
        self.__saldo += jumlah
        print("Terkonfirmasi")
    def tarik(self, jumlah):
        self.__saldo -= jumlah
        print("Terkonfirmasi")

class RekeningTabungan(RekeningBank):
    def __init__(self, pemilik, bank, saldo, bunga_persen):
        super().__init__(pemilik, bank, saldo)
        self.bunga_persen = bunga_persen
    def hitung_bunga(self):
        return self.lihat_saldo() * self.bunga_persen / 100

my_rekening = RekeningTabungan("Danuardi", "BTN", 10000000000000000, 10)
my_rekening.setor(100000)
my_rekening.tarik(4578928)
print(my_rekening.hitung_bunga())

# ============================================================================
# SOAL 9: Abstract Class ⭐⭐⭐
# ============================================================================
"""
Buat Abstract Class `PembayaranOnline` (dari abc import ABC, abstractmethod):
- Abstract method: bayar(jumlah) 
- Abstract method: cek_saldo()
- Method biasa: riwayat() → print "Menampilkan riwayat transaksi..."

Buat 2 child class:
- `GoPay(PembayaranOnline)`: atribut saldo, implementasi bayar dan cek_saldo
- `OVO(PembayaranOnline)`: atribut saldo, implementasi bayar dan cek_saldo

Demo: buat objek, isi saldo, bayar, cek saldo
Buktikan bahwa PembayaranOnline() langsung TIDAK BISA dibuat (pakai try-except)
"""
# Tulis jawaban SOAL 9 di sini:

from abc import ABC, abstractmethod

class PembayaranOnline(ABC):
    @abstractmethod
    def bayar(self, jumlah):
        pass
    @abstractmethod
    def cek_saldo(self):
        pass
    def riwayat(self):
        print("Menampilkan riwayat transaksi...")

class GoPay(PembayaranOnline):
    def __init__(self, saldo):
        self.__saldo = saldo
    def isi_saldo(self, jumlah):
        self.__saldo += jumlah
    def bayar(self, jumlah):
        self.__saldo -= jumlah
    def cek_saldo(self):
        return self.__saldo

class OVO(PembayaranOnline):
    def __init__(self, saldo):
        self.__saldo = saldo
    def isi_saldo(self, jumlah):
        self.__saldo += jumlah
    def bayar(self, jumlah):
        self.__saldo -= jumlah
    def cek_saldo(self):
        return self.__saldo

my_gopay = GoPay(100000)
my_gopay.isi_saldo(10000)
my_gopay.bayar(20000)
print(my_gopay.cek_saldo())

my_OVO = OVO(200000)
my_OVO.isi_saldo(50000)
my_OVO.bayar(100000)
print(my_OVO.cek_saldo)

# ============================================================================
# SOAL 10: Property + Inheritance ⭐⭐⭐
# ============================================================================
"""
Buat class `Siswa`:
- Atribut: nama, _nilai (0-100)
- @property nilai → return _nilai
- @nilai.setter → cek apakah 0-100, jika tidak raise ValueError

Buat class `SiswaBeasiswa(Siswa)`:
- Atribut tambahan: beasiswa (nama beasiswa)
- @property status → return "Layak" jika nilai >= 80, else "Tidak Layak"
- Method: info() → print nama, nilai, beasiswa, status

Demo: buat objek dengan nilai 85 dan panggil info()
Coba set nilai menjadi -10 dan tangkap error-nya
"""
# Tulis jawaban SOAL 10 di sini:

class Siswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self._nilai = nilai
    
    @property
    def nilai(self):
        return self._nilai

    @nilai.setter
    def nilai(self, input_nilai):
        if input_nilai < 0 or input_nilai > 100:
            raise ValueError("Nilai harus berada di rentang 0-100")
        else:
            self._nilai = input_nilai

class SiswaBeasiswa(Siswa):
    def __init__(self, nama, nilai, beasiswa):
        super().__init__(nama, nilai)
        self.beasiswa = beasiswa
    
    @property
    def status(self):
        if self._nilai >= 80:
            return "Layak"
        else:
            return "Tidak Layak"

    def info(self):
        print(f"Nama: {self.nama}, Nilai: {self.nilai}, Beasiswa: {self.beasiswa}, Status: {self.status}")

siswa = SiswaBeasiswa("Danuardi", 100, "KIPK")
siswa.info()
try:
    siswa.nilai = -10
except ValueError as e:
    print(f"Error: {e}")

# ============================================================================
# SOAL 11: MRO (Method Resolution Order) ⭐⭐⭐
# ============================================================================
"""
Buat class berikut:
- class X → method siapa() → print "X"
- class Y(X) → method siapa() → print "Y"
- class Z(X) → method siapa() → print "Z"
- class W(Y, Z) → pass (tidak ada override)

Pertanyaan (jawab di print):
1. Ketika w = W(); w.siapa() → apa outputnya?
2. Cetak MRO dari class W menggunakan W.__mro__
3. Jelaskan mengapa hasilnya demikian (dalam komentar)
"""
# Tulis jawaban SOAL 11 di sini:

class X:
    def siapa(self):
        print("X")

class Y(X):
    def siapa(self):
        print("Y")

class Z(X):
    def siapa(self):
        print("Z")

class W(Y, Z):
    pass

w = W()
w.siapa()

# ============================================================================
# SOAL 12: super() di Multiple Inheritance ⭐⭐⭐
# ============================================================================
"""
Buat class:
- `Database` → __init__ print "Database siap", method simpan() → print "Data disimpan ke DB"
- `Cache` → __init__ print "Cache siap", method simpan() → print "Data disimpan ke Cache"
- `Aplikasi(Database, Cache)`:
  - __init__ → panggil super().__init__()
  - simpan_semua() → panggil Database.simpan(self) dan Cache.simpan(self)

Buat objek Aplikasi, panggil simpan_semua()
Cetak MRO-nya dan jelaskan __init__ mana yang terpanggil via super()
"""
# Tulis jawaban SOAL 12 di sini:

class Database:
    def __init__(self):
        print("Database siap")
    def simpan(self):
        print("Data disimpan ke Database")

class Cache:
    def __init__(self):
        print("Cache Siap")
    def simpan(self):
        print("Data disimpan ke Cache")

class Aplikasi(Database, Cache):
    def __init__(self):
        super().__init__()
    def simpan_semua():
        Database.simpan()
        Cache.simpan()

my_app = Aplikasi()
my_app.simpan()
print("MRO dari Aplikasi:", [cls.__name__ for cls in Aplikasi.__mro__])
# Yang dipanggil adalah __init__ nya Database

# ============================================================================
# SOAL 13: Sistem Toko Online ⭐⭐⭐
# ============================================================================
"""
Buat sistem mini e-commerce:

Class `Produk`:
- Atribut: nama, harga, stok
- Method: beli(jumlah) → kurangi stok jika cukup
- Method: __str__() → "{nama} - Rp{harga:,} (Stok: {stok})"

Class `Elektronik(Produk)`:
- Atribut tambahan: garansi_bulan
- Override __str__() → tambahkan info garansi

Class `Pakaian(Produk)`:
- Atribut tambahan: ukuran, warna
- Override __str__() → tambahkan info ukuran dan warna

Demo:
1. Buat masing-masing 1 objek
2. Print semua produk
3. Beli beberapa produk
4. Print lagi untuk lihat stok berkurang
"""
# Tulis jawaban SOAL 13 di sini:

class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok
    def beli(self, jumlah):
        if jumlah > self.stok or not self.stok:
            print("Stok tidak cukup")
        else:
            self.stok -= jumlah
    def __str__(self):
        return f"{self.nama} - Rp{self.harga:,} (Stok: {self.stok})"

class Elektronik(Produk):
    def __init__(self, nama, harga, stok, garansi_bulan):
        super().__init__(nama, harga, stok)
        self.garansi_bulan = garansi_bulan
    def __str__(self):
        return f"{super().__str__()} [Garansi: {self.garansi_bulan}]"

class Pakaian(Produk):
    def __init__(self, nama, harga, stok, ukuran, warna):
        super().__init__(nama, harga, stok)
        self.ukuran = ukuran
        self.warna = warna
    def __str__(self):
        return f"{super().__str__()}, Ukuran: {self.ukuran}, Warna: {self.warna}"

smartphone = Elektronik("Samsung Zfold", 100000000, 1, 36)
print(smartphone)
smartphone.beli(1)
print(smartphone)

dress = Pakaian("Dress Pesta Mewah", 50000000, 20, "M", "Merah")
print(dress)
dress.beli(10)
print(dress)

# ============================================================================
# SOAL 14: Sistem Karyawan + Gaji ⭐⭐⭐⭐
# ============================================================================
"""
Buat Abstract Class `Karyawan`:
- Atribut: nama, id_karyawan
- Abstract method: hitung_gaji()
- Method: slip_gaji() → print nama, id, dan hasil hitung_gaji()

Buat child class:
- `KaryawanTetap(Karyawan)`:
  - Atribut: gaji_pokok, tunjangan
  - hitung_gaji() → gaji_pokok + tunjangan

- `KaryawanKontrak(Karyawan)`:
  - Atribut: upah_per_jam, jam_kerja
  - hitung_gaji() → upah_per_jam * jam_kerja

- `KaryawanFreelance(Karyawan)`:
  - Atribut: upah_per_proyek, jumlah_proyek
  - hitung_gaji() → upah_per_proyek * jumlah_proyek

Demo: buat 1 objek dari masing-masing class dan panggil slip_gaji()
"""
# Tulis jawaban SOAL 14 di sini:

class Karyawan(ABC):
    def __init__(self, nama, id_karyawan):
        self.nama = nama
        self.id_karyawan = id_karyawan
    @abstractmethod
    def hitung_gaji(self):
        pass
    def slip_gaji(self):
        print(f"{self.nama} - ({self.id_karyawan}) Rp{self.hitung_gaji}")

class KaryawanTetap(Karyawan):
    def __init__(self, nama, id_karyawan, gaji_pokok, tunjangan):
        super().__init__(nama, id_karyawan)
        self.gaji_pokok = gaji_pokok
        self.tunjangan = tunjangan
    def hitung_gaji(self):
        return self.gaji_pokok + self.tunjangan

class KaryawanKontrak(Karyawan):
    def __init__(self, nama, id_karyawan, upah_per_jam, jam_kerja):
        super().__init__(nama, id_karyawan)
        self.upah_per_jam = upah_per_jam
        self.jam_kerja = jam_kerja
    def hitung_gaji(self):
        return self.upah_per_jam * self.jam_kerja

class KaryawanFreelance(Karyawan):
    def __init__(self, nama, id_karyawan, upah_per_proyek, jumlah_proyek):
        super().__init__(nama, id_karyawan)
        self.upah_per_proyek = upah_per_proyek
        self.jumlah_proyek = jumlah_proyek
    def hitung_gaji(self):
        return self.upah_per_proyek * self.jumlah_proyek

karyawan_1 = KaryawanTetap("Asep", 157028, 20000000, 5000000)
karyawan_2 = KaryawanKontrak("Ucup", 152798, 100000, 8)
karyawan_3 = KaryawanFreelance("Tuti", 123086, 50000000, 3)
print(karyawan_1.hitung_gaji())
print(karyawan_2.hitung_gaji())
print(karyawan_3.hitung_gaji())

# ============================================================================
# SOAL 15: Sistem RPG Game ⭐⭐⭐⭐
# ============================================================================
"""
Buat sistem karakter RPG sederhana:

Abstract Class `Karakter`:
- Atribut: nama, hp, attack
- Abstract method: skill_khusus()
- Method: serang(target) → kurangi hp target sebesar self.attack
  print "{nama} menyerang {target.nama}! HP {target.nama}: {target.hp}"
- Method: is_alive() → return hp > 0

Class `Warrior(Karakter)`:
- Atribut tambahan: armor
- skill_khusus() → print "{nama} menggunakan Shield Bash!"
  Efek: attack sementara dinaikkan 50%

Class `Mage(Karakter)`:
- Atribut tambahan: mana
- skill_khusus() → print "{nama} menggunakan Fireball!" (jika mana >= 20)
  Efek: attack dikali 2 untuk serangan ini, mana berkurang 20

Class `Archer(Karakter)`:
- Atribut tambahan: arrows
- skill_khusus() → print "{nama} menggunakan Rain of Arrows!" (jika arrows >= 5)
  Efek: serang 3 kali berturut-turut, arrows berkurang 5

Demo: Buat 1 Warrior, 1 Mage, 1 Archer dan simulasikan pertarungan sederhana
"""
# Tulis jawaban SOAL 15 di sini:

class Karakter(ABC):
    def __init__(self, nama, hp, attack):
        self.nama = nama
        self.hp = hp
        self.attack = attack

    @abstractmethod
    def skill_khusus(self):
        pass
    def serang(self, target):
        target.hp -= self.attack
        print(f"{self.nama} menyerang {target.nama}! HP {target.nama}: {target.hp}")
    def is_alive(self):
        if self.hp < 0:
            return f"{self.nama} telah mati! HP: {self.hp}"
        else:
            return self.hp

class Warrior(Karakter):
    def __init__(self, nama, hp, attack, armor):
        super().__init__(nama, hp, attack)
        self.armor = armor
    def skill_khusus(self):
        print(f"{self.nama} menggunakan Shield Bash!")
        self.attack += self.attack * 0.5

class Mage(Karakter):
    def __init__(self, nama, hp, attack, mana):
        super().__init__(nama, hp, attack)
        self.mana = mana
    def skill_khusus(self, target):
        if self.mana >= 20:
            print(f"{self.nama} menggunakan Fireball!")
            self.attack *= 2
            self.mana -= 20

class Archer(Karakter):
    def __init__(self, nama, hp, attack, arrows):
        super().__init__(nama, hp, attack)
        self.arrows = arrows
    def skill_khusus(self):
        if self.arrows >= 5:
            self.attack *= 3
            self.arrows -= 5

smith = Warrior("Smith", 100, 10, 5)
shell = Mage("Shell", 70, 15, 5)
glin = Archer("Glin", 50, 25, 5)

while smith.is_alive() and shell.is_alive() and glin.is_alive() > 0:
    smith.serang(shell)
    shell.serang(glin)
    glin.serang(smith)

print(smith.is_alive())
print(shell.is_alive())
print(glin.is_alive())


# ============================================================================
#
#                    ⬇️  JAWABAN DI BAWAH INI  ⬇️
#              (COBA KERJAKAN SENDIRI DULU YA! 💪)
#
# ============================================================================
print("\n" + "=" * 60)
print("📝 JAWABAN SOAL LATIHAN")
print("=" * 60)


# ==================== JAWABAN SOAL 1 ====================
print("\n--- JAWABAN SOAL 1 ---")

class HewanJ1:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def info(self):
        print(f"Nama: {self.nama}, Jenis: {self.jenis}")

class KucingJ1(HewanJ1):
    def __init__(self, nama, jenis, warna):
        super().__init__(nama, jenis)
        self.warna = warna

    def makan(self):
        print(f"{self.nama} sedang makan ikan")

kucing_j1 = KucingJ1("Mimi", "Kucing Persia", "Putih")
kucing_j1.info()
kucing_j1.makan()


# ==================== JAWABAN SOAL 2 ====================
print("\n--- JAWABAN SOAL 2 ---")

class KendaraanJ2:
    def __init__(self, merk, tahun):
        self.merk = merk
        self.tahun = tahun

    def info(self):
        print(f"Merk: {self.merk}, Tahun: {self.tahun}")

class MobilJ2(KendaraanJ2):
    def __init__(self, merk, tahun, warna, jumlah_pintu):
        super().__init__(merk, tahun)
        self.warna = warna
        self.jumlah_pintu = jumlah_pintu

    def klakson(self):
        print("Tin tin!")

mobil_j2 = MobilJ2("Toyota", 2024, "Hitam", 4)
mobil_j2.info()
mobil_j2.klakson()
print(f"Warna: {mobil_j2.warna}, Pintu: {mobil_j2.jumlah_pintu}")


# ==================== JAWABAN SOAL 3 ====================
print("\n--- JAWABAN SOAL 3 ---")

class BentukJ3:
    def luas(self):
        return 0
    def tampilkan(self):
        print(f"Luas = {self.luas()}")

class PersegiJ3(BentukJ3):
    def __init__(self, sisi):
        self.sisi = sisi
    def luas(self):
        return self.sisi * self.sisi

class PersegiPanjangJ3(BentukJ3):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    def luas(self):
        return self.panjang * self.lebar

p = PersegiJ3(5)
p.tampilkan()  # Luas = 25
pp3 = PersegiPanjangJ3(10, 5)
pp3.tampilkan()  # Luas = 50


# ==================== JAWABAN SOAL 4 ====================
print("\n--- JAWABAN SOAL 4 ---")

class MakhlukJ4:
    def bernapas(self):
        print("Bernapas...")

class Hewan2J4(MakhlukJ4):
    def bergerak(self):
        print("Bergerak...")

class BurungJ4(Hewan2J4):
    def terbang(self):
        print("Terbang...")

burung = BurungJ4()
burung.bernapas()
burung.bergerak()
burung.terbang()


# ==================== JAWABAN SOAL 5 ====================
print("\n--- JAWABAN SOAL 5 ---")

class BisaBerenangJ5:
    def berenang(self):
        print("🏊 Berenang!")

class BisaTerbangJ5:
    def terbang(self):
        print("🦅 Terbang!")

class BebekJ5(BisaBerenangJ5, BisaTerbangJ5):
    def __init__(self, nama):
        self.nama = nama
    def perkenalan(self):
        print(f"Saya {self.nama}, bebek multitalenta!")

bebek = BebekJ5("Donald")
bebek.perkenalan()
bebek.berenang()
bebek.terbang()


# ==================== JAWABAN SOAL 6 ====================
print("\n--- JAWABAN SOAL 6 ---")

elang = BurungJ4()
print(f"isinstance(elang, BurungJ4): {isinstance(elang, BurungJ4)}")
print(f"isinstance(elang, Hewan2J4): {isinstance(elang, Hewan2J4)}")
print(f"isinstance(elang, MakhlukJ4): {isinstance(elang, MakhlukJ4)}")
print(f"issubclass(BurungJ4, MakhlukJ4): {issubclass(BurungJ4, MakhlukJ4)}")
print(f"issubclass(MakhlukJ4, BurungJ4): {issubclass(MakhlukJ4, BurungJ4)}")


# ==================== JAWABAN SOAL 7 ====================
print("\n--- JAWABAN SOAL 7 ---")

class SmartphoneJ7:
    def __init__(self, merk, ram):
        self.merk = merk
        self.ram = ram
    def telepon(self):
        print(f"{self.merk} sedang menelepon...")

class iPhoneJ7(SmartphoneJ7):
    def facetime(self):
        print("FaceTime aktif!")

class SamsungJ7(SmartphoneJ7):
    def dex_mode(self):
        print("DeX Mode aktif!")

class XiaomiJ7(SmartphoneJ7):
    def ir_blaster(self):
        print("IR Blaster aktif!")

ip = iPhoneJ7("iPhone 15", 8)
ip.telepon(); ip.facetime()
ss = SamsungJ7("Galaxy S24", 12)
ss.telepon(); ss.dex_mode()
xm = XiaomiJ7("Redmi Note 13", 8)
xm.telepon(); xm.ir_blaster()


# ==================== JAWABAN SOAL 8 ====================
print("\n--- JAWABAN SOAL 8 ---")

class RekeningBankJ8:
    def __init__(self, pemilik, bank, saldo):
        self.pemilik = pemilik
        self._bank = bank
        self.__saldo = saldo

    def lihat_saldo(self):
        return self.__saldo

    def setor(self, jumlah):
        self.__saldo += jumlah
        print(f"✅ Setor Rp{jumlah:,} berhasil. Saldo: Rp{self.__saldo:,}")

    def tarik(self, jumlah):
        if jumlah > self.__saldo:
            print("❌ Saldo tidak mencukupi!")
        else:
            self.__saldo -= jumlah
            print(f"✅ Tarik Rp{jumlah:,} berhasil. Saldo: Rp{self.__saldo:,}")

class RekeningTabunganJ8(RekeningBankJ8):
    def __init__(self, pemilik, bank, saldo, bunga_persen):
        super().__init__(pemilik, bank, saldo)
        self.bunga_persen = bunga_persen

    def hitung_bunga(self):
        return self.lihat_saldo() * self.bunga_persen / 100

rek = RekeningTabunganJ8("Danua", "BCA", 10000000, 5)
rek.setor(5000000)
rek.tarik(2000000)
print(f"Bunga: Rp{rek.hitung_bunga():,.0f}")


# ==================== JAWABAN SOAL 9 ====================
print("\n--- JAWABAN SOAL 9 ---")
from abc import ABC, abstractmethod

class PembayaranOnlineJ9(ABC):
    @abstractmethod
    def bayar(self, jumlah):
        pass
    @abstractmethod
    def cek_saldo(self):
        pass
    def riwayat(self):
        print("Menampilkan riwayat transaksi...")

class GoPayJ9(PembayaranOnlineJ9):
    def __init__(self, saldo=0):
        self.saldo = saldo
    def bayar(self, jumlah):
        if jumlah > self.saldo:
            print("❌ Saldo GoPay tidak cukup!")
        else:
            self.saldo -= jumlah
            print(f"✅ GoPay: Bayar Rp{jumlah:,} berhasil!")
    def cek_saldo(self):
        print(f"💰 Saldo GoPay: Rp{self.saldo:,}")

class OVOJ9(PembayaranOnlineJ9):
    def __init__(self, saldo=0):
        self.saldo = saldo
    def bayar(self, jumlah):
        if jumlah > self.saldo:
            print("❌ Saldo OVO tidak cukup!")
        else:
            self.saldo -= jumlah
            print(f"✅ OVO: Bayar Rp{jumlah:,} berhasil!")
    def cek_saldo(self):
        print(f"💰 Saldo OVO: Rp{self.saldo:,}")

gp = GoPayJ9(500000)
gp.bayar(100000)
gp.cek_saldo()
gp.riwayat()

try:
    po = PembayaranOnlineJ9()
except TypeError as e:
    print(f"❌ Error: {e}")


# ==================== JAWABAN SOAL 10 ====================
print("\n--- JAWABAN SOAL 10 ---")

class SiswaJ10:
    def __init__(self, nama, nilai):
        self.nama = nama
        self._nilai = nilai

    @property
    def nilai(self):
        return self._nilai

    @nilai.setter
    def nilai(self, v):
        if not (0 <= v <= 100):
            raise ValueError("Nilai harus antara 0-100!")
        self._nilai = v

class SiswaBeasiswaJ10(SiswaJ10):
    def __init__(self, nama, nilai, beasiswa):
        super().__init__(nama, nilai)
        self.beasiswa = beasiswa

    @property
    def status(self):
        return "Layak" if self.nilai >= 80 else "Tidak Layak"

    def info(self):
        print(f"Nama: {self.nama}, Nilai: {self.nilai}")
        print(f"Beasiswa: {self.beasiswa}, Status: {self.status}")

sb = SiswaBeasiswaJ10("Andi", 85, "Beasiswa Prestasi")
sb.info()
try:
    sb.nilai = -10
except ValueError as e:
    print(f"❌ Error: {e}")


# ==================== JAWABAN SOAL 11 ====================
print("\n--- JAWABAN SOAL 11 ---")

class XJ11:
    def siapa(self): print("X")
class YJ11(XJ11):
    def siapa(self): print("Y")
class ZJ11(XJ11):
    def siapa(self): print("Z")
class WJ11(YJ11, ZJ11):
    pass

w = WJ11()
w.siapa()  # Output: "Y" karena Y dicek LEBIH DULU di MRO
print("MRO:", [c.__name__ for c in WJ11.__mro__])
# Penjelasan: Python gunakan C3 Linearization → W, Y, Z, X, object
# Karena Y ditulis lebih dulu di W(Y, Z), maka Y dicek duluan


# ==================== JAWABAN SOAL 12 ====================
print("\n--- JAWABAN SOAL 12 ---")

class DatabaseJ12:
    def __init__(self):
        print("Database siap")
    def simpan(self):
        print("Data disimpan ke DB")

class CacheJ12:
    def __init__(self):
        print("Cache siap")
    def simpan(self):
        print("Data disimpan ke Cache")

class AplikasiJ12(DatabaseJ12, CacheJ12):
    def __init__(self):
        super().__init__()  # Hanya DatabaseJ12.__init__ yang terpanggil (MRO)
    def simpan_semua(self):
        DatabaseJ12.simpan(self)
        CacheJ12.simpan(self)

app = AplikasiJ12()
app.simpan_semua()
print("MRO:", [c.__name__ for c in AplikasiJ12.__mro__])


# ==================== JAWABAN SOAL 13 ====================
print("\n--- JAWABAN SOAL 13 ---")

class ProdukJ13:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok
    def beli(self, jumlah):
        if jumlah > self.stok:
            print(f"❌ Stok {self.nama} tidak cukup!")
        else:
            self.stok -= jumlah
            print(f"✅ Beli {jumlah}x {self.nama} berhasil!")
    def __str__(self):
        return f"{self.nama} - Rp{self.harga:,} (Stok: {self.stok})"

class ElektronikJ13(ProdukJ13):
    def __init__(self, nama, harga, stok, garansi_bulan):
        super().__init__(nama, harga, stok)
        self.garansi_bulan = garansi_bulan
    def __str__(self):
        return f"{super().__str__()} [Garansi: {self.garansi_bulan} bulan]"

class PakaianJ13(ProdukJ13):
    def __init__(self, nama, harga, stok, ukuran, warna):
        super().__init__(nama, harga, stok)
        self.ukuran = ukuran
        self.warna = warna
    def __str__(self):
        return f"{super().__str__()} [Ukuran: {self.ukuran}, Warna: {self.warna}]"

laptop = ElektronikJ13("Laptop ASUS", 12000000, 10, 24)
kaos = PakaianJ13("Kaos Polo", 250000, 50, "L", "Navy")
print(laptop)
print(kaos)
laptop.beli(2)
kaos.beli(3)
print(laptop)
print(kaos)


# ==================== JAWABAN SOAL 14 ====================
print("\n--- JAWABAN SOAL 14 ---")

class KaryawanJ14(ABC):
    def __init__(self, nama, id_karyawan):
        self.nama = nama
        self.id_karyawan = id_karyawan
    @abstractmethod
    def hitung_gaji(self):
        pass
    def slip_gaji(self):
        print(f"Nama: {self.nama} | ID: {self.id_karyawan}")
        print(f"Gaji: Rp{self.hitung_gaji():,}")
        print("-" * 30)

class KaryawanTetapJ14(KaryawanJ14):
    def __init__(self, nama, id_k, gaji_pokok, tunjangan):
        super().__init__(nama, id_k)
        self.gaji_pokok = gaji_pokok
        self.tunjangan = tunjangan
    def hitung_gaji(self):
        return self.gaji_pokok + self.tunjangan

class KaryawanKontrakJ14(KaryawanJ14):
    def __init__(self, nama, id_k, upah_per_jam, jam_kerja):
        super().__init__(nama, id_k)
        self.upah_per_jam = upah_per_jam
        self.jam_kerja = jam_kerja
    def hitung_gaji(self):
        return self.upah_per_jam * self.jam_kerja

class KaryawanFreelanceJ14(KaryawanJ14):
    def __init__(self, nama, id_k, upah_per_proyek, jumlah_proyek):
        super().__init__(nama, id_k)
        self.upah_per_proyek = upah_per_proyek
        self.jumlah_proyek = jumlah_proyek
    def hitung_gaji(self):
        return self.upah_per_proyek * self.jumlah_proyek

kt = KaryawanTetapJ14("Andi", "KT001", 8000000, 2000000)
kk = KaryawanKontrakJ14("Budi", "KK001", 75000, 160)
kf = KaryawanFreelanceJ14("Citra", "KF001", 5000000, 3)
kt.slip_gaji()
kk.slip_gaji()
kf.slip_gaji()


# ==================== JAWABAN SOAL 15 ====================
print("\n--- JAWABAN SOAL 15 ---")

class KarakterJ15(ABC):
    def __init__(self, nama, hp, attack):
        self.nama = nama
        self.hp = hp
        self.attack = attack
    @abstractmethod
    def skill_khusus(self):
        pass
    def serang(self, target):
        target.hp -= self.attack
        if target.hp < 0:
            target.hp = 0
        print(f"⚔️ {self.nama} menyerang {target.nama}! HP {target.nama}: {target.hp}")
    def is_alive(self):
        return self.hp > 0

class WarriorJ15(KarakterJ15):
    def __init__(self, nama, hp, attack, armor):
        super().__init__(nama, hp, attack)
        self.armor = armor
        self._base_attack = attack
    def skill_khusus(self):
        self.attack = int(self._base_attack * 1.5)
        print(f"🛡️ {self.nama} menggunakan Shield Bash! Attack naik jadi {self.attack}")

class MageJ15(KarakterJ15):
    def __init__(self, nama, hp, attack, mana):
        super().__init__(nama, hp, attack)
        self.mana = mana
    def skill_khusus(self):
        if self.mana >= 20:
            self.mana -= 20
            old_atk = self.attack
            self.attack *= 2
            print(f"🔥 {self.nama} menggunakan Fireball! Attack: {self.attack}, Mana: {self.mana}")
            return True  # Flag untuk reset attack setelah serang
        else:
            print(f"❌ Mana {self.nama} tidak cukup!")
            return False

class ArcherJ15(KarakterJ15):
    def __init__(self, nama, hp, attack, arrows):
        super().__init__(nama, hp, attack)
        self.arrows = arrows
    def skill_khusus(self):
        if self.arrows >= 5:
            self.arrows -= 5
            print(f"🏹 {self.nama} menggunakan Rain of Arrows! Arrows: {self.arrows}")
            return True
        else:
            print(f"❌ Arrows {self.nama} tidak cukup!")
            return False

# Demo pertarungan
warrior = WarriorJ15("Thorin", 150, 25, 15)
mage = MageJ15("Gandalf", 100, 30, 60)
archer = ArcherJ15("Legolas", 120, 20, 20)

print("🎮 PERTARUNGAN DIMULAI!")
print(f"  {warrior.nama}: HP={warrior.hp}, ATK={warrior.attack}")
print(f"  {mage.nama}: HP={mage.hp}, ATK={mage.attack}")
print(f"  {archer.nama}: HP={archer.hp}, ATK={archer.attack}")
print()

# Ronde 1
print("--- Ronde 1 ---")
warrior.skill_khusus()       # Shield Bash
warrior.serang(mage)         # Serang Gandalf

mage.skill_khusus()          # Fireball
mage.serang(warrior)         # Serang Thorin
mage.attack = 30             # Reset attack

if archer.skill_khusus():    # Rain of Arrows
    for _ in range(3):
        archer.serang(warrior)

print(f"\n📊 Status: {warrior.nama} HP={warrior.hp} | {mage.nama} HP={mage.hp} | {archer.nama} HP={archer.hp}")


print("\n\n🎉 Selamat! Kamu telah menyelesaikan 15 soal latihan Inheritance!")
print("Terus berlatih untuk menguasai OOP di Python! 💪")
