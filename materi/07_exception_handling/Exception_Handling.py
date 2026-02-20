"""
Materi Pembelajaran: Exception Handling (Penanganan Error) di Python
-------------------------------------------------------------------

Selamat datang! File ini dibuat khusus untuk membantumu memahami apa itu error,
exception, dan bagaimana cara menjinakkannya menggunakan blok try-except.

Daftar Isi:
1. Perbedaan Syntax Error dan Exception
2. Apa itu Try dan Except
3. Menangkap Spesifik Error
4. Blok Else dan Finally
5. Membuat Error Sendiri (Raise)
6. Latihan Soal (15 Soal)

Mari kita mulai! 🚀
"""

# ==============================================================================
# 1. Perbedaan Syntax Error dan Exception
# ==============================================================================
"""
Di Python, error dibagi menjadi dua jenis utama:

1. Syntax Error:
   Error ini terjadi 'sebelum' program dijalankan. Ini seperti kesalahan tata bahasa.
   Python tidak mengerti apa yang kamu tulis.
   Contoh: Lupa titik dua (:), kurung tidak lengkap, dll.

2. Exception (Runtime Error):
   Error ini terjadi 'saat' program sedang berjalan. Secara tata bahasa (syntax)
   kode sudah benar, tetapi terjadi sesuatu yang salah saat dieksekusi.
   Contoh: Membagi angka dengan nol, mengakses index list yang tidak ada.
"""

# Coba jalankan kode di bawah ini (Uncomment barisnya untuk mencoba)

print("--- 1. Cek Error ---")
# --- Contoh Syntax Error ---
# print("Hello world"  # <-- Kurung tutup kurang! (Uncomment untuk lihat errornya)
# Kalau ini dijalankan, Python akan langsung teriak "SyntaxError: unexpected EOF while parsing"

# --- Contoh Exception ---
# angka = 10 / 0       # <-- ZeroDivisionError! (Uncomment untuk lihat errornya)
# Kalau ini dijalankan, Python bilang "ZeroDivisionError: division by zero"


# ==============================================================================
# 2. Apa itu Try dan Except?
# ==============================================================================
"""
Bayangkan kamu sedang berjalan membawa nampan gelas.
- 'Try' adalah usahamu berjalan hati-hati (mencoba menjalankan kode).
- 'Except' adalah rencana cadanganmu jika kamu terpeleset (menangani error),
  agar gelas tidak pecah berantakan (program tidak crash).

Struktur dasar:
try:
    # Kode yang mungkin bikin error
except:
    # Kode penyelamat jika terjadi error
"""

print("\n--- 2. Contoh Dasar Try-Except ---")
try:
    # Kita mencoba kode yang berpotensi error di sini
    pembilang = 10
    penyebut = 0
    hasil = pembilang / penyebut
    print(f"Hasilnya adalah: {hasil}")
except:
    # Jika error terjadi di blok try, Python langsung lompat ke sini
    print("Ups! Terjadi kesalahan. Kamu tidak bisa membagi angka dengan nol.")

print("Program tetap lanjut jalan sampai bawah lho, tidak crash!")


# ==============================================================================
# 3. Menangkap Spesifik Error
# ==============================================================================
"""
Praktik terbaik (Best Practice) adalah menangkap error yang SPESIFIK.
Jangan cuma pakai `except:` (polos), karena itu menangkap SEMUA error,
termasuk error yang mungkin sebenarnya ingin kita lihat.

Contoh Exception umum:
- ZeroDivisionError: Bagi nol
- ValueError: Salah nilai (misal str 'a' diubah ke int)
- TypeError: Operasi salah tipe data (misal 1 + "a")
- IndexError: Ambil data di list pakai index yang kejauhan
- KeyError: Ambil data di dictionary pakai key yang gak ada
"""

print("\n--- 3. Contoh Exception Spesifik ---")
def hitung_pembagian(a, b):
    print(f"Mencoba menghitung {a} / {b} ...")
    try:
        hasil = a / b
        print(f"-> Sukses! Hasilnya: {hasil}")
    except ZeroDivisionError:
        print("-> Gagal: Tidak boleh membagi dengan nol!")
    except TypeError:
        print("-> Gagal: Input harus berupa angka ya!")
    except Exception as e:
        # 'Exception' adalah induk segala error umum. 'as e' untuk menangkap pesan errornya.
        print(f"-> Terjadi error lain yang tidak terduga: {e}")
    print("-" * 20)

