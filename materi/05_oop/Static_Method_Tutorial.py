"""
PANDUAN LENGKAP @STATICMETHOD: FUNGSI "NUMPANG" YANG BERGUNA
===========================================================
Dalam Python, @staticmethod adalah cara untuk menyisipkan fungsi biasa ke dalam sebuah Class.
Ia tidak butuh data dari object (self) ataupun data dari Class (cls).

Daftar Isi:
1. Apa itu @staticmethod?
2. Kenapa tidak pakai fungsi biasa saja di luar class?
3. Perbedaan: Instance Method vs Class Method vs Static Method.
4. Contoh Kasus Nyata (Utility & Validation).
5. Soal Latihan (15 Soal: Mudah, Sedang, Sulit).
"""

import re # Untuk contoh validasi email nanti

# ==============================================================================
# 1. KONSEP DASAR: FUNGSI TANPA AKSES
# ==============================================================================
"""
Ciri-ciri @staticmethod:
- Tidak punya parameter 'self' (tidak bisa akses data object).
- Tidak punya parameter 'cls' (tidak bisa akses data class).
- Kerjanya mandiri, hanya mengandalkan input yang diberikan saat dipanggil.
- Bisa dipanggil langsung dari Class: `NamaClass.nama_method()`.
"""

class Kalkulator:
    def __init__(self, merk):
        self.merk = merk

    # Instance Method: Butuh 'self' (akses data merk)
    def sapa(self):
        return f"Halo, saya kalkulator {self.merk}"

    # STAKTICLESS: Tidak butuh data merk, cuma butuh angka buat dihitung
    @staticmethod
    def tambah(a, b):
        return a + b

print("--- 1. Konsep Dasar ---")
# Cara panggil lewat Class (Sangat disarankan)
print(f"Hasil 5 + 10: {Kalkulator.tambah(5, 10)}")

# Cara panggil lewat Object (Bisa, tapi jarang dilakukan)
k = Kalkulator("Casio")
print(f"Hasil 2 + 2: {k.tambah(2, 2)}")
print(k.sapa())


# ==============================================================================
# 2. PERBANDINGAN: TANPA @STATICMETHOD VS DENGAN @STATICMETHOD
# ==============================================================================
"""
Mungkin kamu bertanya: "Apa ruginya kalau nggak pakai @staticmethod?"
Mari kita lihat perbandingannya.
"""

# --- A. Tanpa @staticmethod (Instance Method Biasa) ---
class MathLama:
    def tambah(self, a, b):
        return a + b

# MASALAH: Kamu TERPAKSA bikin objek dulu, padahal cuma mau hitung angka.
m = MathLama() 
print(f"[Tanpa Static] 5 + 5 = {m.tambah(5, 5)}") # Boros memori karena bikin objek cuma buat 1 fungsi.


# --- B. Dengan @staticmethod (Lebih Efisien) ---
class MathBaru:
    @staticmethod
    def tambah(a, b):
        return a + b

# KEUNTUNGAN: Bisa langsung panggil tanpa bikin objek (Hemat memori & lebih cepat).
print(f"[Pake Static] 5 + 5 = {MathBaru.tambah(5, 5)}")


# --- C. Tanpa @staticmethod (Fungsi di Luar Class / Global) ---
def cek_usia(n):
    return n >= 18

class User:
    pass

# MASALAH: Fungsi cek_usia 'berceceran' di luar. Kalau ada ribuan fungsi, 
# kita bakal bingung fungsi mana yang punyanya class User.


# --- D. Dengan @staticmethod (Terorganisir / Namespacing) ---
class UserBaru:
    @staticmethod
    def apakah_dewasa(usia):
        return usia >= 18

# KEUNTUNGAN: Kita tahu pasti bahwa fungsi ini adalah bagian dari logika "User".
# Kodingan jadi lebih rapi dan profesional.
print(f"[Pake Static] Dewasa? {UserBaru.apakah_dewasa(20)}")


# ==============================================================================
# 3. KENAPA PAKAI @STATICMETHOD? (MODULARITY & NAMESPACING)
# ==============================================================================
"""
Mungkin kamu bertanya: "Kenapa nggak bikin fungsi tambah() di luar class aja?"
Jawabannya: NAMESPACING dan ORGANISASI KODE.

Bayangkan kamu punya ribuan fungsi. Dengan meletakkannya di dalam Class yang relevan, 
kodinganmu jadi lebih rapi. Orang lain tahu kalau fungsi tersebut berhubungan 
erat dengan "Kalkulator".
"""

class ValidatorPassword:
    @staticmethod
    def cek_panjang(password):
        return len(password) >= 8

    @staticmethod
    def punya_angka(password):
        return any(char.isdigit() for char in password)

print("\n--- 2. Pengorganisasian Kode ---")
pw = "rahasia123"
if ValidatorPassword.cek_panjang(pw) and ValidatorPassword.punya_angka(pw):
    print("Password Kuat!")
else:
    print("Password Lemah!")


# ==============================================================================
# 3. PERBANDINGAN TIGA JENIS METHOD
# ==============================================================================
"""
| Jenis Method      | Decorator      | Parameter Utama | Kegunaan Utama                   |
|-------------------|----------------|-----------------|----------------------------------|
| Instance Method   | (Tidak ada)    | self            | Mengubah/Membaca data object     |
| Class Method      | @classmethod   | cls             | Membuat object (Factory)         |
| Static Method     | @staticmethod  | Tidak ada       | Fungsi bantuan (Utility/Helper)  |
"""

