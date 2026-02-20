"""
Materi: Structural Pattern Matching (Match Case) di Python
-------------------------------------------------------------------------------
Prasyarat: Python versi 3.10 atau yang lebih baru.

Apa itu Match Case?
Bayangkan kamu punya sebuah tombol dengan banyak pilihan fungsi.
Sebelum Python 3.10, kita biasanya menggunakan `if`, `elif`, dan `else` yang panjang
untuk mengecek kondisi satu per satu.

Mulai Python 3.10, kita punya 'Match Case'. Ini mirip dengan 'Switch Case' di 
bahasa pemrograman lain (seperti C++ atau Java), tapi versi Python ini (Structural Pattern Matching) 
jauh lebih canggih! Tidak hanya mengecek nilai, tapi bisa mengecek BENTUK (struktur) data.

Mari kita pelajari dari yang paling dasar!
"""

# ==============================================================================
# 1. DASAR: PENGGANTI IF-ELIF SEDERHANA
# ==============================================================================
print("\n--- 1. Dasar Match Case ---")

status = 200

# Cara Lama (If-Elif)
if status == 200:
    print("Sukses!")
elif status == 404:
    print("Tidak Ditemukan")
elif status == 500:
    print("Server Error")
else:
    print("Status tidak dikenal")

# Cara Baru (Match-Case)
# `match` adalah subjek yang dicek, `case` adalah polanya.
match status:
    case 200:
        print("MANTAP (Match): Sukses!")
    case 404:
        print("MANTAP (Match): Tidak Ditemukan")
    case 500:
        print("MANTAP (Match): Server Error")
    case _:  # Tanda `_` (underscore) adalah Wildcard (mirip `else`)
        print("MANTAP (Match): Status tidak dikenal")


# ==============================================================================
# 2. MATCHING DENGAN PIPELINE (|) (ATAU / OR)
# ==============================================================================
print("\n--- 2. Or Pattern (|) ---")

hari = "Minggu"

match hari:
    case "Sabtu" | "Minggu":  # Jika Sabtu ATAU Minggu
        print("Waktunya Liburan!")
    case "Senin":
        print("Semangat kerja!")
    case _:
        print("Hari biasa...")


# ==============================================================================
# 3. LIST & TUPLE MATCHING (MENANGKAP NILAI)
# ==============================================================================
print("\n--- 3. Sequence Matching & Variable Binding ---")
# Ini fitur SANGAT KUAT. Kita bisa membongkar isi list/tuple langsung di dalam case.

# Contoh: Sistem koordinat (x, y)
posisi = (0, 100)

match posisi:
    case (0, 0):
        print("Posisi di titik pusat (Origin)")
    case (0, y):  # Mencocokkan tuple yang x-nya 0, dan MENYIMPAN elemen kedua ke variabel `y`
        print(f"Di sumbu Y, sejauh {y}")
    case (x, 0):  # Mencocokkan tuple yang y-nya 0, dan MENYIMPAN elemen pertama ke variabel `x`
        print(f"Di sumbu X, sejauh {x}")
    case (x, y):
        print(f"Di koordinat bebas: {x}, {y}")
    case _:
        print("Bukan koordinat valid")

# Contoh List dengan panjang tak tentu (*)
data_user = ["Budi", "Admin", "Editor", "Viewer", "Manusia"]

match data_user:
    case [nama, "User"]:
        print(f"Halo user biasa: {nama}")
    case [nama, *roles, humandity]: # `*roles` menangkap SISANYA dalam bentuk list
        print(f"Halo {nama}, kamu punya role: {roles} dan kamu adalah {humandity}")
    case _:
        print("Format data salah")


# ==============================================================================
# 4. GUARD CLAUSE (MENAMBAHKAN IF DI DALAM CASE)
# ==============================================================================
print("\n--- 4. Guard Clause ---")
# Kadang pattern saja tidak cukup, kita butuh cek kondisi angka/logika tambahan.

angka = 75

match angka:
    case n if n < 0: # Cocokkan apapun ke `n`, TAPI hanya jika n < 0
        print("Angka Negatif")
    case n if n % 2 == 0:
        print(f"{n} adalah Genap")
    case n: # Default catch-all (jika tidak masuk kriteria di atas)
        print(f"{n} adalah Ganjil")


# ==============================================================================
# 5. DICTIONARY MATCHING
# ==============================================================================
print("\n--- 5. Dictionary Matching ---")
# Kita bisa mengecek apakah sebuah dictionary punya key tertentu dan value tertentu

request_api = {"url": "google.com", "method": "GET", "timeout": 3}

