import datetime
# print(5 * "=", "TEBAK UMUR", 5*"=")
# print("Masukkan Tanggal Lahir Anda")
# tanggal = int(input("Tanggal\t: "))
# bulan = int(input("Bulan\t: "))
# tahun = int(input("Tahun\t: "))
# tanggal_lahir = datetime.date(tahun, bulan, tanggal)
# hari_ini = datetime.date.today()
# umur = hari_ini - tanggal_lahir
# umur = umur.days // 365
# print("Umur anda sekarang adalah:", umur := umur.days // 365)

print(i := " BIRTH DATE CHALENGE ".center(50, "="), "\nInput your birth date!")
date = int(input("Date\t: "))
month = int(input("Month\t: "))
year = int(input("Year\t: "))
born = datetime.date(year, month, date)
today = datetime.date.today()
age = today - born
age = age.days // 365
print("Your age is", age, "years old")