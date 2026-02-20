"""
Materi Belajar: Read and Write Files (File I/O) dalam Python
============================================================

File handling (File I/O) adalah kemampuan program untuk berinteraksi dengan file eksternal.
Ini memungkinkan data disimpan secara permanen (persisten) sehingga tidak hilang saat program berhenti.

DAFTAR ISI MATERI LENGKAP:
1.  Konsep Dasar & Mode File
2.  Membuka & Menutup File (Safe Way with 'with')
3.  Membaca File (Reading)
4.  Menulis File (Writing)
5.  Menambah Isi File (Appending)
6.  Mode Lanjutan (r+, w+, a+)
7.  Cursor / File Pointer (seek & tell)
8.  Operasi File dengan Module OS (Rename, Delete, Check)
9.  Best Practice: Encoding & Error Handling
10. Latihan Soal (15 Soal)

"""

import os

# ==========================================
# 1. KONSEP DASAR & MODE FILE
# ==========================================
"""
Fungsi utama: `open(filename, mode, encoding)`

MODE UTAMA:
- 'r' (Read)   : Default. Membaca. Error jika file tidak ada.
- 'w' (Write)  : Menulis. Membuat file baru atau MENIMPA (overwrite) jika ada.
- 'a' (Append) : Menambah data di akhir. Membuat file baru jika tidak ada.
- 'x' (Create) : Membuat file baru. Error jika file sudah ada.

MODE TAMBAHAN:
- 'b' (Binary) : Mode biner (gambar, video, dll). Contoh: 'rb', 'wb'.
- 't' (Text)   : Default. Mode teks.
- '+' (Update) : Membaca DAN Menulis. Contoh: 'r+', 'w+'.
"""

# Nama file untuk contoh
contoh_file = "contoh_materi.txt"

# ==========================================
# 2. MEMBUKA & MENUTUP FILE (THE 'WITH' STATEMENT)
# ==========================================
print("\n--- 2. The 'with' Statement ---")

# CARA LAMA (Tidak Disarankan)
# f = open(contoh_file, "w")
# f.write("Isi data")
# f.close() # Jika lupa close, memori bocor atau data corrupt.

# CARA BARU (Best Practice - Context Manager)
# File otomatis ditutup (close) meskipun terjadi error di dalam blok kode.
with open(contoh_file, "w") as file:
    file.write("Baris 1: Ini adalah baris pertama.\n")
    file.write("Baris 2: Python File Handling itu mudah.\n")

print(f"File '{contoh_file}' berhasil dibuat.")


# ==========================================
# 3. MEMBACA FILE (READING)
# ==========================================
print("\n--- 3. Membaca File ---")

if os.path.exists(contoh_file):
    with open(contoh_file, "r") as f:
        # a. read() -> Membaca seluruh isi file menjadi satu string
        print("[a] read():")
        print(f.read()) 
        # Cursor sekarang ada di akhir file, read lagi akan kosong.

    with open(contoh_file, "r") as f:
        # b. readline() -> Membaca HANYA satu baris pembacaan cursor berjalan
        print("\n[b] readline():")
        print(f.readline(), end="") # end="" agar tidak double enter
        print(f.readline(), end="")

    with open(contoh_file, "r") as f:
        # c. readlines() -> Membaca seluruh baris menjadi LIST
        print("\n\n[c] readlines():")
        lines = f.readlines()
        print(lines) # Output: ['Baris 1...\n', 'Baris 2...\n']

    with open(contoh_file, "r") as f:
        # d. Iterasi langsung (Memory Efficient untuk file besar)
        print("\n[d] Loop file object:")
        for line in f:
            print(f"- {line.strip()}") # strip() membuang whitespace/newline
else:
    print("File tidak ditemukan.")


# ==========================================
# 4 & 5. MENULIS & APPENDING
# ==========================================
print("\n--- 4 & 5. Write vs Append ---")

# WRITE ('w') -> Menghapus isi lama, ganti baru
with open("test_write.txt", "w") as f:
    f.writelines(["Satu\n", "Dua\n", "Tiga\n"]) # writelines untuk list string