match request_api:
    case {"method": "POST", "url": url}:
        print(f"Melakukan POST ke {url}")
    case {"method": "GET", "url": url}:
        print(f"Melakukan GET ke {url}")
    case _:
        print("Method tidak didukung")


# ==============================================================================
# LATIHAN SOAL (PRAKTIK)
# ==============================================================================
"""
Silakan kerjakan soal-soal di bawah ini untuk melatih pemahamanmu!
Tulis kodemu di bawah setiap komentar soal.
"""

print("\n\n=== SOAL LATIHAN ===")

# --- LEVEL: MUDAH ---

# 1. Buatlah match case sederhana yang mengecek variabel `lampu_lalu_lintas`.
#    - "Merah" -> print "Berhenti"
#    - "Kuning" -> print "Bersiap"
#    - "Hijau" -> print "Jalan"
#    - Selain itu -> print "Warna salah"
lampu_lalu_lintas = "Merah"
# Tulis kodemu di sini:
match lampu_lalu_lintas:
    case "Merah":
        print("Berhenti")
    case "Kuning":
        print("Bersiap")
    case "Hijau":
        print("Jalan")
    case _:
        print("Warna Salah")

# 2. Gunakan match case untuk menebak hewan.
#    Variabel `suara` bisa berisi "Meong", "Guk", atau "Mbek".
#    - "Meong" -> "Kucing"
#    - "Guk" -> "Anjing"
#    - "Mbek" -> "Kambing"
#    - Default -> "Hewan Misterius"
suara = "Guk"
hewan = ""
# Tulis kodemu di sini:
match suara:
    case "Meong":
        hewan = "Kucing"
    case "Guk":
        hewan = "Anjing"
    case "Mbek":
        hewan = "Kambing"
    case _:
        hewan = "Tidak diketahui"

# 3. Cek extensi file. 
#    Diberikan nama file "gambar.png". Cek akhiran stringnya (boleh hardcode logic sederhana atau split).
#    Gunakan match case untuk print "Gambar" jika akhiran ".png" atau ".jpg", dan "Dokumen" jika ".txt".
nama_file_penuh = "data.txt" # Anggap saja kita cek string ext-nya langsung misal "txt"
nama_file, ext = nama_file_penuh.split(".")
# Tulis kodemu di sini (match variable `ext`):
match ext:
    case "txt":
        print("Dokumen")
    case "png" | "jpg":
        print("Gambar")

# 4. Cek Tipe Data Dasar
#    Buat match case yang menerima input apapun.
#    - Jika `int` -> print "Ini Angka Bulat"
#    - Jika `str` -> print "Ini Tulisan"
#    - Gunakan `case int():` atau `case str():`
data_test = 100
# Tulis kodemu di sini:
match data_test:
    case int(data_test):
        print("Ini angka Bulat")
    case str(data_test):
        print("Ini Tulisan")


# 5. Tuple Sederhana
#    Diberikan tuple `biodata = ("Andi", 20)`.
#    Gunakan match case untuk menangkap (nama, umur) dan print "Nama: X, Umur: Y".
biodata = ("Andi", 20)
# Tulis kodemu di sini:
match biodata:
    case (x, y):
        print(f"Nama: {x}, Umur: {y}")

# --- LEVEL: MENENGAH ---

# 6. Command Parser (Sequence)
#    Buat sistem perintah sederhana menggunakan list.
#    - ["jalankan", "kiri"] -> print "Robot jalan ke kiri"
#    - ["jalankan", "kanan"] -> print "Robot jalan ke kanan"
#    - ["stop"] -> print "Robot berhenti"
#    - Perintah lain -> "Perintah tidak dikenal"
perintah = ["jalankan", "atas"]
# Tulis kodemu di sini:
match perintah:
    case ["jalankan", "kiri"]:
        print("Robot bergerak kearah kiri")
    case ["jalankan", "kiri"]:
        print("Robot bergerak kearah kanan")
    case ["stop"]:
        print("Robot berhenti")
    case _:
        print("Perintah tidak dikenal")

# 7. Wildcard Sisa List
#    Diberikan list angka `nilai = [10, 20, 30, 40, 50]`.
#    Tangkap elemen pertama sebagai `pertama`, kedua sebagai `kedua`, dan sisanya sebagai `sisa`.
#    Print ketiga variabel tersebut.
nilai = [10, 20, 30, 40, 50]
# Tulis kodemu di sini:
match nilai:
    case [pertama, kedua, *sisa]:
        print(f"Variabel pertama\t: {pertama}")
        print(f"Variabel kedua\t\t: {kedua}")
        print(f"Variabel sisanya\t: {sisa}")

