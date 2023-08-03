import math

def toplama(a,b):
    return a+b

def cikarma(a,b):
    return a-b

def carpma(a,b):
    return a*b

def bolme(a,b):
    return a/b

def karekok(a):
    return math.sqrt(a)


while True:
    print("Hesap Makinesi")
    print("1. Toplama")
    print("2. Çikarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Karekök")
    print("6. Çikiş")


    secim = input("Yapmak istediğiniz işlemi seçin (1-6): ")

    if(secim==6):
        print("hesap makinesinden cikiş yapiliyor")
        break
    elif secim in ['1', '2', '3', '4', '5']:
        num1 = float(input("Birinci sayiyi girin: "))
        num2 = float(input("İkinci sayiyi girin: "))

        if(secim==1):
            print("sonuc:",toplama(num1,num2))
        elif(secim==2):
            print("sonuc:",cikarma(num1,num2))
        elif(secim==3):
            print("sonuc:",carpma(num1,num2))
        elif(secim==4):
            print("sonuc:",bolme(num1,num2))
        elif(secim==5):
            print("sonuc:",bolme(num1,num2))
        elif(secim==6):
            print("1.secenegin sonucu:",karekok(num1))
            print("2.secenegin sonucu:",karekok(num2))  
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
