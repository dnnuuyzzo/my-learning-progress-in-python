"""
Materi Belajar: The 'with' Statement (Context Managers)
=====================================================

Hai! Selamat datang di materi khusus tentang keyword `with`.
Banyak pemula yang pakai `with` cuma buat buka file, padahal fungsinya JAUH lebih hebat dari itu!

DAFTAR ISI:
1. Konsep Dasar & Analogi (Kenapa harus pakai 'with'?)
2. Implementasi Dasar pada File (Basic)
3. Cara Kerja di Belakang Layar (__enter__ & __exit__)
4. Membuat Context Manager Sendiri (Custom Class)
5. Cara Cepat Pakai Library (contextlib)
6. Multiple Contexts (Mengelola banyak resource sekaligus)
7. Latihan Soal (15 Soal)

"""

from time import time
from contextlib import contextmanager

# ==========================================
# 1. KONSEP DASAR: JANGAN JADI PEMINJAM YANG BURUK
# ==========================================
"""
Bayangkan kamu meminjam buku di perpustakaan:
1. PINJAM buku.
2. BACA buku.
3. KEMBALIKAN buku.

Kalau kamu lupa mengembalikan (Step 3), kamu akan kena denda atau diblacklist.
Dalam programming:
- Membuka File -> Harus di-CLOSE.
- Membuka Koneksi Database -> Harus di-CLOSE.
- Mengunci Thread -> Harus di-RELEASE.

Keyword `with` menjamin langkah ke-3 (CLOSE/RELEASE) akan SELALU dijalankan,
bahkan jika programmu error saat sedang membaca/memproses (Step 2).
"""

# ==========================================
# 2. IMPLEMENTASI DASAR (FILE HANDLING)
# ==========================================
print("\n--- 2. Implementasi Dasar (File) ---")

# Cara Tanpa 'with' (BERISIKO)
# f = open("test.txt", "w")
# try:
#     f.write("Halo")
#     # Jika error terjadi di sini, f.close() tidak akan pernah dipanggil!
# finally:
#     f.close() # Ribet harus pakai try-finally

# Cara Dengan 'with' (AMAN & RAPI)
# Struktur: with [RESOURCE] as [VARIABLE]:
with open("latihan_with.txt", "w") as file:
    file.write("Ini ditulis otomatis dengan aman.")
    # Saat indentasi ini selesai, file.close() otomatis dipanggil.

print("File berhasil ditulis dan ditutup.")

# --- RUANG MENCOBA 1 ---
# Silakan coba buat file "coba_sendiri.txt" menggunakan `with`, 
# tulis nama panggilanmu di dalamnya.
# Tulis kodemu di bawah ini:

with open("coba_sendiri.txt", "w") as file:
    file.write("Nama panggilanku: Danu")

# ==========================================
# 3. CARA KERJA DI BELAKANG LAYAR (MAGIC METHODS)
# ==========================================
print("\n--- 3. Magic Methods (__enter__ & __exit__) ---")
"""
Bagaimana Python tahu cara menutup file?
Ternyata object yang dipakai di `with` harus punya 2 method rahasia:
1. __enter__(): Dijalankan saat MASUK blok `with`. 
                Return value-nya akan masuk ke variabel `as ...`.
2. __exit__():  Dijalankan saat KELUAR blok `with`. 
                Di sinilah proses cleanup (close file, tutup koneksi) terjadi.
"""

class PengelolaPintu:
    def __enter__(self):
        print(">> Pintu TERBUKA otomatis!")
        return "Silakan Masuk"
    
    def __exit__(self, exc_type, exc_value, traceback):
        print(">> Pintu TERTUTUP otomatis!")
        # Return False biar kalau ada error, errornya tetap muncul (tidak ditelan)
        return False

# Mari kita coba pakai class di atas dengan 'with'
print("KITA MULAI:")
with PengelolaPintu() as pesan:
    print(f"   Sedang di dalam ruangan. Pesan: {pesan}")
    print("   Melakukan aktivitas...")
print("SELESAI.")

# --- RUANG MENCOBA 2 ---
# Coba buat class `PenghitungWaktu` yang:
# - Saat __enter__: Print "Mulai menghitung..." dan catat waktu sekarang (time.time())
# - Saat __exit__: Print "Selesai!" dan print durasi waktu yang dihabiskan.
# Gunakan modul 'time'. class-nya sudah disiapkan kerangkanya:

class PenghitungWaktu:
    def __enter__(self):
        print("Mulai menghitung...")
        time = self.time()

    def __exit__(self, exc_type, exc_value, traceback):
        print("Selesai!")
        print(f"Waktu yang diperlukan: {time}")

# Gunakan classmu di sini:
with PenghitungWaktu():
    time.sleep(1) # Pura-pura kerja selama 1 detik


# ==========================================
# 4. CARA CEPAT: MENGGUNAKAN LIBRARY (contextlib)
# ==========================================
print("\n--- 4. Library contextlib ---")
"""
Malas bikin Class dengan __enter__ dan __exit__? 
Python punya cara cepat pakai DECORATOR `@contextmanager`.
Caranya:
1. Buat fungsi generator (pakai `yield`).
2. Kode SEBELUM `yield` = __enter__.
3. Kode SETELAH `yield` = __exit__.
"""

