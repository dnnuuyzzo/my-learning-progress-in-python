"""
===============================================
FUNGSI DI PYTHON
===============================================

Fungsi adalah blok kode yang bisa dipanggil berulang kali.
"""

# =====================================
# 1. MENDEFINISIKAN FUNGSI
# =====================================

def sapa():
    print("Halo, Selamat Datang!")

sapa()  # Memanggil fungsi

# =====================================
# 2. FUNGSI DENGAN PARAMETER
# =====================================

def sapa_nama(nama):
    print(f"Halo, {nama}!")

sapa_nama("Budi")
sapa_nama("Ani")

# =====================================
# 3. FUNGSI DENGAN RETURN
# =====================================

def tambah(a, b):
    return a + b

hasil = tambah(5, 3)
print(f"5 + 3 = {hasil}")

# Multiple return values
def operasi_matematika(a, b):
    return a + b, a - b, a * b, a / b

jumlah, kurang, kali, bagi = operasi_matematika(10, 2)
print(f"Jumlah: {jumlah}, Kurang: {kurang}")

# =====================================
# 4. DEFAULT PARAMETER
# =====================================

def sapa_lengkap(nama, salam="Halo"):
    print(f"{salam}, {nama}!")

sapa_lengkap("Budi")           # Halo, Budi!
sapa_lengkap("Ani", "Selamat") # Selamat, Ani!

# =====================================
# 5. KEYWORD ARGUMENTS
# =====================================

def profil(nama, umur, kota):
    print(f"Nama: {nama}, Umur: {umur}, Kota: {kota}")

profil("Budi", 25, "Jakarta")
profil(kota="Bandung", nama="Ani", umur=22)  # Urutan bebas

# =====================================
# 6. *ARGS (Variadic Positional)
# =====================================

def jumlahkan(*angka):
    total = 0
    for n in angka:
        total += n
    return total

print(f"Jumlah 1,2,3: {jumlahkan(1, 2, 3)}")
print(f"Jumlah 1-5: {jumlahkan(1, 2, 3, 4, 5)}")

# =====================================
# 7. **KWARGS (Variadic Keyword)
# =====================================

def tampilkan_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

tampilkan_info(nama="Budi", umur=25, pekerjaan="Developer")

# =====================================
# 8. KOMBINASI PARAMETER
# =====================================

def fungsi_lengkap(a, b, *args, nama="default", **kwargs):
    print(f"a={a}, b={b}")
    print(f"args: {args}")
    print(f"nama: {nama}")
    print(f"kwargs: {kwargs}")

fungsi_lengkap(1, 2, 3, 4, nama="test", x=10, y=20)

# =====================================
# 9. DOCSTRING
# =====================================

def hitung_luas_persegi(sisi):
    """
    Menghitung luas persegi.
    
    Args:
        sisi: Panjang sisi persegi
        
    Returns:
        Luas persegi (sisi * sisi)
    """
    return sisi * sisi

print(hitung_luas_persegi.__doc__)
help(hitung_luas_persegi)

# =====================================
# LATIHAN
# =====================================

"""
Latihan 1: Buat fungsi untuk menghitung BMI
Latihan 2: Buat fungsi untuk mengecek bilangan prima
Latihan 3: Buat fungsi dengan *args untuk mencari nilai max
"""