# Silakan bereksperimen:
hitung_pembagian(10, 2)    # Berhasil
hitung_pembagian(10, 0)    # Kena ZeroDivisionError
hitung_pembagian(10, "a")  # Kena TypeError


# ==============================================================================
# 4. Blok Else dan Finally
# ==============================================================================
"""
Selain `try` dan `except`, ada dua teman lagi untuk melengkapi logikanya:

- `else`: Dijalankan HANYA jika TIDAK ada error di dalam block `try`.
  Berguna untuk memisahkan kode yang "mungkin error" dengan kode "lanjutan kalau sukses".

- `finally`: SELALU dijalankan, mau ada error atau tidak, mau sukses atau gagal.
  Biasa dipakai untuk bersih-bersih (clean up actions), 
  seperti menutup file atau menutup koneksi database.
"""

print("\n--- 4. Contoh Else dan Finally ---")
try:
    input_user = "100" # Coba ganti jadi "budi" untuk memicu ValueError
    angka = int(input_user)
except ValueError:
    print("EXCEPT: Gagal konversi! Itu bukan angka.")
else:
    print(f"ELSE: Sukses! Angka yang kamu masukkan adalah {angka}")
finally:
    print("FINALLY: Bagian ini akan selalu muncul apapun yang terjadi.")


# ==============================================================================
# 5. Membuat Error Sendiri (Raise)
# ==============================================================================
"""
Kadang kita ingin memicu (melemparkan) error secara sengaja jika aturan bisnis kita dilanggar.
Kita gunakan kata kunci `raise`.
"""

print("\n--- 5. Contoh Raise ---")
def daftar_sekolah_sd(usia):
    if usia < 6:
        # Kita "melempar" error buatan kita sendiri
        raise ValueError("Maaf, usia belum cukup untuk masuk SD (Min 6 tahun).")
    print(f"Selamat! Usia {usia} tahun diterima.")

try:
    umur_calon_siswa = 4 
    print(f"Mencoba mendaftar dengan usia {umur_calon_siswa}...")
    daftar_sekolah_sd(umur_calon_siswa)
except ValueError as pesan_error:
    print(f"Ditolak Sistem: {pesan_error}")

print("\n" + "="*50)
print("SELESAI MATERI. SEKARANG WAKTUNYA LATIHAN!")
print("="*50 + "\n")

# ==============================================================================
# 6. Latihan Soal (15 Soal)
# ==============================================================================
"""
Instruksi:
Kerjakan soal-soal di bawah ini untuk menguji pemahamanmu.
Kamu bisa menulis jawabannya langsung di file ini di bawah komentar soal.
"""

# --- LEVEL: EASY (MUDAH) ---

# 1. Buatlah sebuah blok try-except sederhana yang mencoba memprint variabel yang BELUM didefinisikan (misal: print(nama_saya)).
#    Tangkap error `NameError` dan tampilkan pesan "Variabel belum dibuat!".
# Jawab:

try:
    print(nama_saya)
except NameError:
    print("Variabel belum dibuat")

# 2. Apa yang akan terjadi jika dalam blok 'try' tidak terjadi error sama sekali? Apakah blok 'except' akan dijalankan?
# Jawab:
# Jika blok 'try' tidak terjadi error, maka blok 'except' tidak akan dijalankan 

# 3. Lengkapi kode berikut agar menangkap error index.
#    list_buah = ["Apel", "Jeruk"]
#    try:
#        print(list_buah[5])
#    except _______:
#        print("Index tidak ditemukan")
# Jawab:

list_buah = ["Apel", "Jeruk"]
try:
    print(list_buah[5])
except IndexError:
    print("Index tidak ditemukan")

# 4. Fungsi `int("halo")` akan menyebabkan error tipe apa?
#    a. TypeError
#    b. ValueError
#    c. NameError
# Jawab:
# Fungsi 'int("halo")' akan menyebabkan error tipe 'ValueError (b)'


# 5. Tulis satu baris kode untuk me-raise (memunculkan) error `Exception` dengan pesan "Boom!".
# Jawab:
# angka = 1
# if angka < 5: raise Exception("Boom!")

# --- LEVEL: MEDIUM (MENENGAH) ---

