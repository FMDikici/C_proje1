import time
import random

print("*********************")

print("Sayi Tahmin oyunu")

print("1 ile 40 arası sayi giriniz ") 

rastgele_sayi=random.randint(1,40)
tahmin_hakki=7

while True:
    tahmin=int(input("tahmininiz: "))
    if(tahmin<rastgele_sayi):
        print("sorgulaniyor..")
        time.sleep(1)
        print("lütfen sayiyi arttirarak tekrar deneyiniz")
        tahmin_hakki-=1
    elif(tahmin>rastgele_sayi):
        print("sorgulaniyor..")
        time.sleep(1)
        print("lütfen sayiyi azaltarak tekrar deneyiniz")
        tahmin_hakki-=1
    elif(tahmin==rastgele_sayi):
        print("sorgulaniyor..")
        time.sleep(1)
        print("tebrikler sayi: ",rastgele_sayi)
        break      
    elif(tahmin==0):
        print("sorgulaniyor..")
        time.sleep(1)
        print("aralikta olmayan bir sayi girdiniz,oyundan cikiliyor..!")
        break

      
