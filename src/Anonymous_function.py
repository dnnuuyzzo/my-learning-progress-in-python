"""
================================================================================
                    ANONYMOUS FUNCTION (LAMBDA) DI PYTHON
================================================================================

DAFTAR ISI:
1. Pengertian Anonymous Function
2. Syntax Lambda Function
3. Karakteristik Lambda Function
4. Perbedaan Lambda vs Function Biasa
5. Penggunaan Lambda dengan Built-in Functions
6. Lambda dengan Multiple Arguments
7. Lambda dalam Conditional Expression
8. Lambda dengan Higher-Order Functions
9. Closure dalam Lambda
10. Best Practices dan Kapan Menggunakan Lambda
11. 15 LATIHAN SOAL BERLEVEL

================================================================================
"""

# ============================================================================
# 1. PENGERTIAN ANONYMOUS FUNCTION
# ============================================================================

"""
Anonymous Function (Fungsi Anonim) adalah fungsi yang didefinisikan tanpa nama.
Di Python, anonymous function dibuat menggunakan keyword 'lambda'.

Disebut "anonim" karena:
- Tidak memiliki nama (tidak menggunakan 'def')
- Biasanya digunakan untuk operasi sederhana
- Sering digunakan sebagai argumen untuk fungsi lain
- Bersifat sementara (one-time use)

Keuntungan:
✓ Kode lebih ringkas dan readable untuk operasi sederhana
✓ Tidak perlu mendefinisikan fungsi terpisah untuk operasi kecil
✓ Cocok untuk functional programming
✓ Mengurangi namespace pollution

Kekurangan:
✗ Hanya bisa berisi satu expression
✗ Tidak bisa menggunakan statements (print, assignment, dll)
✗ Sulit di-debug karena tidak punya nama
✗ Kurang readable untuk logika kompleks
"""

# ============================================================================
# 2. SYNTAX LAMBDA FUNCTION
# ============================================================================

"""
SYNTAX DASAR:
lambda arguments: expression

Komponen:
- lambda      : keyword untuk membuat anonymous function
- arguments   : parameter input (bisa 0, 1, atau lebih)
- :           : pemisah antara parameter dan expression
- expression  : operasi yang akan dilakukan (hanya 1 expression)

Return value: hasil dari expression secara otomatis di-return
"""

# Contoh 1: Lambda tanpa argument
greet = lambda: "Hello, World!"
print(greet())  # Output: Hello, World!

# Contoh 2: Lambda dengan 1 argument
square = lambda x: x ** 2
print(square(5))  # Output: 25

# Contoh 3: Lambda dengan 2 arguments
add = lambda x, y: x + y
print(add(3, 7))  # Output: 10

# Contoh 4: Lambda dengan 3 arguments
volume = lambda p, l, t: p * l * t
print(volume(5, 3, 2))  # Output: 30

# ============================================================================
# 3. KARAKTERISTIK LAMBDA FUNCTION
# ============================================================================

"""
KARAKTERISTIK PENTING:

1. SINGLE EXPRESSION
   - Hanya boleh berisi SATU expression
   - Tidak boleh menggunakan statements (if-else statement, loops, dll)
   - Expression otomatis di-return (tidak perlu keyword 'return')

2. ANONYMOUS (TANPA NAMA)
   - Tidak memiliki nama fungsi
   - Bisa disimpan dalam variabel
   - Bisa digunakan langsung tanpa disimpan

3. INLINE FUNCTION
   - Didefinisikan di tempat penggunaannya
   - Cocok untuk operasi sederhana dan sementara

4. FUNCTIONAL PROGRAMMING
   - Sering digunakan dengan map(), filter(), reduce()
   - Mendukung paradigma functional programming
"""

# Contoh: Lambda hanya bisa single expression
# BENAR ✓
is_even = lambda x: x % 2 == 0
print(is_even(4))  # Output: True

# SALAH ✗ (tidak bisa multi-line atau statement)
# wrong_lambda = lambda x:
#     result = x * 2
#     return result

# ============================================================================
# 4. PERBEDAAN LAMBDA VS FUNCTION BIASA
# ============================================================================

