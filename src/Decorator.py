"""
PANDUAN LENGKAP DECORATOR PYTHON (RAMAH PEMULA)
===============================================
Author: Assistant
Topic: Decorators
Level: Beginner to Intermediate

Daftar Isi:
1. Konsep Dasar (Prasyarat)
2. Apa itu Decorator?
3. Membuat Decorator Pertama
4. Syntax Sugar (@)
5. Decorator Untuk Fungsi dengan Parameter (*args, **kwargs)
6. Mengembalikan Nilai (Return)
7. Masalah Identitas Fungsi dan Solusinya (@wraps)
8. Contoh Kasus Nyata (Timer, Logger)
9. Soal Latihan (5 Mudah, 5 Sedang, 5 Sulit)
"""

# ==============================================================================
# BAGIAN 1: KONSEP DASAR (PRASYARAT)
# ==============================================================================
# Sebelum masuk ke decorator, kita harus paham bahwa di Python:
# 1. Fungsi adalah objek (First-Class Objects).
# 2. Fungsi bisa didefinisikan di dalam fungsi lain (Nested Functions).
# 3. Fungsi bisa dikembalikan sebagai return value.

# 1. Fungsi sebagai Objek
def sapa(nama):
    return f"Halo, {nama}!"

test_sapa = sapa # Kita bisa menyimpan fungsi ke variabel lain
print(f"1. Fungsi sebagai objek: {test_sapa('Budi')}")

# 2. Fungsi di dalam Fungsi (Nested Function)
def luar():
    print("  > Ini fungsi luar")
    def dalam():
        print("  > Ini fungsi dalam")
    dalam() # Memanggil fungsi dalam

print("\n2. Nested Function:")
luar()

# 3. Fungsi sebagai Return Value
def peluncur_roket():
    def hitung_mundur():
        return "3... 2... 1... Meluncur!"
    return hitung_mundur # Mengembalikan FUNGSI-nya, bukan hasil panggilannya

roket = peluncur_roket()
print(f"\n3. Return Function: {roket()}") 
# roket sekarang berisi fungsi hitung_mundur


# ==============================================================================
# BAGIAN 2: APA ITU DECORATOR? 
# ==============================================================================
"""
Bayangkan Decorator sebagai "Bungkus Kado" atau "Topping".
Anda punya sebuah benda (fungsi), dan anda ingin mempercantik atau 
menambah fitur pada benda tersebut TANPA mengubah benda aslinya.

Secara teknis:
Decorator adalah sebuah fungsi yang menerima fungsi lain sebagai input,
menambahkan fungsionalitas, dan mengembalikan fungsi baru (yang sudah dimodifikasi).
"""


# ==============================================================================
# BAGIAN 3: MEMBUAT DECORATOR PERTAMA
# ==============================================================================

def dekorator_sederhana(fungsi_asli):
    def pembungkus():
        print("[Log] Sebelum fungsi dijalankan...")
        fungsi_asli() # Menjalankan fungsi asli
        print("[Log] Setelah fungsi dijalankan...")
    return pembungkus

def fungsi_biasa():
    print("  -> Saya adalah fungsi biasa.")

print("\n--- Manual Decorator ---")
# Cara manual mendekorasi
fungsi_terdekorasi = dekorator_sederhana(fungsi_biasa)
fungsi_terdekorasi()


# ==============================================================================
# BAGIAN 4: SYNTAX SUGAR (@)
# ==============================================================================
"""
Python menyediakan cara yang lebih cantik untuk menggunakan decorator,
yaitu dengan simbol @ di atas definisi fungsi.
"""

print("\n--- Menggunakan @ Syntax ---")

@dekorator_sederhana
def fungsi_lain():
    print("  -> Saya fungsi lain yang otomatis didekorasi.")

# Memanggilnya seperti biasa, tapi perilakunya sudah berubah!
fungsi_lain()


# ==============================================================================
# BAGIAN 5: DECORATOR DENGAN PARAMETER (*args, **kwargs)
# ==============================================================================
"""
Bagaimana jika fungsi yang mau didekorasi punya parameter?
Wrapper kita harus bisa menerima argumen apapun.
Kita gunakan *args dan **kwargs.
"""

def dekorator_pintar(func):
    def wrapper(*args, **kwargs):
        print(f"\n[Info] Memanggil fungsi '{func.__name__}' dengan argumen {args}")
        func(*args, **kwargs)
        print("[Info] Selesai.")
    return wrapper

@dekorator_pintar
def jumlahkan(a, b):
    print(f"  Hasil: {a + b}")

jumlahkan(10, 20)


# ==============================================================================
# BAGIAN 6: MENGEMBALIKAN NILAI (RETURN)
# ==============================================================================
"""
Seringkali fungsi kita mengembalikan nilai (return), bukan cuma print.
Decorator harus meneruskan nilai return tersebut.
"""

def dekorator_return(func):
    def wrapper(*args, **kwargs):
        print("\n[Proses] Menghitung...")
        hasil = func(*args, **kwargs) # Tangkap hasilnya
        return hasil # Kembalikan hasilnya
    return wrapper

@dekorator_return
def kali(a, b):
    return a * b

hasil_kali = kali(5, 5)
print(f"Hasil Return: {hasil_kali}")


# ==============================================================================
# BAGIAN 7: MASALAH IDENTITAS DAN @wraps
# ==============================================================================
"""
Saat kita mendekorasi fungsi, nama asli fungsi berubah menjadi 'wrapper'.
Ini bisa membingungkan saat debugging. Solusinya: functools.wraps
"""
import functools

def dekorator_benar(func):
    @functools.wraps(func) # Ini menyalin metadata func ke wrapper
    def wrapper(*args, **kwargs):
        """Docstring wrapper"""
        # Lakukan sesuatu sebelum
        return func(*args, **kwargs)
    return wrapper

@dekorator_benar
def fungsi_rahasia():
    """Ini adalah docstring fungsi rahasia."""
    pass

print(f"\nNama fungsi: {fungsi_rahasia.__name__}") # Outputnya tetap 'fungsi_rahasia'
print(f"Docstring: {fungsi_rahasia.__doc__}")


# ==============================================================================
# BAGIAN 8: CONTOH KASUS NYATA
# ==============================================================================

import time

# Contoh 1: Timer (Mengukur lama eksekusi)
def timer_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"\n[Timer] Fungsi '{func.__name__}' selesai dalam {end_time - start_time:.4f} detik")
        return result
    return wrapper

@timer_decorator
def loop_berat(n):
    total = 0
    for i in range(n):
        total += i
    return total

loop_berat(1000000)


