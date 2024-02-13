def palindrom_mu(sayi):
    sayi_str = str(sayi)
    ters_sayi_str = sayi_str[::-1]
    return sayi_str == ters_sayi_str

sayi = input("Lütfen bir sayı giriniz: ")

if palindrom_mu(sayi):
    print(sayi, " bir palindromdur.")
else:
    print(sayi, " bir palindrom değildir.")