"""
PERBANDINGAN LAMBDA vs DEF FUNCTION:

┌─────────────────────┬──────────────────────┬──────────────────────┐
│ Aspek               │ Lambda Function      │ Def Function         │
├─────────────────────┼──────────────────────┼──────────────────────┤
│ Nama                │ Anonim (tanpa nama)  │ Memiliki nama        │
│ Keyword             │ lambda               │ def                  │
│ Expression          │ Hanya 1 expression   │ Multiple statements  │
│ Return              │ Implicit return      │ Explicit return      │
│ Panjang kode        │ 1 baris              │ Multiple lines       │
│ Kompleksitas        │ Operasi sederhana    │ Operasi kompleks     │
│ Debugging           │ Sulit                │ Mudah                │
│ Dokumentasi         │ Tidak ada docstring  │ Bisa ada docstring   │
│ Reusability         │ Terbatas             │ Tinggi               │
└─────────────────────┴──────────────────────┴──────────────────────┘
"""

# Contoh perbandingan:

# Menggunakan DEF (Function biasa)
def multiply_def(x, y):
    """Mengalikan dua angka"""
    return x * y

# Menggunakan LAMBDA
multiply_lambda = lambda x, y: x * y

# Keduanya menghasilkan output yang sama
print(multiply_def(4, 5))      # Output: 20
print(multiply_lambda(4, 5))   # Output: 20

# Contoh lain: Cek bilangan genap
# DEF version
def is_even_def(n):
    return n % 2 == 0

# LAMBDA version
is_even_lambda = lambda n: n % 2 == 0

print(is_even_def(10))      # Output: True
print(is_even_lambda(10))   # Output: True

# ============================================================================
# 5. PENGGUNAAN LAMBDA DENGAN BUILT-IN FUNCTIONS
# ============================================================================

"""
Lambda sangat powerful ketika dikombinasikan dengan built-in functions:
- map()     : Menerapkan fungsi ke setiap elemen
- filter()  : Menyaring elemen berdasarkan kondisi
- sorted()  : Mengurutkan dengan custom key
- reduce()  : Menggabungkan elemen menjadi satu nilai
"""

# ─────────────────────────────────────────────────────────────────────────
# A. LAMBDA dengan MAP()
# ─────────────────────────────────────────────────────────────────────────
"""
map(function, iterable)
- Menerapkan function ke setiap elemen dalam iterable
- Return: map object (perlu dikonversi ke list/tuple)
"""

numbers = [1, 2, 3, 4, 5]

# Mengkuadratkan setiap angka
squared = list(map(lambda x: x ** 2, numbers))
print(f"Original: {numbers}")
print(f"Squared: {squared}")
# Output: [1, 4, 9, 16, 25]

# Mengubah ke uppercase
words = ["hello", "world", "python"]
uppercase = list(map(lambda x: x.upper(), words))
print(f"Uppercase: {uppercase}")
# Output: ['HELLO', 'WORLD', 'PYTHON']

# Map dengan multiple iterables
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums3 = [7, 8, 9]
sums = list(map(lambda x, y, z: x + y, nums1, nums2, nums3))
print(f"Sums: {sums}")
# Output: [5, 7, 9]

