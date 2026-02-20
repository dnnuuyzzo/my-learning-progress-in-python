inputUser = float(input("Masukkan angka: "))
isLebihDari_1 = inputUser > 0
isKurangDari_1 = inputUser < 5
hasil_1 = isKurangDari_1 and isLebihDari_1
isLebihDari_2 = inputUser > 8
isKurangDari_2 = inputUser < 11
hasil_2 = isLebihDari_2 and isKurangDari_2
print(hasil := hasil_2 or hasil_1)

inputUser = float(input("Masukkan angka: "))
kurangdari1 = inputUser < 0
lebihdari2 = inputUser > 11
kurangdari3 = inputUser < 8
lebihdari3 = inputUser > 5
hasil3 = kurangdari3 and lebihdari3
print(hasil := kurangdari1 or hasil3 or lebihdari2)