# =================================================================
# MATERI: GLOBAL DAN LOCAL SCOPE DI PYTHON
# =================================================================
# Penulis: Antigravity AI
# Topik: Ruang Lingkup Variabel (Variable Scope)
# =================================================================

"""
PENGANTAR SCOPE (RUANG LINGKUP)
Scope menentukan di bagian mana suatu variabel dapat diakses atau "terlihat" oleh kode Anda.
Python mengikuti aturan LEGB untuk mencari variabel:
1. Local (L): Di dalam fungsi.
2. Enclosing (E): Di dalam fungsi yang membungkus fungsi lain (nested functions).
3. Global (G): Di tingkat teratas file script (.py).
4. Built-in (B): Variabel bawaan Python (seperti print, len, dll).
"""

# -----------------------------------------------------------------
# 1. LOCAL SCOPE (RUANG LINGKUP LOKAL)
# -----------------------------------------------------------------
# Variabel yang didefinisikan di dalam fungsi hanya hidup di dalam fungsi tersebut.

def fungsi_lokal():
    x = "Saya adalah variabel lokal"
    print(f"Inside function: {x}")

fungsi_lokal()
# print(x) # Ini akan ERROR (NameError) karena x tidak dikenal di luar fungsi.

print("-" * 30)

# -----------------------------------------------------------------
# 2. GLOBAL SCOPE (RUANG LINGKUP GLOBAL)
# -----------------------------------------------------------------
# Variabel yang didefinisikan di luar fungsi (di level indentasi 0) 
# dapat diakses dari mana saja dalam file tersebut.

y = "Saya adalah variabel global"

def fungsi_akses_global():
    print(f"Akses global dari dalam fungsi: {y}")

fungsi_akses_global()
print(f"Akses global dari luar fungsi: {y}")

print("-" * 30)

# -----------------------------------------------------------------
# 3. VARIABLE SHADOWING (PENYAMARAN VARIABEL)
# -----------------------------------------------------------------
# Jika variabel lokal punya nama yang sama dengan variabel global, 
# fungsi akan memprioritaskan yang lokal.

nama = "Budi (Global)"

def sapa():
    nama = "Andi (Lokal)"
    print(f"Halo {nama}") # Mencetak Andi

sapa()
print(f"Variabel global tetap: {nama}") # Mencetak Budi

print("-" * 30)

# -----------------------------------------------------------------
# 4. KATA KUNCI 'global'
# -----------------------------------------------------------------
# Digunakan untuk mengubah nilai variabel global dari DALAM fungsi.

angka = 10

def ubah_global():
    global angka # Memberitahu Python kita ingin memakai variabel global 'angka'
    angka = 50
    print(f"Angka di dalam fungsi (setelah diubah): {angka}")

print(f"Angka sebelum fungsi: {angka}")
ubah_global()
print(f"Angka setelah fungsi: {angka}") # Nilainya berubah jadi 50

print("-" * 30)

# -----------------------------------------------------------------
# 5. ENCLOSING SCOPE & KATA KUNCI 'nonlocal'
# -----------------------------------------------------------------
# Digunakan pada fungsi bersarang (nested functions) untuk mengubah 
# variabel di fungsi pembungkusnya (tapi bukan global).

def fungsi_luar():
    pesan = "Pesan dari Luar"
    
    def fungsi_dalam():
        nonlocal pesan # Merujuk ke 'pesan' di fungsi_luar
        pesan = "Pesan diubah oleh fungsi dalam"
        print(f"Dalam: {pesan}")
    
    fungsi_dalam()
    print(f"Luar (sesudah diubah): {pesan}")

fungsi_luar()

print("-" * 30)

# -----------------------------------------------------------------
# 6. ATURAN LEGB (RINGKASAN VISUAL)
# -----------------------------------------------------------------
"""
Cari Lokal? -> Ada? Pakai.
Tidak? -> Cari Enclosing (Fungsi induk)? Ada? Pakai.
Tidak? -> Cari Global? Ada? Pakai.
Tidak? -> Cari Built-in (Bawaan Python)? Ada? Pakai.
Tidak? -> NameError!
"""

# =================================================================
# LATIHAN MANDIRI (PRACTICE EXERCISES)
# =================================================================

# --- LEVEL: MUDAH (EASY) ---
# 1. Buat variabel global bernama 'kota' dengan isi "Jakarta".
kota = "Jakarta"
# 2. Buat fungsi yang mencap 'kota' tersebut.
    

# 3. Tambahkan variabel lokal dengan nama yang sama di fungsi lain, lihat perbedaannya.

# --- LEVEL: MENENGAH (MEDIUM) ---
# 4. Buat variabel global 'counter = 0'.
# 5. Buat fungsi 'tambah_satu()' yang bisa menambah nilai 'counter' global tersebut 
#    setiap kali dipanggil dengan menggunakan kata kunci 'global'.

# --- LEVEL: SULIT (HARD) ---
# 6. Simulasi Bank:
#    - Buat variabel global 'saldo'.
#    - Buat fungsi 'transaksi()' yang di dalamnya terdapat fungsi nested 'tarik()' dan 'setor()'.
#    - Gunakan 'global' atau 'nonlocal' secara tepat untuk mengelola saldo tersebut.
#    - Pastikan saldo tidak bisa ditarik melebihi sisa yang ada.

# =================================================================
# TIPS BEST PRACTICE:
# 1. Gunakan variabel global sesedikit mungkin untuk menghindari bug yang sulit dilacak.
# 2. Lebih baik mengoper variabel sebagai argumen/parameter fungsi.
# 3. Berikan nama variabel yang jelas untuk membedakan antara yang global dan lokal.
# =================================================================