# ─────────────────────────────────────────────────────────────────────────
# B. LAMBDA dengan FILTER()
# ─────────────────────────────────────────────────────────────────────────
"""
filter(function, iterable)
- Menyaring elemen yang memenuhi kondisi (return True)
- Return: filter object (perlu dikonversi ke list/tuple)
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter bilangan genap
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")
# Output: [2, 4, 6, 8, 10]

# Filter bilangan > 5
greater_than_5 = list(filter(lambda x: x > 5, numbers))
print(f"Greater than 5: {greater_than_5}")
# Output: [6, 7, 8, 9, 10]

# Filter string yang panjangnya > 5
words = ["cat", "elephant", "dog", "butterfly", "ant"]
long_words = list(filter(lambda x: len(x) > 5, words))
print(f"Long words: {long_words}")
# Output: ['elephant', 'butterfly']

# ─────────────────────────────────────────────────────────────────────────
# C. LAMBDA dengan SORTED()
# ─────────────────────────────────────────────────────────────────────────
"""
sorted(iterable, key=function)
- Mengurutkan elemen berdasarkan custom key
- key: fungsi yang menentukan nilai untuk sorting
"""

# Sort berdasarkan panjang string
words = ["python", "is", "awesome", "and", "powerful"]
sorted_by_length = sorted(words, key=lambda x: len(x))
print(f"Sorted by length: {sorted_by_length}")
# Output: ['is', 'and', 'python', 'awesome', 'powerful']

# Sort tuple berdasarkan elemen kedua
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("Diana", 95)]
sorted_by_score = sorted(students, key=lambda x: x[1], reverse=True)
print(f"Sorted by score: {sorted_by_score}")
# Output: [('Diana', 95), ('Bob', 92), ('Alice', 85), ('Charlie', 78)]

# Sort dictionary berdasarkan value
data = {"apple": 5, "banana": 2, "cherry": 8, "date": 1}
sorted_dict = dict(sorted(data.items(), key=lambda x: x[1]))
print(f"Sorted dict: {sorted_dict}")
# Output: {'date': 1, 'banana': 2, 'apple': 5, 'cherry': 8}

# ─────────────────────────────────────────────────────────────────────────
# D. LAMBDA dengan REDUCE()
# ─────────────────────────────────────────────────────────────────────────
"""
reduce(function, iterable)
- Menggabungkan elemen secara berurutan menjadi satu nilai
- Perlu import dari functools
"""

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Menjumlahkan semua elemen
total = reduce(lambda x, y: x + y, numbers)
print(f"Sum: {total}")
# Output: 15

# Mengalikan semua elemen
product = reduce(lambda x, y: x * y, numbers)
print(f"Product: {product}")
# Output: 120

# Mencari nilai maksimum
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(f"Maximum: {maximum}")
# Output: 5

# ============================================================================
# 6. LAMBDA DENGAN MULTIPLE ARGUMENTS
# ============================================================================

"""
Lambda bisa menerima multiple arguments seperti function biasa.
Syntax: lambda arg1, arg2, arg3, ...: expression
"""

# Lambda dengan 2 arguments
add = lambda a, b: a + b
print(add(10, 20))  # Output: 30

# Lambda dengan 3 arguments
calculate_average = lambda a, b, c: (a + b + c) / 3
print(calculate_average(80, 90, 85))  # Output: 85.0

# Lambda dengan 4 arguments
rectangle_info = lambda p, l, action: p * l if action == "area" else 2 * (p + l)
print(rectangle_info(5, 3, "area"))       # Output: 15
print(rectangle_info(5, 3, "perimeter"))  # Output: 16

# Lambda dengan *args (variable arguments)
sum_all = lambda *args: sum(args)
print(sum_all(1, 2, 3, 4, 5))  # Output: 15

# Lambda dengan **kwargs (keyword arguments)
greet_person = lambda **kwargs: f"Hello {kwargs.get('name', 'Guest')}, you are {kwargs.get('age', 'unknown')} years old"
print(greet_person(name="Alice", age=25))
# Output: Hello Alice, you are 25 years old

# ============================================================================
# 7. LAMBDA DALAM CONDITIONAL EXPRESSION
# ============================================================================

"""
Lambda bisa menggunakan conditional expression (ternary operator):
Syntax: lambda x: value_if_true if condition else value_if_false

CATATAN: Ini adalah EXPRESSION, bukan STATEMENT
"""

# Contoh 1: Cek genap/ganjil
check_parity = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check_parity(4))   # Output: Even
print(check_parity(7))   # Output: Odd

# Contoh 2: Cek positif/negatif/nol
check_sign = lambda x: "Positive" if x > 0 else ("Negative" if x < 0 else "Zero")
print(check_sign(10))    # Output: Positive
print(check_sign(-5))    # Output: Negative
print(check_sign(0))     # Output: Zero

# Contoh 3: Grade calculator
get_grade = lambda score: "A" if score >= 90 else ("B" if score >= 80 else ("C" if score >= 70 else ("D" if score >= 60 else "F")))
print(get_grade(95))     # Output: A
print(get_grade(75))     # Output: C
print(get_grade(55))     # Output: F

# Contoh 4: Discount calculator
calculate_discount = lambda price, is_member: price * 0.8 if is_member else price * 0.9
print(calculate_discount(100, True))   # Output: 80.0 (20% discount)
print(calculate_discount(100, False))  # Output: 90.0 (10% discount)

# Contoh 5: Max of two numbers
max_of_two = lambda a, b: a if a > b else b
print(max_of_two(15, 23))  # Output: 23

# ============================================================================
# 8. LAMBDA DENGAN HIGHER-ORDER FUNCTIONS
# ============================================================================

"""
Higher-Order Function adalah fungsi yang:
- Menerima fungsi lain sebagai argument, ATAU
- Mengembalikan fungsi sebagai return value

