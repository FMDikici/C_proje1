"""
a=5
b=10
def carpma():
    print(a*b)


carpma()

def dongu():
    for i in range(10):
        print("merhaba")

dongu() 


def dongu2():
    print("merhaba")

for i in range(10):
    dongu2()    


saat=int(input("saati giriniz(dakika önemsenmeyecektir)"))

def selamla():
    if (12>saat>8):
        return "Gunaydin"
    elif(17>saat) and (saat>=12):
        return "Tunaydin"
    elif(saat>=17) and (24>=saat):
        return "iyi geceler"
    else:
        return "hata"
    
sonuc=selamla()

print(sonuc)
"""
"""parametre"""

"""
def yashesapla(dogumyili):
     return 2023-dogumyili

sonuc=yashesapla(2003)

print("su anki yasiniz {}".format(sonuc))

"""
"""
def selamla(isim):
    return ("merhaba",isim)

sonuc=selamla("fatih")

print(sonuc)
"""

"""varsayılan parametreler"""

ad=input("adinizi giriniz")
soyad=input("soyadinizi giriniz")

def fullname(ad,soyad): 
    return f"sisteme hos geldiniz {ad} {soyad}"

sonuc=fullname(ad , soyad)

print(sonuc)