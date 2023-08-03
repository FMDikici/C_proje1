"""def geometri(kenar):
    print("Lütfen bekleyiniz...")
    print("Sistem yükleniyor...")

    if len(kenar) == 3:
        a = kenar[0]
        b = kenar[1]
        c = kenar[2]
        if a == b == c:
            print("Eşkenar üçgen")
        elif a == b or a == c or b == c:
            print("İkizkenar üçgen")
        else:
            print("Çeşitkenar üçgen")
    elif len(kenar) == 4:
        a = kenar[0]
        b = kenar[1]
        c = kenar[2]
        d = kenar[3]
        if a == b == c == d:
            print("Kare")
        elif (a == c and b == d) or (a == b and c == d) or (a == d and b == c):
            print("Dikdörtgen")
        else:
            print("Dörtgen")
    else:
        print("HATA")

while True:
    sekil = int(input("Lütfen kenar sayısını giriniz: "))
    if sekil == 3:
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
        geometri([a, b, c])
    elif sekil == 4:
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
        d = int(input("d: "))
        geometri([a, b, c, d])
    else:
        print("Hata..")
"""
"""
def faktoriyel(sayi):
    if(sayi==0) or (sayi==1):
        return 1
    else:
        return faktoriyel(sayi-1)*sayi
    
sayi=int(input("sayi giriniz:"))
a=faktoriyel(sayi)
print(a)    
"""
"""
def sayilari_topla(sayilar):
    toplam = 0
    for sayi in sayilar:
        toplam += sayi
    return toplam

# Kullanıcıdan sayıları alıp toplamını hesaplayan bir program
sayi_listesi = []
adet = int(input("Kaç adet sayı gireceksiniz? "))

for i in range(adet):
    sayi = int(input(f"{i+1}. sayıyı girin: "))
    sayi_listesi.append(sayi)

toplam = sayilari_topla(sayi_listesi)
print("Sayıların toplamı:", toplam)
"""
"""
def en_buyuk_sayiyi_bul(dizi):
    en_buyuk = 0

    for sayi in dizi:
        if sayi > en_buyuk:
            en_buyuk = sayi

    return en_buyuk

sayilar = [5, 8, 3, 12, 1, 7, 9]
en_buyuk = en_buyuk_sayiyi_bul(sayilar)

print("En büyük sayı:", en_buyuk)
"""
"""
def negatif_sayilari_pozitif_yap(dizi):
    for i in range(len(dizi)):
        if dizi[i]<0:
            dizi[i]=-dizi[i]
    return dizi

sayilar = [3, -5, 1, -8, 2, -4, 6]
sayi = negatif_sayilari_pozitif_yap(sayilar)

print("Dizinin güncel hali:", sayi)  
"""

def cift_sayilari_bul(dizi):
    ciftler = []

    for sayi in dizi:
        if sayi % 2 == 0:
            ciftler.append(sayi)

    return ciftler

sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ciftler = cift_sayilari_bul(sayilar)

print("Çift sayılar:", ciftler)
       
