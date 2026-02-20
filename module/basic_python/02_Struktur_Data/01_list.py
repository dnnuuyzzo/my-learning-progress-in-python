"""
===============================================
LIST DI PYTHON
===============================================

List adalah struktur data yang:
- Menyimpan koleksi item secara terurut
- Bisa diubah (mutable)
- Bisa menyimpan tipe data berbeda
- Mengizinkan duplikat
"""

# =====================================
# 1. MEMBUAT LIST
# =====================================

# List kosong
list_kosong = []
list_kosong2 = list()

# List dengan nilai
angka = [1, 2, 3, 4, 5]
buah = ["apel", "jeruk", "mangga"]
campuran = [1, "dua", 3.0, True, None]

# List bersarang (nested list)
matriks = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(f"angka: {angka}")
print(f"buah: {buah}")
print(f"campuran: {campuran}")
print(f"matriks: {matriks}")

# =====================================
# 2. MENGAKSES ELEMEN LIST
# =====================================

buah = ["apel", "jeruk", "mangga", "pisang", "anggur"]
#        0        1        2         3         4
#       -5       -4       -3        -2        -1

print("\n=== Mengakses Elemen ===")
print(f"buah[0]: {buah[0]}")    # apel (pertama)
print(f"buah[2]: {buah[2]}")    # mangga
print(f"buah[-1]: {buah[-1]}")  # anggur (terakhir)
print(f"buah[-2]: {buah[-2]}")  # pisang

# Mengakses nested list
matriks = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"matriks[0]: {matriks[0]}")       # [1, 2, 3]
print(f"matriks[1][2]: {matriks[1][2]}") # 6

# =====================================
# 3. LIST SLICING
# =====================================

angka = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("\n=== List Slicing ===")
print(f"angka: {angka}")
print(f"angka[2:5]: {angka[2:5]}")   # [2, 3, 4]
print(f"angka[:4]: {angka[:4]}")     # [0, 1, 2, 3]
print(f"angka[6:]: {angka[6:]}")     # [6, 7, 8, 9]
print(f"angka[::2]: {angka[::2]}")   # [0, 2, 4, 6, 8] (step 2)
print(f"angka[::-1]: {angka[::-1]}") # Reverse

# =====================================
# 4. MENGUBAH ELEMEN LIST
# =====================================

buah = ["apel", "jeruk", "mangga"]

print("\n=== Mengubah Elemen ===")
print(f"Sebelum: {buah}")

# Mengubah satu elemen
buah[1] = "lemon"
print(f"Setelah buah[1] = 'lemon': {buah}")

# Mengubah beberapa elemen sekaligus
buah[1:3] = ["anggur", "pisang"]
print(f"Setelah slice assignment: {buah}")

# =====================================
# 5. MENAMBAH ELEMEN
# =====================================

buah = ["apel", "jeruk"]

print("\n=== Menambah Elemen ===")
print(f"Awal: {buah}")

# append() - menambah di akhir
buah.append("mangga")
print(f"Setelah append('mangga'): {buah}")

# insert() - menambah di posisi tertentu
buah.insert(1, "pisang")
print(f"Setelah insert(1, 'pisang'): {buah}")

# extend() - menambah beberapa elemen sekaligus
buah.extend(["anggur", "melon"])
print(f"Setelah extend(['anggur', 'melon']): {buah}")

# Menggunakan operator +
buah = buah + ["semangka"]
print(f"Setelah + ['semangka']: {buah}")

# =====================================
# 6. MENGHAPUS ELEMEN
# =====================================

buah = ["apel", "jeruk", "mangga", "pisang", "anggur"]

print("\n=== Menghapus Elemen ===")
print(f"Awal: {buah}")

# remove() - menghapus berdasarkan nilai
buah.remove("mangga")
print(f"Setelah remove('mangga'): {buah}")

# pop() - menghapus dan mengembalikan elemen (default: terakhir)
elemen = buah.pop()
print(f"Setelah pop(): {buah}, elemen dihapus: {elemen}")

elemen = buah.pop(1)
print(f"Setelah pop(1): {buah}, elemen dihapus: {elemen}")

# del - menghapus berdasarkan index
del buah[0]
print(f"Setelah del buah[0]: {buah}")

# clear() - menghapus semua elemen
buah.clear()
print(f"Setelah clear(): {buah}")

# =====================================
# 7. LIST METHODS
# =====================================

angka = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

print("\n=== List Methods ===")
print(f"angka: {angka}")

# index() - mencari posisi elemen
print(f"index(5): {angka.index(5)}")

# count() - menghitung kemunculan
print(f"count(1): {angka.count(1)}")

# sort() - mengurutkan (mengubah list asli)
angka_copy = angka.copy()
angka_copy.sort()
print(f"sort(): {angka_copy}")

# sort(reverse=True) - urutan menurun
angka_copy2 = angka.copy()
angka_copy2.sort(reverse=True)
print(f"sort(reverse=True): {angka_copy2}")

