"""
===============================================
BEKERJA DENGAN JSON DAN CSV
===============================================
"""

import json
import csv
import os

os.makedirs("output", exist_ok=True)

# =====================================
# 1. JSON - MEMBACA
# =====================================

# Membuat file JSON contoh
data_json = {
    "nama": "Budi",
    "umur": 25,
    "hobi": ["membaca", "coding", "gaming"],
    "alamat": {
        "kota": "Jakarta",
        "negara": "Indonesia"
    }
}

with open("output/data.json", "w") as f:
    json.dump(data_json, f, indent=4)

# Membaca JSON
with open("output/data.json", "r") as f:
    data = json.load(f)
    print("=== Data dari JSON ===")
    print(f"Nama: {data['nama']}")
    print(f"Hobi: {data['hobi']}")
    print(f"Kota: {data['alamat']['kota']}")

# =====================================
# 2. JSON - STRING CONVERSION
# =====================================

# Dict ke JSON string
json_string = json.dumps(data_json, indent=2)
print(f"\n=== JSON String ===\n{json_string}")

# JSON string ke Dict
json_str = '{"nama": "Ani", "umur": 22}'
parsed = json.loads(json_str)
print(f"\nParsed: {parsed}")

# =====================================
# 3. CSV - MEMBACA DAN MENULIS
# =====================================

# Menulis CSV
siswa = [
    ["Nama", "NIM", "Nilai"],
    ["Budi", "001", 85],
    ["Ani", "002", 92],
    ["Cici", "003", 78]
]

with open("output/siswa.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(siswa)

# Membaca CSV
print("\n=== Data CSV ===")
with open("output/siswa.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# =====================================
# 4. CSV DENGAN DICTREADER/DICTWRITER
# =====================================

# Menulis dengan DictWriter
data_list = [
    {"nama": "Budi", "umur": 25, "kota": "Jakarta"},
    {"nama": "Ani", "umur": 22, "kota": "Bandung"},
    {"nama": "Cici", "umur": 28, "kota": "Surabaya"}
]

with open("output/data_dict.csv", "w", newline="") as f:
    fieldnames = ["nama", "umur", "kota"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data_list)

# Membaca dengan DictReader
print("\n=== CSV dengan DictReader ===")
with open("output/data_dict.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['nama']} ({row['umur']}) - {row['kota']}")

# =====================================
# 5. KONVERSI JSON KE CSV
# =====================================

json_data = [
    {"id": 1, "produk": "Laptop", "harga": 15000000},
    {"id": 2, "produk": "Mouse", "harga": 250000},
    {"id": 3, "produk": "Keyboard", "harga": 500000}
]

# JSON ke CSV
with open("output/produk.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=json_data[0].keys())
    writer.writeheader()
    writer.writerows(json_data)

print("\nJSON berhasil dikonversi ke CSV!")

# =====================================
# 6. PRETTY PRINT JSON
# =====================================

import pprint

data_kompleks = {
    "users": [
        {"id": 1, "name": "User1", "roles": ["admin", "user"]},
        {"id": 2, "name": "User2", "roles": ["user"]}
    ],
    "meta": {"total": 2, "page": 1}
}

print("\n=== Pretty Print ===")
pprint.pprint(data_kompleks, width=60)

# =====================================
# LATIHAN
# =====================================

"""
Latihan 1: Buat program untuk menyimpan daftar kontak ke JSON
Latihan 2: Buat program untuk membaca CSV dan menghitung rata-rata nilai
Latihan 3: Konversi data CSV ke JSON
"""
