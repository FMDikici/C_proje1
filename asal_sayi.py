"""
def asal(sayi):
    if ((sayi==0) or (sayi==1)):
        return False
    else:
        for i in range(2,sayi):
            if (sayi%i==0):
                return False
            else:
                return True
            
while(True):
    sayi=int(input("sayi giriniz:"))

    if(asal(sayi)):
        print("Sayi Asal")

    else:
        print("Sayi asal degil")  

"""
"""
def tambolenlerbulma(sayi):
    tam_bolenler=[]
    for i in range(1,sayi):
        if (sayi%i==0):
            tam_bolenler.append(i)
    return tam_bolenler



while(True):
    sayi=int(input("Lutfen Sayi Giriniz:"))
    if(sayi==0):
        print("Program 0 sayisinda kapatilmaya uyarlanmistir...Kapatiliyor!")
    else:
        print("Tam bolenler {}".format(tambolenlerbulma(sayi)))

"""

def ebob(a, b):
    if a < b:
        enkucuksayi = a
    else:
        enkucuksayi = b
    ebob = 1
    
    for i in range(1, enkucuksayi + 1):
        if a % i == 0 and b % i == 0:
            ebob = i
         
    return ebob

a = int(input("Birinci sayıyı giriniz: "))
b = int(input("İkinci sayıyı giriniz: "))
en_buyuk_ortak_bolen = ebob(a, b)
print(f"{a} ve {b}'nin en büyük ortak böleni: {en_buyuk_ortak_bolen}'dir")