Lambda sangat cocok digunakan dengan higher-order functions.
"""

# ─────────────────────────────────────────────────────────────────────────
# A. Lambda sebagai Argument
# ─────────────────────────────────────────────────────────────────────────

def apply_operation(x, y, operation):
    """Menerapkan operasi pada x dan y"""
    return operation(x, y)

# Menggunakan lambda sebagai argument
result1 = apply_operation(10, 5, lambda a, b: a + b)
result2 = apply_operation(10, 5, lambda a, b: a - b)
result3 = apply_operation(10, 5, lambda a, b: a * b)
result4 = apply_operation(10, 5, lambda a, b: a / b)

print(f"Addition: {result1}")        # Output: 15
print(f"Subtraction: {result2}")     # Output: 5
print(f"Multiplication: {result3}")  # Output: 50
print(f"Division: {result4}")        # Output: 2.0

# ─────────────────────────────────────────────────────────────────────────
# B. Function yang Mengembalikan Lambda
# ─────────────────────────────────────────────────────────────────────────

def power_function(n):
    """Mengembalikan fungsi yang memangkatkan dengan n"""
    return lambda x: x ** n

# Membuat fungsi pangkat 2, 3, dan 4
square = power_function(2)
cube = power_function(3)
fourth_power = power_function(4)

print(square(5))        # Output: 25
print(cube(5))          # Output: 125
print(fourth_power(5))  # Output: 625

# Contoh lain: Multiplier generator
def multiplier(n):
    """Mengembalikan fungsi yang mengalikan dengan n"""
    return lambda x: x * n

double = multiplier(2)
triple = multiplier(3)
times_ten = multiplier(10)

print(double(7))      # Output: 14
print(triple(7))      # Output: 21
print(times_ten(7))   # Output: 70

# ─────────────────────────────────────────────────────────────────────────
# C. Chaining Lambda Functions
# ─────────────────────────────────────────────────────────────────────────

# Membuat pipeline of operations
operations = [
    lambda x: x + 10,
    lambda x: x * 2,
    lambda x: x - 5
]

def apply_pipeline(value, ops):
    """Menerapkan serangkaian operasi secara berurutan"""
    for op in ops:
        value = op(value)
    return value

result = apply_pipeline(5, operations)
print(f"Pipeline result: {result}")
# 5 -> +10 = 15 -> *2 = 30 -> -5 = 25
# Output: 25

# ============================================================================
# 9. CLOSURE DALAM LAMBDA
# ============================================================================

"""
Closure adalah fungsi yang "mengingat" variabel dari scope di mana ia dibuat,
bahkan setelah scope tersebut selesai dieksekusi.

