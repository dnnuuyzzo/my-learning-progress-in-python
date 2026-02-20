"""
===============================================
EXCEPTION HANDLING DI PYTHON
===============================================
"""

# =====================================
# 1. TRY-EXCEPT DASAR
# =====================================

try:
    hasil = 10 / 0
except ZeroDivisionError:
    print("Error: Tidak bisa membagi dengan nol!")

# =====================================
# 2. MULTIPLE EXCEPTIONS
# =====================================

try:
    x = int("abc")
except (ValueError, TypeError) as e:
    print(f"Error: {e}")

# =====================================
# 3. TRY-EXCEPT-ELSE-FINALLY
# =====================================

try:
    angka = int("123")
except ValueError:
    print("Bukan angka!")
else:
    print(f"Berhasil convert: {angka}")
finally:
    print("Selesai.")

# =====================================
# 4. RAISE EXCEPTION
# =====================================

def set_umur(umur):
    if umur < 0:
        raise ValueError("Umur tidak boleh negatif!")
    return umur

try:
    set_umur(-5)
except ValueError as e:
    print(f"Error: {e}")

# =====================================
# 5. CUSTOM EXCEPTION
# =====================================

class SaldoError(Exception):
    pass

def tarik_uang(saldo, jumlah):
    if jumlah > saldo:
        raise SaldoError("Saldo tidak cukup!")
    return saldo - jumlah

try:
    tarik_uang(100000, 150000)
except SaldoError as e:
    print(e)