# sorted() - mengurutkan (mengembalikan list baru)
print(f"sorted(angka): {sorted(angka)}")
print(f"angka asli: {angka}")

# reverse() - membalik urutan
angka.reverse()
print(f"reverse(): {angka}")

# copy() - membuat salinan
salinan = angka.copy()

# =====================================
# 8. LIST COMPREHENSION
# =====================================

print("\n=== List Comprehension ===")

# Cara tradisional
kuadrat = []
for i in range(1, 6):
    kuadrat.append(i ** 2)
print(f"Cara tradisional: {kuadrat}")

# Dengan list comprehension
kuadrat = [i ** 2 for i in range(1, 6)]
print(f"List comprehension: {kuadrat}")

# Dengan kondisi
genap = [i for i in range(1, 11) if i % 2 == 0]
print(f"Genap 1-10: {genap}")

# Dengan if-else
label = ["genap" if i % 2 == 0 else "ganjil" for i in range(1, 6)]
print(f"Label: {label}")

# Nested list comprehension
matriks = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(f"Matriks perkalian: {matriks}")

# =====================================
# 9. OPERASI UMUM PADA LIST
# =====================================

print("\n=== Operasi Umum ===")

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation
gabung = list1 + list2
print(f"Concatenation: {gabung}")

# Repetition
ulang = list1 * 3
print(f"Repetition: {ulang}")

# Membership
print(f"2 in list1: {2 in list1}")

# Length
print(f"len(list1): {len(list1)}")

# Min, Max, Sum
angka = [5, 2, 8, 1, 9]
print(f"min: {min(angka)}, max: {max(angka)}, sum: {sum(angka)}")

# =============================================================================
# LATIHAN LIST - 20 SOAL (4 TINGKAT KESULITAN)
# =============================================================================

"""
================================================================================
                        DAFTAR SOAL LATIHAN LIST
================================================================================

🟢 BASIC (1-5) - Dasar-dasar List
   1. Buat list berisi 5 nama buah, tampilkan elemen pertama dan terakhir
   2. Buat list angka 1-10, ambil 5 angka pertama menggunakan slicing
   3. Tambahkan "semangka" ke akhir list buah menggunakan append()
   4. Hapus elemen kedua dari list menggunakan pop()
   5. Cari panjang (jumlah elemen) dari list [10, 20, 30, 40, 50]

🟡 INTERMEDIATE (6-10) - Operasi Menengah
   6. Gabungkan dua list [1,2,3] dan [4,5,6], lalu urutkan secara descending
   7. Dari list [45, 23, 78, 12, 56], cari nilai min, max, dan rata-rata
   8. Hapus semua duplikat dari list [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
   9. Hitung berapa kali "apel" muncul di ["apel","jeruk","apel","mangga","apel"]
   10. Balik urutan list ["a","b","c","d","e"] tanpa menggunakan reverse()

🟠 ADVANCED (11-15) - List Comprehension & Logika
   11. Buat list kuadrat dari angka ganjil 1-20 menggunakan list comprehension
   12. Dari list harga [5000,12000,8000,25000,15000], beri diskon 10% jika > 10000
   13. Filter list campuran [1,"error",2,"bug",3,4,"crash"] hanya ambil integer
   14. Ubah list nama ["andi","BUDI","CaCa"] menjadi format Title Case
   15. Dari list nilai [85,92,78,95,88], kategorikan: >=90="A", >=80="B", else="C"

🔴 EXPERT (16-20) - Tantangan & Nested List
   16. Transpose matriks 3x3: [[1,2,3],[4,5,6],[7,8,9]] menjadi [[1,4,7],[2,5,8],[3,6,9]]
   17. Flatten nested list [[1,2],[3,4,5],[6]] menjadi [1,2,3,4,5,6]
   18. Dari list kata ["python","java","go","rust"], buat dictionary {kata: panjang}
   19. Cari elemen yang muncul di kedua list: [1,2,3,4,5] dan [4,5,6,7,8]
   20. Rotasi list [1,2,3,4,5] ke kanan sebanyak 2 posisi menjadi [4,5,1,2,3]

================================================================================
"""

# =============================================================================
# 🟢 BASIC (LEVEL 1-5) - Dasar-dasar List
# =============================================================================

print("\n" + "=" * 60)
print("🟢 BASIC - Dasar-dasar List")
print("=" * 60)

# --- Soal 1: Akses Elemen Pertama & Terakhir ---
print("\n📝 Soal 1: Tampilkan elemen pertama dan terakhir dari list buah")
buah = ["Apel", "Anggur", "Mangga", "Jeruk", "Pisang"]
print(f"Tampilan Buah pertama: {buah[0]}")
print(f"Tampilan Buah terakhir: {buah[-1]}")

# --- Soal 2: Slicing 5 Angka Pertama ---
print("\n📝 Soal 2: Ambil 5 angka pertama dari list 1-10")
angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Lima angka pertama dalam list: {angka[:5]}")

