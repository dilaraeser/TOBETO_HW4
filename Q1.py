def vucutİndeksi(boy, agirlik):
    vki = agirlik / (boy * boy)
    return vki

boy = float(input("Lütfen boyunuzu (metre cinsinde) giriniz: "))
agirlik = float(input("Lütfen kilonuzu giriniz: "))

vki = vucutİndeksi(boy, agirlik)

if vki <18:
    print("\nZayıf VKİ:{}".format(vki))
elif vki >= 18 and vki <25 :
    print("\nNormal VKİ:{}".format(vki))
elif vki >= 25 and vki <30:
    print("\nKilolu VKİ:{}".format(vki))
elif vki >= 30 and vki <35:
    print("\nObez VKİ:{}".format(vki))
else:
    print("\nCiddi obez VKİ:{}".format(vki))