"""
===============================================
DATETIME - TANGGAL DAN WAKTU
===============================================
"""

from datetime import datetime, date, time, timedelta

# =====================================
# 1. DATETIME SAAT INI
# =====================================

sekarang = datetime.now()
print(f"Sekarang: {sekarang}")
print(f"Tanggal: {sekarang.date()}")
print(f"Waktu: {sekarang.time()}")

print(f"Tahun: {sekarang.year}")
print(f"Bulan: {sekarang.month}")
print(f"Hari: {sekarang.day}")
print(f"Jam: {sekarang.hour}")

# =====================================
# 2. MEMBUAT DATETIME
# =====================================

tanggal = date(2024, 12, 25)
waktu = time(14, 30, 0)
dt = datetime(2024, 12, 25, 14, 30)

print(f"Tanggal: {tanggal}")
print(f"Waktu: {waktu}")
print(f"Datetime: {dt}")

# =====================================
# 3. FORMAT DATETIME
# =====================================

sekarang = datetime.now()

# strftime - datetime ke string
print(f"Format 1: {sekarang.strftime('%d/%m/%Y')}")
print(f"Format 2: {sekarang.strftime('%d %B %Y')}")
print(f"Format 3: {sekarang.strftime('%H:%M:%S')}")
print(f"Format lengkap: {sekarang.strftime('%A, %d %B %Y %H:%M')}")

# strptime - string ke datetime
tanggal_str = "25/12/2024"
tanggal = datetime.strptime(tanggal_str, '%d/%m/%Y')
print(f"Parse string: {tanggal}")

# =====================================
# 4. OPERASI DENGAN TIMEDELTA
# =====================================

sekarang = datetime.now()

# Menambah/mengurangi waktu
besok = sekarang + timedelta(days=1)
seminggu_lalu = sekarang - timedelta(weeks=1)
print(f"Besok: {besok.date()}")
print(f"Seminggu lalu: {seminggu_lalu.date()}")

# Selisih dua tanggal
awal = datetime(2024, 1, 1)
akhir = datetime(2024, 12, 31)
selisih = akhir - awal
print(f"Selisih: {selisih.days} hari")

# =====================================
# 5. PERBANDINGAN TANGGAL
# =====================================

tanggal1 = date(2024, 6, 15)
tanggal2 = date(2024, 12, 25)

print(f"{tanggal1} < {tanggal2}: {tanggal1 < tanggal2}")

# =====================================
# FORMAT CODES
# =====================================

"""
%Y - Tahun 4 digit (2024)
%y - Tahun 2 digit (24)
%m - Bulan (01-12)
%d - Hari (01-31)
%H - Jam 24h (00-23)
%I - Jam 12h (01-12)
%M - Menit (00-59)
%S - Detik (00-59)
%A - Nama hari (Monday)
%B - Nama bulan (January)
%p - AM/PM
"""
