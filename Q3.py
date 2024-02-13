a = float(input("Birinci sayiyi giriniz:"))
b = float(input("İkinci sayiyi giriniz:"))
c = float(input("Üçüncü sayiyi giriniz:"))

def maximum(a, b, c):
    list = [a, b, c]
    return max(list)
print("En buyuk sayi: ", maximum(a, b, c))