# 6. Buatlah program kalkulator sederhana yang meminta input dua angka dari user (pakai variabel saja, tidak perlu input()).
#    Lakukan operasi pembagian.
#    Gunakan try-except bertingkat untuk menangani:
#    a. ValueError (jika input bukan angka)
#    b. ZeroDivisionError (jika membagi nol)
# Jawab:

def pembagian(pembilang, penyebut) -> float:
    try:
        hasil = pembilang / penyebut
        return hasil
    except ValueError:
        print("Variabel pembilang atau penyebut harus berupa angka")
    except ZeroDivisionError:
        print("Variabel pembilang tidak bisa dibagi dengan nol (0)")

# 7. Jelaskan dengan kata-katamu sendiri, kapan block 'else' pada try-except-else-finally dijalankan?
# Jawab:

# Block 'else' akan dijalankan ketika block 'try' tidak mengalami error saat dijalankan

# 8. Perbaiki kode di bawah ini agar aman (tidak crash):
#    kamus = {"nama": "Budi", "umur": 20}
#    print(kamus["alamat"])
# Jawab:

kamus = {"nama": "Budi", "umur": 20}
try:
    print(kamus["alamat"])
except KeyError:
    print("Key tidak ditemukan!")

# 9. Apa output dari kode berikut?
#    try:
#        val = 10 / 2
#    except ZeroDivisionError:
#        print("Error")
#    else:
#        print("Berhasil")
#    finally:
#        print("Selesai")
# Jawab:

print("Berhasil")
print("Selesai")

# 10. Jika kita menggunakan `except Exception as e:`, variabel `e` itu isinya apa?
# Jawab:

# Variabel 'e' akan menangkap pesan error nya

# --- LEVEL: HARD (SULIT) ---

# 11. Buatlah Custom Exception bernama `PasswordTerlaluPendekError`.
#     Buat fungsi `cek_password(pw)` yang me-raise error ini jika panjang password kurang dari 5 karakter.
#     Tangkap errornya dan tampilkan pesannya.
# Jawab:

def cek_password(pw):
    if len(pw) < 5:
        raise ValueError("Password tidak boleh kurang dari 5 karakter")

try:
    cek_password("Ayu")
except ValueError as pesan_error:
    print(f"ERROR: {pesan_error}")

# 12. Buatlah fungsi `aman_baca_file(nama_file)` yang mencoba membaca file text.
#     - Handle `FileNotFoundError` (return "File tidak ada").
#     - Handle `PermissionError` (return "Izin ditolak").
#     - Pastikan file ditutup (gunakan with open atau finally).
# Jawab:

def aman_baca_file(nama_file):
    try:
       file = open(nama_file, "r")
       permission = file.read()
       if permission.lower() == "izin diterima":
        return "Izin diterima"
    except FileNotFoundError:
        return "File tidak ada"
    except PermissionError:
        return "Izin ditolak"
    finally:
        file.close()

# 13. Studi Kasus: Kamu membuat bot yang looping selamanya `while True`.
#     Kamu menutup bot dengan CTRL+C (KeyboardInterrupt).
#     Tapi kamu punya kode `except Exception: pass`.
#     Kenapa CTRL+C mungkin tidak bekerja? Dan bagaimana cara memperbaikinya?
# Jawab:


# 14. Buatlah program yang meloop list `data = [10, 0, "a", 20]`.
#     Untuk setiap elemen, coba bagi 100 dengan elemen tersebut (100/x).
#     Gunakan try-except DI DALAM loop.
#     Jika error, print type errornya saja, jangan hentikan loop.
#     Jika sukses, print hasilnya.
# Jawab:

data = [10, 0, "a", 20]
for x in data:
    try:
        hasil = 100 / x
        print(hasil)
    except ZeroDivisionError:
        print(f"{x} tidak bisa membagi 100")
    except ValueError:
        print(f"{x} tidak bisa membagi 100")

# 15. Nested Try-Except.
#     Tulis kode dimana:
#     Outer Try: Mencoba membuka file.
#     Inner Try: (Jika file terbuka) Mencoba mengubah isi file jadi integer.
#     Tangkap FileNotFoundError di Outer Except.
#     Tangkap ValueError di Inner Except.
# Jawab:

file_name = "Random.txt"
try:
    file = open(file_name, "r")
    try:
        integer = int(file.read())
    except ValueError as message:
        print(f"ERROR: {message}")
except FileNotFoundError as message:
    print(f"ERROR: {message}")    
finally:
    file.close()