# 8. Guard Clause - Nilai Ujian
#    Variable `score`.
#    - score >= 90 -> "A"
#    - score >= 75 -> "B"
#    - score >= 60 -> "C"
#    - Sisanya -> "D"
score = 85
# Tulis kodemu di sini:
match score:
    case x if x >= 90:
        print("A")
    case x if x >= 75:
        print("B")
    case x if x >= 60:
        print("C")
    case x:
        print("D")

# 9. Koordinat 3D
#    Tuple (x, y, z).
#    - Jika z == 0 -> "Di Lantai Dasar (2D)"
#    - Jika y == 0 dan x == 0 -> "Di Tiang (Hanya ketinggian)"
#    - Default -> "Melayang di 3D"
posisi_3d = (0, 0, 15)
# Tulis kodemu di sini:
match posisi_3d:
    case (x, y, 0):
        print("Di Lantai Dasar (2D)")
    case (0, 0, z):
        print("Di Tiang (Hanya ketinggian)")
    case (x, y, z):
        printt("Melayang di 3D")

# 10. Struktur Data Majemuk
#     List of list: `data = ["login", "user123"]`
#     Dan `data = ["logout"]`
#     Buat match case untuk handle kedua bentuk struktur list yang panjangnya beda itu.
data = ["login", "user123"]
# Tulis kodemu di sini:
match data:
    case ["login", user]:
        print(f"User {user} berhasil login")
    case ["logout"]:
        print(f"Logout berhasil")
    case _:
        print("Perintah tidak valid")

# --- LEVEL: SULIT ---

# 11. Dictionary Pattern
#     Data: `user = {"nama": "Budi", "role": "admin", "status": "active"}`
#     - Jika role "admin" DAN status "active" -> "Selamat datang Admin!"
#     - Jika role "user" -> "Halo User"
#     - Default -> "Akses Ditolak"
user_info = {"nama": "Budi", "role": "admin", "status": "active"}
# Tulis kodemu di sini:
match user_info:
    case {"nama": nama, "role": "admin", "status": "active"}:
        print("Selamat datang Admin!")
    case {"nama": nama, "role": "user", "status": status}:
        print("Halo user!")
    case _:
        print("Akses ditolak")

# 12. Nested Pattern (List di dalam Dictionary)
#     Data: `paket = {"tipe": "makanan", "isi": ["Nasi", "Ayam"]}`
#     Cek:
#     - Jika tipe "makanan" dan isi memiliki minimal 2 item -> "Paket Komplit"
#     - Jika tipe "elektronik" -> "Barang pecah belah"
paket = {"tipe": "makanan", "isi": ["Nasi", "Ayam", "Teh"]}
# Tulis kodemu di sini:
match paket:
    case {"tipe": "makanan", "isi": [_, _, *sisa]}:
        print("Paket Komplit")
    case {"tipe": "elektronik"}:
        print("Barang mudah pecah")
    case _:
        print("Barang tidak diketahui")

# 13. Class Pattern Matching (Objek)
#     Definisikan class sederhana:
class Tombol:
    def __init__(self, aksi):
        self.aksi = aksi

#     Buat objek `t = Tombol("Klik")`.
#     Lakukan match pada `t`.
#     - case Tombol(aksi="Klik") -> "Tombol diklik"
#     - case Tombol(aksi="Geser") -> "Tombol digeser"
item = Tombol("Klik")
# Tulis kodemu di sini:


# 14. FizzBuzz dengan Match Case (Tuple Trick)
#     Angka `i = 15`.
#     Lakukan match terhadap tuple `(i % 3, i % 5)`
#     - (0, 0) -> "FizzBuzz"
#     - (0, _) -> "Fizz"
#     - (_, 0) -> "Buzz"
#     - _      -> print angka itu sendiri
angka_fb = 15
# Tulis kodemu di sini:
3

# 15. Validasi Form Kompleks
#     Data: `form = {"username": "andi", "email": "andi@mail.com", "umur": 17}`
#     Validasi:
#     - Username harus string, Umur harus int.
#     - Gunakan Guard `if` untuk memastikan umur >= 17.
#     - Jika lolos -> "Registrasi Berhasil"
#     - Jika gagal -> "Validasi Gagal"
#     Petunjuk: case {"username": str(), "umur": int() as u} if u >= 17:
form_data = {"username": "andi", "email": "andi@mail.com", "umur": 12}
# Tulis kodemu di sini:
