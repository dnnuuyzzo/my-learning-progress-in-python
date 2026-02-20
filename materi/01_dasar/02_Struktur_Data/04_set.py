"""
===============================================
SET DI PYTHON
===============================================

Set adalah koleksi yang:
- Tidak terurut
- Tidak mengizinkan duplikat
- Mutable
- Elemen harus immutable
"""

# =====================================
# 1. MEMBUAT SET
# =====================================

set_kosong = set()  # Bukan {} karena itu dictionary
angka = {1, 2, 3, 4, 5}
buah = {"apel", "jeruk", "mangga"}

# Duplikat otomatis dihapus
angka_duplikat = {1, 2, 2, 3, 3, 3}
print(f"angka_duplikat: {angka_duplikat}")  # {1, 2, 3}

# =====================================
# 2. OPERASI SET
# =====================================

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union (gabungan)
print(f"Union: {set1 | set2}")
print(f"Union: {set1.union(set2)}")

# Intersection (irisan)
print(f"Intersection: {set1 & set2}")

# Difference (selisih)
print(f"Difference: {set1 - set2}")

# Symmetric Difference
print(f"Symmetric Difference: {set1 ^ set2}")

# =====================================
# 3. MENAMBAH DAN MENGHAPUS
# =====================================

buah = {"apel", "jeruk"}
buah.add("mangga")
buah.update(["pisang", "anggur"])
print(f"Setelah add/update: {buah}")

buah.remove("jeruk")  # Error jika tidak ada
buah.discard("melon")  # Tidak error jika tidak ada
print(f"Setelah remove: {buah}")

# =====================================
# 4. MEMBERSHIP DAN SUBSET
# =====================================

set_besar = {1, 2, 3, 4, 5}
set_kecil = {2, 3}

print(f"2 in set_besar: {2 in set_besar}")
print(f"set_kecil.issubset(set_besar): {set_kecil.issubset(set_besar)}")
print(f"set_besar.issuperset(set_kecil): {set_besar.issuperset(set_kecil)}")

# =====================================
# 5. SET COMPREHENSION
# =====================================

kuadrat = {x**2 for x in range(1, 6)}
print(f"kuadrat: {kuadrat}")

# =====================================
# 6. FROZEN SET (Immutable Set)
# =====================================

frozen = frozenset([1, 2, 3])
print(f"frozenset: {frozen}")
# frozen.add(4)  # Error: tidak bisa diubah

# =============================================================================
# LATIHAN SET - 20 SOAL (4 TINGKAT KESULITAN)
# =============================================================================

"""
================================================================================
                        DAFTAR SOAL LATIHAN SET
================================================================================

🟢 BASIC (1-5) - Dasar-dasar Set
   1. Buat set berisi 5 buah-buahan, print hasilnya
   2. Buat set dari list [1,2,2,3,3,3,4] - perhatikan duplikat hilang
   3. Tambahkan "semangka" ke set buah menggunakan add()
   4. Hapus "apel" dari set menggunakan remove()
   5. Cek apakah "mangga" ada dalam set menggunakan 'in'

🟡 INTERMEDIATE (6-10) - Operasi Set
   6. Buat union dari {1,2,3} dan {3,4,5} menggunakan | atau union()
   7. Buat intersection dari {1,2,3,4} dan {3,4,5,6} menggunakan &
   8. Buat difference {1,2,3,4,5} - {3,4} menggunakan -
   9. Buat symmetric difference {1,2,3} ^ {2,3,4}
   10. Cek apakah {2,3} adalah subset dari {1,2,3,4,5}

🟠 ADVANCED (11-15) - Set Methods & Operasi Lanjutan
   11. Gunakan discard() untuk hapus elemen yang mungkin tidak ada
   12. Gunakan update() untuk menambah beberapa elemen sekaligus
   13. Gunakan pop() untuk hapus dan return elemen acak
   14. Buat set comprehension: kuadrat dari 1-10
   15. Gabung 3 set sekaligus menggunakan union()

🔴 EXPERT (16-20) - Tantangan Set
   16. Dari dua list, cari elemen yang ada di keduanya (intersection)
   17. Dari dua list, cari elemen yang hanya ada di salah satu (symmetric diff)
   18. Buat frozenset dan coba tambahkan elemen (error expected)
   19. Gunakan set untuk menghapus duplikat dari list dengan tetap menjaga urutan
   20. Cari semua huruf unik dari kata "programming" menggunakan set

================================================================================
"""

