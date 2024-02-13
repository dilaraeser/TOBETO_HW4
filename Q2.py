def zamliMaas(maas, zamOrani):
    #zamMiktari = maas * (zamOrani / 100)
    zamliMaas = maas + (maas * zamOrani / 100)
    return zamliMaas

maas = float(input("Lütfen mevcut maaşı giriniz: "))
zamOrani = float(input("Lütfen zam oranını giriniz (Sadece pay kısmını giriniz ,payda kısmı 100 alınacaktır): "))

zamli = float (zamliMaas(maas, zamOrani))
print("Zamlı Maaş:", zamli)