class DemoMethod:
    atribut_class = "Data Class"

    def __init__(self):
        self.atribut_object = "Data Object"

    def instance_method(self):
        return f"Bisa akses: {self.atribut_object} & {self.atribut_class}"

    @classmethod
    def class_method(cls):
        return f"Hanya bisa akses: {cls.atribut_class}"

    @staticmethod
    def static_method():
        return "Gak bisa akses siapa-siapa, mandiri!"


# ==============================================================================
# 4. CONTOH KASUS NYATA: KONVERSI SATUAN
# ==============================================================================
class KonversiWaktu:
    @staticmethod
    def detik_ke_menit(detik):
        return detik / 60

    @staticmethod
    def menit_ke_jam(menit):
        return menit / 60

print("\n--- 3. Contoh Kasus (Konversi) ---")
print(f"120 detik = {KonversiWaktu.detik_ke_menit(120)} menit")


# ==============================================================================
# TANTANGAN / LATIHAN @STATICMETHOD (15 SOAL)
# ==============================================================================
"""
--- LEVEL MUDAH (Penulisan Dasar) ---

1. Buat class `Greeting` dengan @staticmethod `hello()` yang hanya menge-print "Halo semuanya!".
2. Buat class `MathHelper` dengan @staticmethod `kuadrat(n)` yang mengembalikan n * n.
3. Buat class `StringTools` dengan @staticmethod `hitung_vokal(teks)` yang menghitung jumlah huruf hidup (a,i,u,e,o).
4. Buat class `CheckNumber` dengan @staticmethod `apakah_genap(n)` yang mengembalikan True jika n genap.
5. Buat class `Printer` dengan @staticmethod `garis()` yang menge-print "--------------------".

--- LEVEL SEDANG (Logika Menengah) ---

6. Buat class `Validator` dengan @staticmethod `cek_email(email)`. Kembalikan True jika mengandung "@" dan ".".
7. Buat class `KonversiSuhu` dengan @staticmethod `c_ke_f(celsius)` dan `f_ke_c(fahrenheit)`.
8. Buat class `ListHelper` dengan @staticmethod `cari_terbesar(angka_list)`. Jangan pakai fungsi sum() bawaan, pakai loop manual.
9. Buat class `DataFormatter` dengan @staticmethod `format_nama(nama)`. Input: "BUDI", Output: "Budi" (Hanya huruf depan besar).
10. Buat class `Geometry` dengan @staticmethod `luas_segitiga(alas, tinggi)` dan `luas_lingkaran(radius)`.

--- LEVEL SULIT (Logic & Integration) ---

11. Buat class `PasswordGenerator`. Buat @staticmethod `acak(panjang)` yang mengembalikan string acak sepanjang n (Gunakan modul random).
12. Buat class `IDValidator`. Buat @staticmethod `cek_nik(nik)`. Syarat: Harus string, panjang 16, dan isinya angka semua.
13. Buat class `CurrencyConverter`. Buat @staticmethod `usd_to_idr(jumlah)` dengan kurs tetap Rp15.000. Tambahkan biaya admin 1%.
14. Buat class `FileManager`. Buat @staticmethod `ambil_ekstensi(nama_file)`. Input: "gambar.pemandangan.jpg", Output: "jpg".
15. [Gabungan] Buat class `AlatPintar`. 
    - Punya @staticmethod `cek_kesehatan(detak_jantung)`.
    - Aturan: < 60 Bradi, 60-100 Normal, > 100 Takikardia.
"""

print("\n" + "="*50)
print("SIAP BELAJAR @STATICMETHOD? 🚀")
print("Kerjakan 15 soal di atas di bawah ini!")
print("="*50)

# --- TEMPAT MENCOBA LATIHAN ---

# 1. Buat class `Greeting` dengan @staticmethod `hello()` yang hanya menge-print "Halo semuanya!".

class Greeting:
    @staticmethod
    def hello():
        print("Halo semuanya!")

# 2. Buat class `MathHelper` dengan @staticmethod `kuadrat(n)` yang mengembalikan n * n.

class MathHelper:
    @staticmethod
    def kuadrat(n):
        return n * n

# 3. Buat class `StringTools` dengan @staticmethod `hitung_vokal(teks)` yang menghitung jumlah huruf hidup (a,i,u,e,o).

class StringTools:
    @staticmethod
    def hitung_vokal(teks):
        vokal_target = "aiueo"
        return sum(1 for vokal in vokal_target if vokal in vokal_target)

teks = "a, i, u, e, o"
print(StringTools.hitung_vokal(teks))

# 4. Buat class `CheckNumber` dengan @staticmethod `apakah_genap(n)` yang mengembalikan True jika n genap.

class CheckNumber:
    @staticmethod
    def apakah_genap(n):
        if n % 2 == 0: return True
        else: False

# 5. Buat class `Printer` dengan @staticmethod `garis()` yang menge-print "--------------------".

class Printer:
    @staticmethod
    def garis():
        print("--------------------")

# 6. Buat class `Validator` dengan @staticmethod `cek_email(email)`. Kembalikan True jika mengandung "@" dan ".".

class Validator:
    @staticmethod
    def cek_email(email):
        if "@" in email and "." in email: return True
        else: return False

# 7. Buat class `KonversiSuhu` dengan @staticmethod `c_ke_f(celsius)` dan `f_ke_c(fahrenheit)`.

class KonversiSuhu:
    @staticmethod
    def c_ke_f(celsius):
        return (celsius * 9/5) + 32
    
    @staticmethod
    def f_ke_c(fahrenheit):
        return (fahrenheit - 32) * 5/9