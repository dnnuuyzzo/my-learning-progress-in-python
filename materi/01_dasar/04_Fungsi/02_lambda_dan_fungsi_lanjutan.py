"""
===============================================
LAMBDA DAN FUNGSI LANJUTAN
===============================================
"""

# =====================================
# 1. LAMBDA (Anonymous Function)
# =====================================

# Fungsi biasa
def kuadrat(x):
    return x ** 2

# Lambda equivalent
kuadrat_lambda = lambda x: x ** 2

print(f"kuadrat(5): {kuadrat(5)}")
print(f"kuadrat_lambda(5): {kuadrat_lambda(5)}")

# Lambda dengan multiple parameter
tambah = lambda a, b: a + b
print(f"tambah(3, 4): {tambah(3, 4)}")

# =====================================
# 2. MAP()
# =====================================

angka = [1, 2, 3, 4, 5]

# Dengan fungsi biasa
def kali_dua(x):
    return x * 2

hasil = list(map(kali_dua, angka))
print(f"map dengan fungsi: {hasil}")

# Dengan lambda
hasil = list(map(lambda x: x * 2, angka))
print(f"map dengan lambda: {hasil}")

# =====================================
# 3. FILTER()
# =====================================

angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter genap
genap = list(filter(lambda x: x % 2 == 0, angka))
print(f"Angka genap: {genap}")

# =====================================
# 4. REDUCE()
# =====================================

from functools import reduce

angka = [1, 2, 3, 4, 5]

# Menjumlahkan semua
total = reduce(lambda a, b: a + b, angka)
print(f"Reduce (jumlah): {total}")

# Factorial dengan reduce
factorial_5 = reduce(lambda a, b: a * b, range(1, 6))
print(f"5! = {factorial_5}")

# =====================================
# 5. SORTED() DENGAN KEY
# =====================================

siswa = [
    {"nama": "Budi", "nilai": 85},
    {"nama": "Ani", "nilai": 92},
    {"nama": "Cici", "nilai": 78}
]

# Sort berdasarkan nilai
terurut = sorted(siswa, key=lambda x: x["nilai"], reverse=True)
print("Urutan nilai tertinggi:")
for s in terurut:
    print(f"  {s['nama']}: {s['nilai']}")

# =====================================
# 6. CLOSURE
# =====================================

def buat_pengali(n):
    def pengali(x):
        return x * n
    return pengali

kali_3 = buat_pengali(3)
kali_5 = buat_pengali(5)

print(f"kali_3(10): {kali_3(10)}")
print(f"kali_5(10): {kali_5(10)}")

# =====================================
# 7. DECORATOR
# =====================================

def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Memanggil fungsi: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Selesai memanggil: {func.__name__}")
        return result
    return wrapper

@logging_decorator
def sapa(nama):
    print(f"Halo, {nama}!")

sapa("Budi")

# =====================================
# 8. GENERATOR
# =====================================

def hitungan(n):
    for i in range(n):
        yield i

for num in hitungan(5):
    print(num, end=" ")
print()

# Generator expression
gen = (x**2 for x in range(5))
print(f"Generator: {list(gen)}")

# =====================================
# 9. RECURSION
# =====================================

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"5! = {factorial(5)}")

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(f"Fibonacci(10): {fibonacci(10)}")
