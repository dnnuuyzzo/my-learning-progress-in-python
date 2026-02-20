"""
PANDUAN LENGKAP @PROPERTY PYTHON: DARI NOL SAMPAI MASTER
======================================================
Decorator @property adalah cara paling "Pythonic" untuk mengelola atribut dalam Class.
Biasanya digunakan untuk: VALIDASI, ENKAPSULASI, dan COMPUTED PROPERTIES.

Daftar Isi:
1. Masalah: Mengapa butuh @property?
2. Anatomi: Getter, Setter, dan Deleter.
3. Contoh 1: Validasi Data (Proteksi Atribut).
4. Contoh 2: Computed Property (Atribut yang Dihitung).
5. Perbandingan: Tanpa @property vs Dengan @property.
6. Soal Latihan (15 Soal: Mudah, Sedang, Sulit).
"""

# ==============================================================================
# 1. MASALAH: AKSES LANGSUNG YANG BERBAHAYA
# ==============================================================================
class ProdukTanpaProperty:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

# MASALAHNYA: Seseorang bisa mengubah harga menjadi negatif secara sengaja/tidak.
p1 = ProdukTanpaProperty("Kopi", 5000)
p1.harga = -100  # Tidak ada proteksi! Program akan kacau.

# ==============================================================================
# 2. SOLUSI: @PROPERTY (GETTER & SETTER)
# ==============================================================================
"""
Konsep Utama:
- Atribut asli disimpan dengan garis bawah (misal: `_harga`) sebagai tanda "Private".
- @property (Getter): Digunakan untuk MEMBACA nilai.
- @nama_atribut.setter: Digunakan untuk MENGUBAH nilai (ditambah validasi).
"""

class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self._harga = harga # Simpan di variabel "internal"

    @property # GETTER
    def harga(self):
        print(f"[Log] Mengakses harga {self.nama}...")
        return f"Rp{self._harga:,}"

    @harga.setter # SETTER
    def harga(self, harga_baru):
        if harga_baru < 0:
            print("[Error] Harga tidak boleh negatif! Perubahan dibatalkan.")
        else:
            print(f"[Log] Mengubah harga menjadi {harga_baru}...")
            self._harga = harga_baru

print("\n--- 1. Validasi dengan @property ---")
kopi = Produk("Espresso", 15000)
print(f"Harga awal: {kopi.harga}")

kopi.harga = 18000 # Memanggil setter otomatis
kopi.harga = -5000 # Validasi memblokir ini!
print(f"Harga akhir: {kopi.harga}")


# ==============================================================================
# 3. COMPUTED PROPERTY (ATRIBUT HASIL HITUNGAN)
# ==============================================================================
"""
Kadang kita butuh atribut yang nilainya tergantung atribut lain.
Misalnya: Luas Persegi Panjang (bergantung pada Panjang dan Lebar).
"""

class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    @property
    def luas(self):
        # Kita tidak perlu menyimpan 'luas' di memori.
        # Hitung saja setiap kali dibutuhkan!
        return self.panjang * self.lebar

print("\n--- 2. Computed Property ---")
kotak = PersegiPanjang(10, 5)
print(f"P: {kotak.panjang}, L: {kotak.lebar} -> Luas: {kotak.luas}")

kotak.panjang = 20
print(f"Update Panjang: {kotak.panjang} -> Luas Baru: {kotak.luas}")


# ==============================================================================
# 4. DELETER (MENGHAPUS ATRIBUT - OPSIONAL)
# ==============================================================================
class User:
    def __init__(self, username):
        self._username = username

    @property
    def username(self):
        return self._username

    @username.deleter
    def username(self):
        print(f"Menghapus data user {self._username}...")
        del self._username

print("\n--- 3. Deleter ---")
u = User("danu_pro")
print(f"User: {u.username}")
del u.username # Memicu @username.deleter


# ==============================================================================
# RINGKASAN: KAPAN HARUS PAKAI @PROPERTY?
# ==============================================================================
"""
1. Saat ingin menambahkan LOGIKA (if/else) setiap kali atribut dibaca/ditulis.
2. Saat ingin memproteksi atribut supaya tidak bisa diisi sembarangan.
3. Saat ingin membuat atribut "Read-Only" (Hanya buat Getter, tanpa buat Setter).
4. Saat ingin membuat atribut "Virtual" yang nilainya hasil hitungan atribut lain.
"""