print("\n" + "=" * 60)
print("LATIHAN SET - Kerjakan di bawah ini!")
print("=" * 60)

# =============================================================================
# 🟢 BASIC (LEVEL 1-5)
# =============================================================================

# --- Soal 1 ---
print("\n📝 Soal 1: Buat set 5 buah")
# Tulis jawabanmu di bawah:
buah = {"apel", "jeruk", "mangga", "nanas", "pisang"}
print(buah)

# --- Soal 2 ---
print("\n📝 Soal 2: Set dari list dengan duplikat")
# Tulis jawabanmu di bawah:
angka = [1,2,2,3,3,3,4]
set(angka)

# --- Soal 3 ---
print("\n📝 Soal 3: Tambah elemen dengan add()")
# Tulis jawabanmu di bawah:
buah.add("semangka")

# --- Soal 4 ---
print("\n📝 Soal 4: Hapus dengan remove()")
# Tulis jawabanmu di bawah:
buah.remove("apel")

# --- Soal 5 ---
print("\n📝 Soal 5: Cek membership")
# Tulis jawabanmu di bawah:
cek = "mangga" in buah

# =============================================================================
# 🟡 INTERMEDIATE (LEVEL 6-10)
# =============================================================================

# --- Soal 6 ---
print("\n📝 Soal 6: Union dua set")
# Tulis jawabanmu di bawah:
set_1 = {1,2,3}
set_2 = {3,4,5}
set_union = set_1.union(set_2)
set_union = set_1 | set_2

# --- Soal 7 ---
print("\n📝 Soal 7: Intersection dua set")
# Tulis jawabanmu di bawah:
set_intersection = set_1 & set_2

# --- Soal 8 ---
print("\n📝 Soal 8: Difference set")
# Tulis jawabanmu di bawah:
set_difference = set_1 - set_2
set_difference = set_2 - set_1

# --- Soal 9 ---
print("\n📝 Soal 9: Symmetric difference")
# Tulis jawabanmu di bawah:
symmetric_difference = {1,2,3} ^ {2,3,4}

# --- Soal 10 ---
print("\n📝 Soal 10: Cek subset")
# Tulis jawabanmu di bawah:
set_1 = {1,2,3,4,5}
cek = {2,3}.issubset(set_1)

# =============================================================================
# 🟠 ADVANCED (LEVEL 11-15)
# =============================================================================

# --- Soal 11 ---
print("\n📝 Soal 11: Gunakan discard()")
# Tulis jawabanmu di bawah:
angka = {10, 20, 30, 40}
angka.discard(50)

# --- Soal 12 ---
print("\n📝 Soal 12: Gunakan update()")
# Tulis jawabanmu di bawah:
angka.update([50, 60, 70, 80])

# --- Soal 13 ---
print("\n📝 Soal 13: Gunakan pop()")
# Tulis jawabanmu di bawah:
angka_pop = angka.pop()

# --- Soal 14 ---
print("\n📝 Soal 14: Set comprehension kuadrat 1-10")
# Tulis jawabanmu di bawah:
set_comprehension = {i ** 2 for i in range(1,10)}
print(set_comprehension)

# --- Soal 15 ---
print("\n📝 Soal 15: Gabung 3 set")
# Tulis jawabanmu di bawah:
set_1 = {1, 3, 7, 6, 2, 8, 9, 10}
set_2 = {2, 6, 9, 3,5, 8, 9, 4}
set_3 = {2,1, 6, 9, 3, 4, 5, 7, 8}
set_union = set_1.union(set_2.union(set_3))  


# =============================================================================
# 🔴 EXPERT (LEVEL 16-20)
# =============================================================================

# --- Soal 16 ---
print("\n📝 Soal 16: Intersection dari dua list")
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
# Tulis jawabanmu di bawah:


# --- Soal 17 ---
print("\n📝 Soal 17: Symmetric diff dari dua list")
# Tulis jawabanmu di bawah:


# --- Soal 18 ---
print("\n📝 Soal 18: Frozenset (immutable)")
# Tulis jawabanmu di bawah:


# --- Soal 19 ---
print("\n📝 Soal 19: Hapus duplikat dengan jaga urutan")
data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# Tulis jawabanmu di bawah:


# --- Soal 20 ---
print("\n📝 Soal 20: Huruf unik dari 'programming'")
# Tulis jawabanmu di bawah:


print("\n" + "=" * 60)
print("Selesaikan semua soal di atas! 💪")
print("=" * 60)