# Contoh 2: Validasi / Guard (Misal Cek Negatif)
def cegah_negatif(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Cek semua argumen posisi
        if any(isinstance(x, (int, float)) and x < 0 for x in args):
            raise ValueError("Input tidak boleh negatif!")
        return func(*args, **kwargs)
    return wrapper

@cegah_negatif
def hitung_akar_kuadrat(x):
    return x ** 0.5

try:
    print(f"Akar 9: {hitung_akar_kuadrat(9)}")
    # print(f"Akar -9: {hitung_akar_kuadrat(-9)}") # Akan error
except ValueError as e:
    print(f"Error: {e}")


# ==============================================================================
# BAGIAN 9: LATIHAN SOAL
# ==============================================================================

"""
Cobalah kerjakan soal-soal berikut untuk menguji pemahaman Anda.

--- LEVEL: MUDAH ---

1. Buatlah sebuah decorator bernama `@sapa_dulu` yang akan print "Halo!" sebelum fungsi asli dijalankan.
2. Buatlah decorator `@print_border` yang memberikan garis putus-putus "---" sebelum dan sesudah output fungsi.
3. Buatlah decorator yang mengubah hasil return fungsi string menjadi HURUF KAPITAL semua (uppercase).
4. Gunakan decorator dari soal no 1 pada sebuah fungsi `def perkenalan(nama): print(nama)`.
5. Apa output dari `fungsi.__name__` jika kita tidak menggunakan `@functools.wraps` pada decorator kita?

--- LEVEL: SEDANG ---

6. Buatlah decorator `@hanya_int` yang mengecek apakah semua argumen yang dimasukkan ke fungsi adalah integer. Jika bukan, print "Input harus angka!".
7. Buatlah decorator `@diulang_dua_kali` yang menjalankan fungsi yang didekorasi sebanyak 2 kali.
8. Buatlah decorator yang menghitung berapa kali sebuah fungsi dipanggil (Hint: gunakan atribut fungsi seperti `wrapper.calls = 0`).
9. Buat decorator yang bisa memodifikasi return value: jika hasilnya angka, kalikan dengan 2.
10. Gabungkan dua decorator sekaligus pada satu fungsi (Stacked Decorators). Misal `@bold` dan `@italic` (implementasikan logic print tag HTML <b> dan <i>).

--- LEVEL: SULIT ---

11. Buatlah decorator `@cache_sederhana`. Jika fungsi dipanggil dengan argumen yang sama, kembalikan hasil yang tersimpan di dictionary tanpa menghitung ulang.
12. Buat decorator `@retry` yang akan mencoba menjalankan fungsi 3 kali jika terjadi error (Exception).
13. Buat decorator yang membutuhkan argumen, contoh `@ulang(n=5)` yang mengulang fungsi sebanyak n kali. (Hint: Ini butuh 3 lapis fungsi).
14. Buat decorator untuk otentikasi dummy. `@butuh_login`. Buat variabel global `IS_LOGGED_IN = False`. Jika False, tolak eksekusi fungsi.
15. (Bonus) Buat decorator class (bukan function) yang menyimpan log setiap kali fungsi dipanggil ke dalam list.
"""

if __name__ == "__main__":
    # 1. Buatlah sebuah decorator bernama `@sapa_dulu` yang akan print "Halo!" sebelum fungsi asli dijalankan.
    
    def sapa_dulu(func):
        def sapa(*args, **kwargs):
            return f"Halo, {func(*args, **kwargs)}"
        return sapa

    @sapa_dulu
    def ngajak_main(target):
        return f"Main yuk, {target}!"

    ngajak_main("danu")

    # 2. Buatlah decorator `@print_border` yang memberikan garis putus-putus "---" sebelum dan sesudah output fungsi.

    def print_border(func):
        def border(*args, **kwargs):
            print("-" * 20)
            func(*args, **kwargs)
            print("-" * 20)
        return border

    @print_border
    def selamat_datang():
        print("Selamat Datang di Toko Kami")

    selamat_datang()

    # 3. Buatlah decorator yang mengubah hasil return fungsi string menjadi HURUF KAPITAL semua (uppercase).

    def kapital(func):
        def wrapper(*args, **kwargs):
            hasil = func(*args, **kwargs)
            if isinstance(hasil, str):
                return hasil.upper()
            return hasil
        return wrapper

    @kapital
    def selamat_tinggal(teks):
        return teks

    Teks = "Halo"
    print(selamat_tinggal(Teks))

    # 4. Gunakan decorator dari soal no 1 pada sebuah fungsi `def perkenalan(nama): print(nama)`.

    def sapa_dulu_engga_sih(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    
    @sapa_dulu_engga_sih
    def perkenalan(nama):
        return f"Perkenalkan, saya {nama}"

    print(perkenalan("Danu"))

    # 6. Buatlah decorator `@hanya_int` yang mengecek apakah semua argumen yang dimasukkan ke fungsi adalah integer. Jika bukan, print "Input harus angka!".

    def hanya_int(func):
        def wrapper(*args, **kwargs):
            hasil = func(*args, **kwargs)
            if not isinstance(hasil, int):
                print("Input harus angka!")
            return hasil
        return wrapper

    @hanya_int
    def cek_angka(input):
        return input

    print(cek_angka(10))

    # 7. Buatlah decorator `@diulang_dua_kali` yang menjalankan fungsi yang didekorasi sebanyak 2 kali.

    def diulang_dua_kali(n):
        def pengganda(func):
            def wrapper(*args, **kwargs):
                for _ in range(n):
                    func()
            return wrapper
        return pengganda

    @diulang_dua_kali(2)
    def halo():
        print("Halo")

    halo()

    # 8. Buatlah decorator yang menghitung berapa kali sebuah fungsi dipanggil (Hint: gunakan atribut fungsi seperti `wrapper.calls = 0`).

    def counter(func):
        def wrapper(*args, **kwargs):
            wrapper.calls += 1
            print(wrapper.calls)
            return func()
        wrapper.calls = 0
        return wrapper

    @counter
    def tester():
        return 1

    for _ in range(5):
        tester()

    # 9. Buat decorator yang bisa memodifikasi return value: jika hasilnya angka, kalikan dengan 2.

    def pengganda(func):
        def wrapper(*args, **kwargs):
            hasil = isinstance(func(*args, **kwargs), (float, int))
            if hasil:
                total = func(*args, *kwargs) * 2
            return total
        return wrapper

    @pengganda
    def angka(input):
        return input

    # 10. Gabungkan dua decorator sekaligus pada satu fungsi (Stacked Decorators). Misal `@upper` dan `@strip`.

    box = []
    def upper(func):
        def wrapper(*args, **kwargs):
            hasil = func(*args, *kwargs)
            hasil = hasil.upper()
            return hasil
        return wrapper

    def split(func):
        def wrapper(*args, **kwargs):
            hasil = func(*args, **kwargs).split(" ")
            for i in hasil:
                box.append(i)
            return ""
        return wrapper

    @split
    @upper
    def teks(txt):
        return txt

    print(teks("Halo bang ganteng"))
    print(box)

    # Decorator @konversi_rupiah: Buat decorator yang mengubah hasil return fungsi (berupa angka) menjadi string format Rupiah. Contoh: 5000 menjadi Rp 5.000.

    def konversi_rupiah(func):
        def wrapper(*args, **kwargs):
            uang = "{:,}".format(func(*args, **kwargs)).replace(",", ".")
            return f"Rp{uang}"
        return wrapper
    
    @konversi_rupiah
    def input_uang(uang):
        return uang

    print(input_uang(5000))

    # Decorator @limit_panggilan(n): Buat decorator factory yang membatasi sebuah fungsi hanya boleh dipanggil maksimal n kali. Jika lebih, print "Batas panggilan tercapai!".

    def limit_panggilan(n):
        def konversi_rupiah(func):
            def wrapper(*args, **kwargs):
                nonlocal n
                if n > 0:
                    uang = "{:,}".format(func(*args, **kwargs)).replace(",", ".")
                    n -= 1
                    return f"Rp{uang}"
                else:
                    return "Batas panggilan tercapai!"
            return wrapper
        return konversi_rupiah

    @limit_panggilan(5)
    def input_uang(uang):
        return uang

    for i in range(20):
        output = input_uang(50000)
        print(output)
        if output == "Batas panggilan tercapai!":
            break
    
    # Decorator @sensor_kata(daftar_kata) Buat decorator yang menerima list kata-kata kasar/rahasia. Jika fungsi mengembalikan string yang mengandung kata tersebut, ganti kata tersebut dengan tanda bintang (***).

    def sensor_kata(daftar_kata):
        def decorator(func):
            def wrapper(*args, **kwargs):
                hasil = func(*args, **kwargs)
                hasil_baru = []
                for item in hasil:
                    if item.lower() in daftar_kata:
                        hasil_baru.append("***")
                    else:
                        hasil_baru.append(item)
                return hasil_baru
            return wrapper
        return decorator

    @sensor_kata(["kasar", "rahasia"])
    def cek_list(content):
        return content

    data = ["Rahasia", "Kasar", "Bahagia", "Buku"]
    print(cek_list(data))

    # Decorator @hanya_admin: Bayangkan ada variabel global USER_ROLE = "guest". Buat decorator yang mengecek variabel tersebut. Jika bukan "admin", fungsi tidak boleh dijalankan dan print "Akses Ditolak!".

    USER_ROLE = "Guest"
    def hanya_admin(func):
        def wrapper(*args, **kwargs):
            if USER_ROLE.lower() != "admin":
                print("Akses ditolak!")
                return None
            return func(*args, **kwargs)
        return wrapper

    @hanya_admin
    def hapus_data():
        print("Data dihapus")

    # Decorator @log_ke_file Buat decorator yang mencatat setiap kali fungsi dipanggil ke dalam file aktivitas.log dengan format: [TANGGAL/WAKTU] Fungsi <nama_fungsi> dipanggil.

    from datetime import datetime
    from functools import wraps

    def log_ke_file(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                with open("aktivitas.log", "a") as file:
                    file.write(f"[{waktu}] Fungsi {func.__name__} dipanggil\n")
                return func(*args, **kwargs)
            except:
                with open("aktivitas.log", "w") as file:
                    file.write(f"[{waktu}] Fungsi {func.__name__} dipanggil\n")
                return func(*args, **kwargs)
        return wrapper

    @log_ke_file
    def input_uang(uang):
        return uang

    input_uang(5000)
    input_uang(10000)