# ==============================================================================
# TANTANGAN / LATIHAN @PROPERTY (15 SOAL)
# ==============================================================================
"""
--- LEVEL MUDAH (Konsep Dasar) ---

1. [Getter Dasar] Buat class `Orang` dengan atribut `_nama`. Buat property `nama` 
   yang mengembalikan nama tersebut dalam huruf KAPITAL.

2. [Setter Dasar] Buat class `Umur` dengan atribut `_nilai`. Buat setter yang 
   memastikan umur yang dimasukkan tidak boleh lebih dari 150 tahun.

3. [Read-Only] Buat class `VersiApp` yang punya property `nomor_versi` = "1.0.0". 
   Jangan buat setter, lalu coba ubah nilainya (harus error).

4. [Full Property] Buat class `Email`. Simpan di `_alamat`. Buat getter dan setter. 
   Di setter, cek apakah ada karakter "@" di dalam inputnya.

5. [Format Output] Buat class `Gaji`. Simpan di `_jumlah`. Buat getter yang 
   mengembalikan string berformat Rupiah (misal: "Rp 5.000.000").

--- LEVEL SEDANG (Logika & Konversi) ---

6. [Konversi Suhu] Buat class `Celcius`. Buat property `kelvin`. Jika kita 
   mengubah `kelvin`, maka atribut `_celcius` di dalamnya ikut berubah.

7. [Computed: Nama Lengkap] Buat class `Member` dengan `nama_depan` dan `nama_belakang`. 
   Buat property `nama_lengkap`. Jika `nama_depan` diubah, `nama_lengkap` otomatis berubah.

8. [Validasi List] Buat class `Scoreboard`. Simpan list nilai di `_scores`. 
   Buat property `total_skor` (Computed) dan setter `tambah_skor` yang mengecek 
   apakah inputnya adalah angka integer sebelum dimasukkan ke list.

9. [Password Privacy] Buat class `Akun`. Simpan password di `_password`. 
   Saat getter dipanggil, kembalikan bintang-bintang ("********"). 
   Hanya setter yang bisa mengubah nilai aslinya.

10. [Read-Only Dinamis] Buat class `Baterai`. Punya atribut `_level`. 
    Buat property `status` yang mengembalikan "Low" jika level < 20, dan "Full" jika > 80.

--- LEVEL SULIT (Logic Master) ---

11. [Setter Dependensi] Buat class `Timbangan`. Punya property `berat_kg` dan `berat_gram`. 
    Jika kita mengubah `berat_gram`, maka `berat_kg` otomatis ter-update, dan sebaliknya.

12. [Validasi String Kompleks] Buat class `Username`. Setter-nya harus mengecek: 
    Minimal 5 karakter, tidak boleh ada spasi, dan harus ada minimal 1 angka.

13. [Bank Account Legacy] Buat class `Tabungan`. Punya `_saldo`. 
    Setter `saldo` tidak boleh langsung mengganti saldo, tapi hanya boleh 
    menambah (deposit). Jika input negatif, print "Gunakan method tarik_tunai!".

14. [Computed: Usia] Buat class `Kucing`. Simpan `tahun_lahir`. 
    Buat property `usia_manusia` yang menghitung (usia_kucing * 7).

15. [Deleter Proteksi] Buat class `FileData`. Saat property `data` dihapus 
    (pakai del), buatlah sistem yang menanyakan "Apakah dikonfirmasi? (Y/N)" 
    lewat input() sebelum benar-benar menghapus atributnya.
"""

print("\n" + "="*50)
print("SIAP JADI MASTER @PROPERTY? 🚀")
print("Kerjakan 15 soal di atas di bawah ini!")
print("="*50)

# --- TEMPAT MENCOBA LATIHAN ---

# 1. [Getter Dasar] Buat class `Orang` dengan atribut `_nama`. Buat property `nama` yang mengembalikan nama tersebut dalam huruf KAPITAL.

class Orang:
    def __init__(self, input_nama):
        self._nama = input_nama
    
    @property
    def nama(self):
        return self._nama.upper()