Lambda bisa membentuk closure dengan mengakses variabel dari outer scope.
"""

def make_multiplier(n):
    """Membuat fungsi multiplier dengan closure"""
    # Lambda ini "mengingat" nilai n
    return lambda x: x * n

# Membuat multiplier dengan nilai n yang berbeda
times_5 = make_multiplier(5)
times_10 = make_multiplier(10)

print(times_5(3))   # Output: 15 (3 * 5)
print(times_10(3))  # Output: 30 (3 * 10)

# Contoh lain: Counter dengan closure
def make_counter():
    """Membuat counter dengan closure"""
    count = [0]  # Menggunakan list agar mutable
    return lambda: count.__setitem__(0, count[0] + 1) or count[0]

counter1 = make_counter()
counter2 = make_counter()

print(counter1())  # Output: 1
print(counter1())  # Output: 2
print(counter2())  # Output: 1 (counter terpisah)
print(counter1())  # Output: 3

# Contoh: Greeting dengan closure
def make_greeter(greeting):
    """Membuat fungsi greeter dengan closure"""
    return lambda name: f"{greeting}, {name}!"

say_hello = make_greeter("Hello")
say_hi = make_greeter("Hi")
say_good_morning = make_greeter("Good morning")

print(say_hello("Alice"))           # Output: Hello, Alice!
print(say_hi("Bob"))                # Output: Hi, Bob!
print(say_good_morning("Charlie"))  # Output: Good morning, Charlie!

# ============================================================================
# 10. BEST PRACTICES DAN KAPAN MENGGUNAKAN LAMBDA
# ============================================================================

"""
KAPAN MENGGUNAKAN LAMBDA:
✓ Operasi sederhana yang hanya butuh 1 expression
✓ Sebagai argument untuk map(), filter(), sorted(), dll
✓ Callback functions yang sederhana
✓ One-time use functions
✓ Functional programming patterns

KAPAN TIDAK MENGGUNAKAN LAMBDA:
✗ Logika kompleks yang butuh multiple statements
✗ Fungsi yang akan digunakan berulang kali (lebih baik def)
✗ Fungsi yang butuh dokumentasi (docstring)
✗ Debugging yang kompleks
✗ Readability lebih penting daripada brevity

BEST PRACTICES:
1. Keep it simple - Lambda untuk operasi sederhana saja
2. Prefer readability - Jika lambda membuat kode sulit dibaca, gunakan def
3. Avoid complex logic - Jangan paksa logika kompleks ke dalam lambda
4. Use meaningful variable names - Meskipun singkat, tetap jelas
5. Don't nest too deep - Hindari nested lambda yang berlebihan
"""

# ❌ BAD: Lambda terlalu kompleks
bad_lambda = lambda x: (x * 2 if x > 0 else x * -2) if x != 0 else 0 if isinstance(x, int) else None

# ✅ GOOD: Gunakan def untuk logika kompleks
def process_number(x):
    """Process number with complex logic"""
    if not isinstance(x, int):
        return None
    if x == 0:
        return 0
    return x * 2 if x > 0 else x * -2

# ❌ BAD: Lambda untuk fungsi yang sering digunakan
# calculate_tax = lambda price: price * 0.1  # Akan digunakan berkali-kali

# ✅ GOOD: Gunakan def untuk reusability
def calculate_tax(price):
    """Calculate 10% tax on price"""
    return price * 0.1

# ✅ GOOD: Lambda untuk one-time use dengan map/filter
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))

# ✅ GOOD: Lambda sebagai key function
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_students = sorted(students, key=lambda x: x[1])

"""
RINGKASAN MATERI:

1. Lambda adalah anonymous function (fungsi tanpa nama)
2. Syntax: lambda arguments: expression
3. Hanya bisa berisi SATU expression
4. Sangat berguna dengan map(), filter(), sorted(), reduce()
5. Bisa menerima multiple arguments
6. Bisa menggunakan conditional expression (ternary)
7. Cocok untuk higher-order functions
8. Bisa membentuk closure
9. Gunakan untuk operasi sederhana, hindari untuk logika kompleks
10. Prioritaskan readability daripada brevity
"""

# ============================================================================
# 11. 15 LATIHAN SOAL BERLEVEL
# ============================================================================

"""
================================================================================
                            LATIHAN SOAL
================================================================================

INSTRUKSI:
- Kerjakan soal sesuai dengan level (Easy → Medium → Hard)
- Tulis kode di bawah setiap soal
- Test kode Anda untuk memastikan hasilnya benar
- Jangan melihat jawaban sebelum mencoba sendiri

================================================================================
LEVEL 1: EASY (Soal 1-5)
================================================================================
Soal-soal dasar untuk memahami syntax dan penggunaan lambda sederhana.
"""

# ─────────────────────────────────────────────────────────────────────────
# SOAL 1: Lambda Dasar
# ─────────────────────────────────────────────────────────────────────────
"""
Buatlah lambda function yang:
- Menerima 1 parameter (angka)
- Mengembalikan hasil angka tersebut dikali 3

Test case:
- Input: 5 → Output: 15
- Input: 10 → Output: 30
- Input: -3 → Output: -9
"""

# Tulis kode Anda di sini:
soal_1 = lambda x: x * 3



# ─────────────────────────────────────────────────────────────────────────
# SOAL 2: Lambda dengan String
# ─────────────────────────────────────────────────────────────────────────
"""
Buatlah lambda function yang:
- Menerima 1 parameter (string)
- Mengembalikan panjang string tersebut

Test case:
- Input: "Python" → Output: 6
- Input: "Hello World" → Output: 11
- Input: "" → Output: 0
"""

# Tulis kode Anda di sini:
soal_2 = lambda x: len(x)



# ─────────────────────────────────────────────────────────────────────────
# SOAL 3: Lambda dengan 2 Parameter
# ─────────────────────────────────────────────────────────────────────────
"""
Buatlah lambda function yang:
- Menerima 2 parameter (angka)
- Mengembalikan hasil pembagian parameter pertama dengan parameter kedua

Test case:
- Input: (10, 2) → Output: 5.0
- Input: (15, 3) → Output: 5.0
- Input: (7, 2) → Output: 3.5
"""

# Tulis kode Anda di sini:
soal_3 = lambda x, y: x / y



# ─────────────────────────────────────────────────────────────────────────
# SOAL 4: Lambda dengan Conditional
# ─────────────────────────────────────────────────────────────────────────
"""
Buatlah lambda function yang:
- Menerima 1 parameter (angka)
- Mengembalikan "Positive" jika angka > 0, "Negative" jika angka < 0, 
  dan "Zero" jika angka = 0

Test case:
- Input: 5 → Output: "Positive"
- Input: -3 → Output: "Negative"
- Input: 0 → Output: "Zero"
"""

# Tulis kode Anda di sini:
soal_4 = lambda x: "Positive" if x > 0 else ("Negative" if x < 0 else "Zero")



# ─────────────────────────────────────────────────────────────────────────
# SOAL 5: Lambda dengan Map
# ─────────────────────────────────────────────────────────────────────────
"""
Gunakan lambda dengan map() untuk:
- Mengubah list angka [1, 2, 3, 4, 5]
- Setiap angka ditambah 10
- Simpan hasilnya dalam list baru

Test case:
- Input: [1, 2, 3, 4, 5]
- Output: [11, 12, 13, 14, 15]
"""

# Tulis kode Anda di sini:
angka = [1, 2, 3, 4, 5]
soal_5 = list(map(lambda x: x + 10, angka))



"""
================================================================================
LEVEL 2: MEDIUM (Soal 6-10)
================================================================================
Soal-soal menengah yang menggabungkan lambda dengan berbagai fungsi built-in.
"""

# ─────────────────────────────────────────────────────────────────────────
# SOAL 6: Lambda dengan Filter
# ─────────────────────────────────────────────────────────────────────────
"""
Gunakan lambda dengan filter() untuk:
- Menyaring list angka [10, 15, 20, 25, 30, 35, 40]
- Hanya ambil angka yang habis dibagi 10
- Simpan hasilnya dalam list baru

Test case:
- Input: [10, 15, 20, 25, 30, 35, 40]
- Output: [10, 20, 30, 40]
"""

# Tulis kode Anda di sini:
angka = [10, 15, 20, 25, 30, 35, 40]
soal_6 = list(filter(lambda x: x % 10, angka))



# ─────────────────────────────────────────────────────────────────────────
# SOAL 7: Lambda dengan Sorted
# ─────────────────────────────────────────────────────────────────────────
"""
Gunakan lambda dengan sorted() untuk:
- Mengurutkan list of tuples berdasarkan elemen kedua (ascending)
- Data: [("Alice", 25), ("Bob", 20), ("Charlie", 30), ("Diana", 22)]

Test case:
- Input: [("Alice", 25), ("Bob", 20), ("Charlie", 30), ("Diana", 22)]
- Output: [("Bob", 20), ("Diana", 22), ("Alice", 25), ("Charlie", 30)]
"""

# Tulis kode Anda di sini:
data = [("Alice", 25), ("Bob", 20), ("Charlie", 30), ("Diana", 22)]
soal_7 = list(sorted(data, key= lambda x: x[1]))



# ─────────────────────────────────────────────────────────────────────────
# SOAL 8: Lambda dengan Reduce
# ─────────────────────────────────────────────────────────────────────────
"""
Gunakan lambda dengan reduce() untuk:
- Mencari nilai maksimum dari list [45, 23, 67, 12, 89, 34]
- Jangan gunakan fungsi max() built-in

Test case:
- Input: [45, 23, 67, 12, 89, 34]
- Output: 89

Hint: Import reduce dari functools
"""

# Tulis kode Anda di sini:
angka = [45, 23, 67, 12, 89, 34]
soal_8 = reduce(lambda x, y: x if x > y else y, angka)



# ─────────────────────────────────────────────────────────────────────────
# SOAL 9: Lambda dengan Multiple Conditions
# ─────────────────────────────────────────────────────────────────────────
"""
Buatlah lambda function yang:
- Menerima 1 parameter (angka/nilai ujian)
- Mengembalikan grade berdasarkan:
  * >= 90: "A"
  * >= 80: "B"
  * >= 70: "C"
  * >= 60: "D"
  * < 60: "F"

Test case:
- Input: 95 → Output: "A"
- Input: 75 → Output: "C"
- Input: 55 → Output: "F"
"""

# Tulis kode Anda di sini:
soal_9 = lambda x: "A" if x >= 90 else ("B" if x >= 80 else ("C" if x >= 70 else ("D" if x >= 60 else "F")))



# ─────────────────────────────────────────────────────────────────────────
# SOAL 10: Lambda dengan Dictionary
# ─────────────────────────────────────────────────────────────────────────
"""
Gunakan lambda dengan sorted() untuk:
- Mengurutkan dictionary berdasarkan value (descending)
- Data: {"apple": 5, "banana": 2, "cherry": 8, "date": 1, "elderberry": 6}
- Return sebagai list of tuples

Test case:
- Input: {"apple": 5, "banana": 2, "cherry": 8, "date": 1, "elderberry": 6}
- Output: [("cherry", 8), ("elderberry", 6), ("apple", 5), ("banana", 2), ("date", 1)]
"""

# Tulis kode Anda di sini:
data = {
    "apple": 5, 
    "banana": 2, 
    "cherry": 8, 
    "date": 1, 
    "elderberry": 6
}

soal_10 = dict(sorted(data.items(), key= lambda x: x[1], reverse= True))
print(soal_10)



"""
================================================================================
LEVEL 3: HARD (Soal 11-15)
================================================================================
Soal-soal advanced yang menggabungkan multiple concepts dan problem solving.
"""

# ─────────────────────────────────────────────────────────────────────────
# SOAL 11: Lambda dengan Map dan Filter
# ─────────────────────────────────────────────────────────────────────────
"""
Gunakan kombinasi map() dan filter() dengan lambda untuk:
1. Ambil list angka [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
2. Filter hanya angka ganjil
3. Kuadratkan setiap angka ganjil tersebut
4. Simpan hasilnya dalam list

Test case:
- Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
- Output: [1, 9, 25, 49, 81]

Hint: Gunakan nested function calls atau chain operations
"""

# Tulis kode Anda di sini:
angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soal_11 = list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, angka)))
print(soal_11)



# ─────────────────────────────────────────────────────────────────────────
# SOAL 12: Higher-Order Function dengan Lambda
# ─────────────────────────────────────────────────────────────────────────
"""
Buatlah function bernama 'create_operation' yang:
- Menerima 1 parameter (string): "add", "subtract", "multiply", atau "divide"
- Mengembalikan lambda function yang sesuai dengan operasi tersebut
- Lambda yang dikembalikan menerima 2 parameter (angka)

Test case:
- add_func = create_operation("add")
  add_func(5, 3) → Output: 8
- multiply_func = create_operation("multiply")
  multiply_func(4, 7) → Output: 28
"""

# Tulis kode Anda di sini:
def create_operation(operasi):
    operasi = operasi.lower()
    if operasi == "add":
        return lambda x, y : x + y
    elif operasi == "subtract":
        return lambda x, y : x - y
    elif operasi == "multiply":
        return lambda x, y : x * y
    elif operasi == "divide":
        return lambda x, y : x / y
    else:
        return "Invalid"

add_func = create_operation("add")
subtract_func = create_operation("subtract")
multiply_func = create_operation("multiply")
divide_func = create_operation("divide")

hasil_add = add_func(5, 3)
hasil_sub = subtract_func(5, 3)
hasil_mul = multiply_func(5, 3)
hasil_div = divide_func(5, 3)



# ─────────────────────────────────────────────────────────────────────────
# SOAL 13: Lambda dengan List Comprehension
# ─────────────────────────────────────────────────────────────────────────
"""
Buatlah list of lambda functions menggunakan list comprehension:
- Buat 5 lambda functions
- Lambda ke-i mengalikan input dengan i (i dari 1 sampai 5)
- Simpan semua lambda dalam list
- Test dengan memanggil setiap lambda dengan input 10

Test case:
- functions[0](10) → Output: 10  (10 * 1)
- functions[1](10) → Output: 20  (10 * 2)
- functions[2](10) → Output: 30  (10 * 3)
- functions[3](10) → Output: 40  (10 * 4)
- functions[4](10) → Output: 50  (10 * 5)

Hint: Gunakan list comprehension dengan lambda dan closure
"""

# Tulis kode Anda di sini:




# ─────────────────────────────────────────────────────────────────────────
# SOAL 14: Complex Data Processing
# ─────────────────────────────────────────────────────────────────────────
"""
Diberikan list of dictionaries berisi data mahasiswa:
students = [
    {"name": "Alice", "scores": [85, 90, 88]},
    {"name": "Bob", "scores": [70, 75, 72]},
    {"name": "Charlie", "scores": [95, 92, 98]},
    {"name": "Diana", "scores": [60, 65, 62]}
]

Gunakan lambda dengan map() dan sorted() untuk:
1. Hitung rata-rata scores untuk setiap mahasiswa
2. Tambahkan key "average" ke setiap dictionary
3. Urutkan mahasiswa berdasarkan rata-rata (descending)
4. Return list of dictionaries yang sudah diurutkan

Test case output:
[
    {"name": "Charlie", "scores": [95, 92, 98], "average": 95.0},
    {"name": "Alice", "scores": [85, 90, 88], "average": 87.67},
    {"name": "Bob", "scores": [70, 75, 72], "average": 72.33},
    {"name": "Diana", "scores": [60, 65, 62], "average": 62.33}
]
"""

# Tulis kode Anda di sini:




# ─────────────────────────────────────────────────────────────────────────
# SOAL 15: Advanced Closure dengan Lambda
# ─────────────────────────────────────────────────────────────────────────
"""
Buatlah function 'create_validator' yang:
- Menerima 2 parameter: min_value dan max_value
- Mengembalikan lambda function yang:
  * Menerima 1 parameter (angka)
  * Return True jika angka berada dalam range [min_value, max_value]
  * Return False jika di luar range

Kemudian gunakan validator ini dengan filter() untuk:
- Filter list [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]
- Ambil hanya angka dalam range 20-70

Test case:
- validator = create_validator(20, 70)
- validator(25) → Output: True
- validator(15) → Output: False
- validator(50) → Output: True

- filtered = list(filter(validator, [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]))
- Output: [25, 35, 45, 55, 65]
"""

# Tulis kode Anda di sini:




"""
================================================================================
                            SELAMAT BELAJAR!
================================================================================

Tips untuk mengerjakan soal:
1. Mulai dari level EASY untuk memahami konsep dasar
2. Jangan terburu-buru, pahami setiap soal dengan baik
3. Test kode Anda dengan berbagai test case
4. Jika stuck, review kembali materi di atas
5. Coba variasikan solusi Anda (ada banyak cara untuk solve)

Setelah selesai:
- Review kode Anda
- Bandingkan dengan best practices
- Coba optimasi solusi Anda
- Eksplorasi use case lain dari lambda

Good luck! 🚀
================================================================================
"""