print("Mode 'w' selesai (file baru/overwrite).")

# APPEND ('a') -> Menambah di akhir
with open("test_write.txt", "a") as f:
    f.write("Empat (Data Tambahan)\n")
print("Mode 'a' selesai (data ditambah).")


# ==========================================
# 6. MODE LANJUTAN (r+, w+, a+)
# ==========================================
"""
- 'r+' (Read + Write): Pointer di AWAL. Error jika file tak ada. 
                      Bisa baca dan timpa data di posisi pointer.
- 'w+' (Write + Read): Pointer di AWAL. MENGHAPUS (truncate) isi file dulu!
- 'a+' (Append + Read): Pointer di AKHIR. Untuk baca, harus geser pointer dulu.
"""

# ==========================================
# 7. CURSOR / FILE POINTER (seek & tell)
# ==========================================
print("\n--- 7. Seek & Tell ---")

with open(contoh_file, "r") as f:
    print(f"Posisi awal: {f.tell()}") # tell() memberitahu posisi byte cursor
    f.read(5) # Baca 5 karakter
    print(f"Posisi setelah baca 5 char: {f.tell()}")
    
    # seek(offset, whence) -> Pindah posisi
    # 0: Awal file, 1: Posisi sekarang, 2: Akhir file
    f.seek(0) # Kembali ke awal
    print(f"Kembali ke awal: {f.read(5)}")


# ==========================================
# 8. OPERASI FILE DENGAN MODULE OS
# ==========================================
print("\n--- 8. OS Module ---")

nama_lama = "test_write.txt"
nama_baru = "test_renamed.txt"

# Cek Exist
if os.path.exists(nama_lama):
    # Jika nama_baru sudah ada, hapus dulu agar rename tidak error (terutama di Windows)
    if os.path.exists(nama_baru):
        os.remove(nama_baru)
        
    # Rename
    os.rename(nama_lama, nama_baru)
    print(f"Rename '{nama_lama}' -> '{nama_baru}' Sukses.")
    
    # Delete
    # os.remove(nama_baru) 
    # print("File dihapus.")
else:
    print("File target tidak ditemukan.")


# ==========================================
# 9. BEST PRACTICE: ENCODING
# ==========================================
# Selalu gunakan encoding='utf-8' saat bekerja dengan teks agar support karakter spesial/emoji
# with open("data.txt", "r", encoding="utf-8") as f: ...


# ==========================================
# 10. LATIHAN SOAL (Challenge)
# ==========================================
"""
Kerjakan soal di bawah ini untuk menguji pemahamanmu.
Kamu bisa membuat file baru untuk menjawabnya.

--- BAGIAN 1: PEMULA (WARM UP) ---
1.  Buat file "biodata_diri.txt", isi dengan: Nama, Umur, dan Hobi (masing-masing 1 baris).
2.  Baca file "biodata_diri.txt" tersebut dan tampilkan isinya ke terminal.
3.  Tambahkan (append) kalimat "Semangat Belajar Python!" di baris baru pada file tersebut.
4.  Buat fungsi `create_empty_file(filename)` yang membuat file kosong (gunakan `pass` di dalam with).
5.  Apa yang terjadi jika kamu membuka file yang tidak ada dengan mode "r"? Coba tangkap errornya dengan `try-except FileNotFoundError`.

--- BAGIAN 2: MENENGAH (LOGIC) ---
6.  Salin isi dari "biodata_diri.txt" ke file baru "copy_biodata.txt".
7.  Hitung jumlah baris dan jumlah kata dalam file "contoh_materi.txt" (yang dibuat di materi).
8.  Buat file "angka.txt" berisi angka 1 sampai 10 (tiap angka 1 baris). Kemudian baca, jumlahkan semua angkanya, dan print Totalnya.
9.  Cari dan Ganti: Baca file apa saja, ganti kata "Python" menjadi "Programming", lalu simpan ke file baru "hasil_edit.txt".
10. Reverse Lines: Baca sebuah file, lalu tulis ulang isinya ke file baru tapi urutan barisnya dibalik (Baris terakhir jadi pertama).

--- BAGIAN 3: LANJUTAN (REAL WORLD CASE) ---
11. **Log System**: Buat fungsi `log_message(msg)` yang menyimpan pesan ke "system.log" dengan format: "[TIMESTAMP] Pesan Error...". Gunakan modul `datetime`.
12. **CSV Sederhana**: Buat file "data_siswa.txt" dengan format "Nama,Nilai" per baris. Baca file tersebut, pisahkan nama dan nilai, lalu hitung rata-rata nilainya.
13. **File Cleaner**: Buat script yang mengecek apakah file "temp.txt" ada. Jika ada, hapus. Jika tidak, beri pesan "File aman".
14. **Specific Line**: Buat fungsi `baca_baris_ke(filename, n)` yang hanya mengembalikan konten baris ke-n dari sebuah file.
15. **Merge Files**: Punya 2 file "part1.txt" dan "part2.txt". Gabungkan keduanya menjadi "full_story.txt" dengan memberi satu baris kosong di antaranya.

Selamat Mengerjakan!
"""

