"""
KUNCI JAWABAN: Structural Pattern Matching (Match Case)
-------------------------------------------------------------------------------
File ini berisi solusi untuk soal-soal di Match_Case.py.
Gunakan file ini untuk memeriksa jawabanmu, tapi cobalah mengerjakan sendiri dulu ya!
"""

# ==============================================================================
# JAWABAN SOAL LATIHAN
# ==============================================================================

print("\n=== KUNCI JAWABAN LATIHAN ===")

# --- LEVEL: MUDAH ---

# 1. Lampu Lalu Lintas
print("\n--- No 1 ---")
lampu_lalu_lintas = "Merah"
match lampu_lalu_lintas:
    case "Merah":
        print("Berhenti")
    case "Kuning":
        print("Bersiap")
    case "Hijau":
        print("Jalan")
    case _:
        print("Warna salah")


# 2. Tebak Hewan
print("\n--- No 2 ---")
suara = "Guk"
match suara:
    case "Meong":
        print("Kucing")
    case "Guk":
        print("Anjing")
    case "Mbek":
        print("Kambing")
    case _:
        print("Hewan Misterius")


# 3. Cek Extensi File
print("\n--- No 3 ---")
nama_file = "data.txt"
ext = "txt" # Atau bisa pakai nama_file.split(".")[-1]
match ext:
    case "png" | "jpg":
        print("Gambar")
    case "txt":
        print("Dokumen")
    case _:
        print("File Lain")


# 4. Cek Tipe Data Dasar
print("\n--- No 4 ---")
data_test = 100
match data_test:
    case int():
        print("Ini Angka Bulat")
    case str():
        print("Ini Tulisan")
    case _:
        print("Tipe Lain")


# 5. Tuple Sederhana
print("\n--- No 5 ---")
biodata = ("Andi", 20)
match biodata:
    case (nama, umur):
        print(f"Nama: {nama}, Umur: {umur}")
    case _:
        print("Format salah")


# --- LEVEL: MENENGAH ---

# 6. Command Parser
print("\n--- No 6 ---")
perintah = ["jalankan", "atas"]
match perintah:
    case ["jalankan", "kiri"]:
        print("Robot jalan ke kiri")
    case ["jalankan", "kanan"]:
        print("Robot jalan ke kanan")
    case ["stop"]:
        print("Robot berhenti")
    case _:
        print("Perintah tidak dikenal")


# 7. Wildcard Sisa List
print("\n--- No 7 ---")
nilai = [10, 20, 30, 40, 50]
match nilai:
    case [pertama, kedua, *sisa]:
        print(f"Pertama: {pertama}, Kedua: {kedua}, Sisa: {sisa}")
    case _:
        print("List terlalu pendek")


# 8. Guard Clause - Nilai Ujian
print("\n--- No 8 ---")
score = 85
match score:
    case s if s >= 90:
        print("A")
    case s if s >= 75:
        print("B")
    case s if s >= 60:
        print("C")
    case _:
        print("D")


# 9. Koordinat 3D
print("\n--- No 9 ---")
posisi_3d = (0, 0, 15)
match posisi_3d:
    case (x, y, 0):
        print("Di Lantai Dasar (2D)")
    case (0, 0, z):
        print("Di Tiang (Hanya ketinggian)")
    case _:
        print("Melayang di 3D")


# 10. Struktur Data Majemuk
print("\n--- No 10 ---")
# Contoh untuk data = ["login", "user123"]
data = ["login", "user123"] 
match data:
    case ["login", username]:
        print(f"Logging in user: {username}")
    case ["logout"]:
        print("Logging out...")
    case _:
        print("Invalid command")


# --- LEVEL: SULIT ---

# 11. Dictionary Patterns
print("\n--- No 11 ---")
user_info = {"nama": "Budi", "role": "admin", "status": "active"}
match user_info:
    case {"role": "admin", "status": "active"}:
        print("Selamat datang Admin!")
    case {"role": "user"}:
        print("Halo User")
    case _:
        print("Akses Ditolak")


# 12. Nested Pattern
print("\n--- No 12 ---")
paket = {"tipe": "makanan", "isi": ["Nasi", "Ayam", "Teh"]}
match paket:
    case {"tipe": "makanan", "isi": [item1, item2, *sisa]}:
        # Minimal 2 item: item1 dan item2 harus ada, sisanya optional
        print("Paket Komplit")
    case {"tipe": "elektronik"}:
        print("Barang pecah belah")
    case _:
        print("Paket Biasa/Tidak Dikenal")


# 13. Class Pattern Matching
print("\n--- No 13 ---")
class Tombol:
    def __init__(self, aksi):
        self.aksi = aksi

item = Tombol("Klik")
match item:
    case Tombol(aksi="Klik"):
        print("Tombol diklik")
    case Tombol(aksi="Geser"):
        print("Tombol digeser")
    case _:
        print("Tombol diam")


# 14. FizzBuzz Match Case
print("\n--- No 14 ---")
angka_fb = 15
match (angka_fb % 3, angka_fb % 5):
    case (0, 0):
        print("FizzBuzz")
    case (0, _):
        print("Fizz")
    case (_, 0):
        print("Buzz")
    case _:
        print(angka_fb)


# 15. Validasi Form Kompleks
print("\n--- No 15 ---")
form_data = {"username": "andi", "email": "andi@mail.com", "umur": 12}
match form_data:
    case {"username": str(), "umur": int() as u} if u >= 17:
        print("Registrasi Berhasil")
    case _:
        print("Validasi Gagal")