# 2. [Setter Dasar] Buat class `Umur` dengan atribut `_nilai`. Buat setter yang memastikan umur yang dimasukkan tidak boleh lebih dari 150 tahun.

class Umur:
    def __init__(self, input_umur):
        self._umur = input_umur

    @property
    def umur(self):
        return self._umur
    
    @umur.setter
    def umur(self, umur_baru):
        if umur_baru > 150:
            print("Umur tidak boleh lebih dari 150 tahun!")
        else:
            self._umur = umur_baru

# 3. [Read-Only] Buat class `VersiApp` yang punya property `nomor_versi` = "1.0.0". Jangan buat setter, lalu coba ubah nilainya (harus error).

class VersiApp:
    @property
    def nomor_versi(self):
        return "1.0.0"

# 4. [Full Property] Buat class `Email`. Simpan di `_alamat`. Buat getter dan setter. Di setter, cek apakah ada karakter "@" di dalam inputnya.

class Email:
    def __init__(self, input_email):
        self._alamat = input_email

    @property
    def alamat(self):
        return self._alamat
    
    @alamat.setter
    def alamat(self, input_email_baru):
        if "@" in input_email_baru:
            self._alamat = input_email_baru
        else:
            print("Sertakan '@' dalam email!")

# 5. [Format Output] Buat class `Gaji`. Simpan di `_jumlah`. Buat getter yang mengembalikan string berformat Rupiah (misal: "Rp 5.000.000").

class Gaji:
    def __init__(self, jumlah):
        self._jumlah = jumlah
    
    @property
    def jumlah(self):
        return "Rp" + "{:,}".format(self._jumlah).replace(",", ".")

# 6. [Konversi Suhu] Buat class `Celcius`. Buat property `kelvin`. Jika kita mengubah `kelvin`, maka atribut `_celcius` di dalamnya ikut berubah.

class Celcius:
    def __init__(self, input_kelvin):
        self._celsius = input_kelvin - 273.15

    @property
    def kelvin(self):
        return self._celsius + 273.15
    
    @kelvin.setter
    def kelvin(self, kelvin_baru):
        self._celsius = kelvin_baru - 273.15
    
# 7. [Computed: Nama Lengkap] Buat class `Member` dengan `nama_depan` dan `nama_belakang`. Buat property `nama_lengkap`. Jika `nama_depan` diubah, `nama_lengkap` otomatis berubah.

class Member:
    def __init__(self, nama_depan, nama_belakang):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang

    @property
    def nama_lengkap(self):
        return f"{self.nama_depan} {self.nama_belakang}"

    @nama_lengkap.setter
    def nama_lengkap(self, nama_baru):
        bagian = nama_baru.split()
        self.nama_depan = bagian[0]
        self.nama_belakang = " ".join(bagian[1:])

# 8. [Validasi List] Buat class `Scoreboard`. Simpan list nilai di `_scores`. Buat property `total_skor` (Computed) dan setter `tambah_skor` yang mengecek apakah inputnya adalah angka integer sebelum dimasukkan ke list.

class Scoreboard:
    def __init__(self, nilai: list):
        self._scores = nilai

    @property
    def total_skor(self):
        return sum(self._scores)

    def tambah_skor(self, nilai_baru):
        if isinstance(nilai_baru, int):
            self._scores.append(nilai_baru)
        else:
            print("Skor harus integer!")

# 9. [Password Privacy] Buat class `Akun`. Simpan password di `_password`. Saat getter dipanggil, kembalikan bintang-bintang ("********"). Hanya setter yang bisa mengubah nilai aslinya.

class Akun:
    def __init__(self, username, password):
        self.username = username
        self._password = password

    @property
    def password(self):
        return "*" * len(self._password)

    @password.setter
    def password(self, password_baru):
        self._password = password_baru

# 10. [Read-Only Dinamis] Buat class `Baterai`. Punya atribut `_level`. Buat property `status` yang mengembalikan "Low" jika level < 20, dan "Full" jika > 80.

class Baterai:
    def __init__(self, level: int):
        self._level = level

    @property
    def status(self):
        if self._level > 80:
            return "Full"
        elif self._level < 20:
            return "Low"
        else:
            return "Normal"