# Tulis jawabanmu di bawah ini:

# 1.  Buat file "biodata_diri.txt", isi dengan: Nama, Umur, dan Hobi (masing-masing 1 baris).
with open("biodata_diri.txt", "w") as file:
    file.write("Nama\t: Danuardi Saputro\n")
    file.write("Umur\t: 20 Tahun\n")
    file.write("Hobi\t: Ngoding\n")

# 2.  Baca file "biodata_diri.txt" tersebut dan tampilkan isinya ke terminal.
with open("biodata_diri.txt", "r") as file:
    print(file.read())

# 3.  Tambahkan (append) kalimat "Semangat Belajar Python!" di baris baru pada file tersebut.
with open("biodata_diri.txt", "a") as file:
    file.write("Semangat Belajar Python!")

# 4.  Buat fungsi `create_empty_file(filename)` yang membuat file kosong (gunakan `pass` di dalam with).
def create_empty_file(filename):
    with open(filename, "x") as file:
        pass

# 5.  Apa yang terjadi jika kamu membuka file yang tidak ada dengan mode "r"? Coba tangkap errornya dengan `try-except FileNotFoundError`.

# 6.  Salin isi dari "biodata_diri.txt" ke file baru "copy_biodata.txt".
with open("biodata_diri.txt", "r") as file:
    back_up = file.read()

with open("copy_biodata.txt", "w") as file:
    file.write(back_up)

# 7.  Hitung jumlah baris dan jumlah kata dalam file "contoh_materi.txt" (yang dibuat di materi).
with open("contoh_materi.txt", "r") as file:
    baris = 0
    kata = 0
    for i in file:
        baris += 1
        kata += len(i.split())

# 8.  Buat file "angka.txt" berisi angka 1 sampai 10 (tiap angka 1 baris). Kemudian baca, jumlahkan semua angkanya, dan print Totalnya.
with open("angka.txt", "w") as file:
    for i in range(1, 11):
        file.write(f"{str(i)} \n")

with open("angka.txt", "r") as file:
    count = 0
    for i in file:
        count += int(i.strip())
    print("Total:", count)

# 9.  Cari dan Ganti: Baca file apa saja, ganti kata "Python" menjadi "Programming", lalu simpan ke file baru "hasil_edit.txt".
with open("copy_biodata.txt", "r") as file:
    konten = file.read()
    
konten = konten.replace("Python!", "Programming")

with open("hasil_edit.txt", "w") as file:
    file.write(konten)

# 10. Reverse Lines: Baca sebuah file, lalu tulis ulang isinya ke file baru tapi urutan barisnya dibalik (Baris terakhir jadi pertama).
with open("copy_biodata.txt", "r") as file:
    konten = file.readlines()

with open("terbalik.txt", "w") as file:
    for baris in reversed(konten):
        file.write(baris)

from datetime import datetime

def log_message(msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("system.log", "a") as file:
        file.write(f"[{timestamp}] {msg}\n")

log_message("Pesan Error: File tidak ditemukan")