@contextmanager
def buka_kado():
    print("🎁 Membuka bungkus kado...")
    yield "Isi Kado: Laptop Gaming!" # Ini yang dikirim ke 'as variable'
    print("🗑️ Membuang sampah bungkus kado...")

with buka_kado() as isi:
    print(f"   Wah aku dapat: {isi}")

# --- RUANG MENCOBA 3 ---
# Buat context manager pakai fungsi `HTMLTag(tag_name)` yang membungkus teks.
# Contoh output: 
# <p>
#    Halo Dunia
# </p>
# Logic: print tag pembuka, yield, print tag penutup.

# @contextmanager
# def html_tag(tag):
    # kodemu...

# with html_tag("h1"):
#    print("Judul Besar")


# ==========================================
# 5. MULTIPLE CONTEXT MANAGERS
# ==========================================
print("\n--- 5. Multiple Contexts ---")

# Kamu bisa membuka banyak resource sekaligus dalam satu baris.
# Contoh: Copy isi file A ke file B
with open("latihan_with.txt", "w") as f: f.write("Konten Asli") # Siapkan dulu filenya

# Cara with ganda:
with open("latihan_with.txt", "r") as asal, open("latihan_copy.txt", "w") as tujuan:
    isi = asal.read()
    tujuan.write(isi + " (Dicopy)")

print("Copy selesai!")

# --- RUANG MENCOBA 4 ---
# Coba gunakan `with` ganda untuk membuka 2 file teks apa saja (buat dulu kalau belum ada)
# dan print nama kedua file tersebut di dalam blok `with`.

with open("file_pertama.txt", "w") as pertama, open("file_kedua.txt", "w") as kedua:
    print(f"Nama file pertama\t: {pertama}")
    print(f"Nama file kedua\t: {kedua}")


# ==========================================
# 6. LATIHAN SOAL (15 SOAL)
# ==========================================
"""
Kerjakan soal-soal ini untuk menguji pemahamanmu tentang `with` statement.
"""

# --- LEVEL 1: PEMULA (Basic Usage) ---
# 1. Gunakan 'with' untuk membuat file "daftar_belanja.txt" dan tulis 3 barang belanjaan (pisahkan dengan enter).
# 2. Buka file "daftar_belanja.txt" dengan 'with', baca isinya, lalu print dengan huruf kapital semua.
# 3. Apa yang terjadi jika ada error (misal pembagian dengan nol 1/0) di dalam blok 'with'? Apakah file tetap tertutup? Jelaskan/Buktikan dengan kode.
# 4. Gunakan `with` untuk membuka file yang TIDAK ADA dengan mode bacara ('r'). Tangkap errornya pakai try-except.
# 5. Jelaskan dengan bahasamu sendiri, apa bedanya `f = open(...)` dengan `with open(...) as f:`?

# --- LEVEL 2: MENENGAH (Custom Context Manager) ---
# 6. Buat class `FileManager` manual yang meniru fungsi `open()`.
#    Harus punya __enter__ (return file object) dan __exit__ (close file).
# 7. Gunakan `@contextmanager` untuk membuat fungsi `my_print(prefix)` yang menambahkan prefix di setiap print di dalamnya.
#    (Hint: Ini agak tricky, mungkin perlu mengubah sys.stdout atau sekedar logic print biasa sebelum/sesudah).
#    *Alternatif soal 7*: Buat context manager `koneksi_db()` yang print "Connect DB" saat masuk, dan "Close DB" saat keluar.
# 8. Buat context manager `ListAppender(my_list, item)` dimana saat masuk blok, item ditambahkan ke list.
#    Tapi jika terjadi error di dalam blok, item tersebut DIHAPUS lagi dari list (Rollback mechanism).
# 9. Gunakan `with` nested (bersarang). `with A(): with B(): ...`. Ubah menjadi satu baris `with A(), B(): ...`.
# 10. Pelajari tentang module `tempfile`. Gunakan `with tempfile.TemporaryFile() as f:` untuk membuat file sementara yang otomatis hilang saat program selesai.

# --- LEVEL 3: SULIT (Advanced & Real World) ---
# 11. **Timer Decorator**: Gabungkan materi Decorator dan Context Manager. Buat class `Timer` yang bisa dipakai sebagai decorator `@Timer` DAN sebagai context manager `with Timer():`.
# 12. **Suppress Error**: Buat class context manager `BungkamError` yang menelan error apapun yang terjadi di dalamnya agar program tidak crash. (Hint: return True di __exit__).
# 13. **Indenter**: Buat context manager yang otomatis menambahkan indentasi (tab) pada setiap print yang dipanggil di dalam bloknya.
# 14. **Database Transaction Simulation**: Buat class `Transaction`.
#     - __enter__: Print "Start Transaction"
#     - __exit__: Jika tidak ada error, print "Commit". Jika ada error, print "Rollback" dan sembunyikan errornya.
#     - Test dengan kode yang error dan tidak error.
# 15. **Change Directory**: Buat context manager `cd(path)` yang mengubah direktori kerja (os.chdir) saat masuk, dan KEMBALI ke direktori asal saat keluar.

print("\n--- Selesai. Selamat Bereksperimen! ---")

# Tulis jawaban latihan soalmu di sini:
