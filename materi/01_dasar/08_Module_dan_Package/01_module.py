"""
===============================================
MODULE DAN PACKAGE DI PYTHON
===============================================
"""

# =====================================
# 1. IMPORT MODULE BUILT-IN
# =====================================

import math
print(f"PI: {math.pi}")
print(f"sqrt(16): {math.sqrt(16)}")

# Import dengan alias
import datetime as dt
print(f"Sekarang: {dt.datetime.now()}")

# Import fungsi spesifik
from random import randint, choice
print(f"Random 1-100: {randint(1, 100)}")
print(f"Choice: {choice(['A', 'B', 'C'])}")

# =====================================
# 2. MODULE PENTING
# =====================================

# os - Operasi sistem
import os
print(f"Current dir: {os.getcwd()}")

# sys - Sistem Python
import sys
print(f"Python version: {sys.version}")

# random
import random
print(f"Random float: {random.random()}")

# collections
from collections import Counter
kata = "abracadabra"
print(f"Counter: {Counter(kata)}")

# =====================================
# 3. MEMBUAT MODULE SENDIRI
# =====================================

"""
Buat file: my_module.py
---
def sapa(nama):
    return f"Halo, {nama}!"

PI = 3.14159
---

Kemudian import:
import my_module
print(my_module.sapa("Budi"))
"""

# =====================================
# 4. PACKAGE
# =====================================

"""
Struktur package:
my_package/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        module3.py

Import:
from my_package import module1
from my_package.subpackage import module3
"""

# =====================================
# 5. __name__ DAN __main__
# =====================================

def main():
    print("Ini fungsi utama")

if __name__ == "__main__":
    # Hanya dijalankan jika file ini dieksekusi langsung
    main()