# --- Soal 3: Append Elemen ---
print("\n📝 Soal 3: Tambahkan 'semangka' ke akhir list buah")
buah.append("Semangka")

# --- Soal 4: Pop Elemen ---
print("\n📝 Soal 4: Hapus elemen kedua (index 1) menggunakan pop()")
buah.pop(1)

# --- Soal 5: Panjang List ---
print("\n📝 Soal 5: Cari panjang list [10, 20, 30, 40, 50]")
angka = [10, 20, 30, 40, 50]
panjang_list = len(angka)

# =============================================================================
# 🟡 INTERMEDIATE (LEVEL 6-10) - Operasi Menengah
# =============================================================================

print("\n" + "=" * 60)
print("🟡 INTERMEDIATE - Operasi Menengah")
print("=" * 60)

# --- Soal 6: Gabung & Urutkan Descending ---
print("\n📝 Soal 6: Gabungkan [1,2,3] dan [4,5,6], urutkan descending")
angka_1 = [1, 2, 3]
angka_2 = [4, 5, 6]
angka_gabungan = sorted(angka_1 + angka_2, reverse= True)

# --- Soal 7: Min, Max, Rata-rata ---
print("\n📝 Soal 7: Cari min, max, dan rata-rata dari [45, 23, 78, 12, 56]")
angka = [45, 23, 78, 12, 56]
nilai_min = min(angka)
nilai_max = max(angka)
nilai_rata_rata = sum(angka) / len(angka)

# --- Soal 8: Hapus Duplikat ---
print("\n📝 Soal 8: Hapus duplikat dari [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]")
angka = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
angka_non_duplikat = set(angka)

# --- Soal 9: Hitung Kemunculan ---
print("\n📝 Soal 9: Hitung berapa kali 'apel' muncul")
buah = ["Apel", "Jeruk", "Apel", "Mangga", "Apel"]
jumlah_apel = buah.count("Apel")

# --- Soal 10: Balik Urutan Tanpa reverse() ---
print("\n📝 Soal 10: Balik urutan ['a','b','c','d','e'] tanpa reverse()")
huruf = ["a", "b", "c", "d", "e"]
sorted(huruf, reverse= True)

# =============================================================================
# 🟠 ADVANCED (LEVEL 11-15) - List Comprehension & Logika
# =============================================================================

print("\n" + "=" * 60)
print("🟠 ADVANCED - List Comprehension & Logika")
print("=" * 60)

# --- Soal 11: Kuadrat Angka Ganjil 1-20 ---
print("\n📝 Soal 11: List kuadrat dari angka ganjil 1-20")
angka_ganjil_kuadrat = [i ** 2 for i in range(1,21) if i % 2 != 0]

# --- Soal 12: Diskon Belanja ---
print("\n📝 Soal 12: Beri diskon 10% untuk harga > 10000")
harga = [5000, 12000, 8000, 25000, 15000]
harga_diskon = [int(i * 0.9) if i > 10000 else i for i in harga]

# --- Soal 13: Filter Hanya Integer ---
print("\n📝 Soal 13: Filter hanya integer dari list campuran")
list_campuran = [1, "error", 2, "bug", 3, 4, "crash"]
list_int = [i for i in list_campuran if isinstance(i, int)]

# --- Soal 14: Title Case ---
print("\n📝 Soal 14: Ubah ke Title Case ['andi','BUDI','CaCa']")
nama = ["andi","BUDI","CaCa"]
nama_title = [i.title() for i in nama]

# --- Soal 15: Kategorisasi Nilai ---
print("\n📝 Soal 15: Kategorikan nilai [85,92,78,95,88] ke A/B/C")
nilai = [85,92,78,95,88]
nilai_A = [i for i in nilai if i >= 90]
nilai_B = [i for i in nilai if 80 <= i < 90]
nilai_C = [i for i in nilai if i < 80]

# =============================================================================
# 🔴 EXPERT (LEVEL 16-20) - Tantangan & Nested List
# =============================================================================

print("\n" + "=" * 60)
print("🔴 EXPERT - Tantangan & Nested List")
print("=" * 60)

# --- Soal 16: Transpose Matriks ---
print("\n📝 Soal 16: Transpose matriks 3x3")


# --- Soal 17: Flatten Nested List ---
print("\n📝 Soal 17: Flatten nested list [[1,2],[3,4,5],[6]]")


# --- Soal 18: List ke Dictionary ---
print("\n📝 Soal 18: Buat dictionary {kata: panjang} dari list kata")


# --- Soal 19: Irisan Dua List ---
print("\n📝 Soal 19: Cari elemen yang ada di kedua list")


# --- Soal 20: Rotasi List ---
print("\n📝 Soal 20: Rotasi list [1,2,3,4,5] ke kanan 2 posisi")


print("\n" + "=" * 60)
print("🎉 SELESAI! Kamu sudah menyelesaikan 20 soal latihan List!")
print("=" * 60)
