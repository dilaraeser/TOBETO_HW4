import math

def daireninAlani(yariCap):
    alan = yariCap ** 2 * math.pi
    return alan

def daireninCevresi(yariCap):
    cevre = 2 * math.pi * yariCap
    return cevre

yariCap = float(input("Yaricapi giriniz: "))

alan = daireninAlani(yariCap)
cevre = daireninCevresi(yariCap)

print("Dairenin Alanı: ", alan)
print("Dairenin Çevresi: ", cevre)