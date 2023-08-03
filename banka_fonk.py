def banka_karti():
    kart_no=123456789
    while(True):
        kart_giris=int(input("Lutfen Kart Numaranizi Giriniz:"))
        if(kart_no==kart_giris):
            print("Lutfen Bekleyiniz...")
            print("Hos Geldiniz Musteri")
            break
        else:
            print("Hatali Kart Numarasi,Lutfen Tekrar Deneyiniz..!")

def para_cek(bakiye):
    miktar=int(input("Cekmek istediginiz tutari giriniz:"))
    if(miktar>bakiye):
        print("Bakiye Yetersiz")
    else:
        bakiye=bakiye-miktar
        print("Lutfen Bekleyiniz...")
        print("İslem Basarili.. Yeni bakiyeniz {}".format(bakiye))
    return bakiye

def para_yatir(bakiye):
    miktar=int(input("yatirmak istediginiz tutari giriniz:"))
    bakiye=bakiye+miktar
    print("Lutfen Bekleyiniz...")
    print("İslem Basarili, Yeni Bakiyeniz {}".format(bakiye))
    return bakiye

def dolar_islemi(bakiye):
    secim = input("Dolar almak icin '1', dolar satmak icin '2' girin: ")
    if secim == '1':
        print("Su anki dolar kuru: 19.5TL") 
        miktar = int(input("Almak istediginiz tutari girin: "))
        bakiye -= miktar*19.5 
        print("Islem basarili. Yeni bakiyeniz: ", bakiye)
    elif secim == '2':
        print("Su anki dolar kuru: 19.3TL") 
        miktar = int(input("Satmak istediginiz tutari girin: "))
        bakiye += miktar*19.3
        print("Islem basarili. Yeni bakiyeniz: ", bakiye)
    else:
        print("Hatali secim yaptiniz. Tekrar deneyin.")
    return bakiye

def euro_islemi(bakiye):
    secim = input("euro almak icin '1', euro satmak icin '2' girin: ")
    if secim == '1':
        print("Su anki euro kuru: 21TL") 
        miktar = int(input("Almak istediginiz tutari girin: "))
        bakiye -= miktar*21 
        print("Islem basarili. Yeni bakiyeniz: ", bakiye)
    elif secim == '2':
        print("Su anki euro kuru: 20.9TL") 
        miktar = int(input("Satmak istediginiz tutari girin: "))
        bakiye += miktar*20.9
        print("Islem basarili. Yeni bakiyeniz: ", bakiye)
    else:
        print("Hatali secim yaptiniz. Tekrar deneyin.")
    return bakiye


bakiye = 10000
banka_karti()

while True:
    print("yapmak istediginiz islemi seciniz:")
    print("1.para cek\n2.para yatir\n3.dolar islemleri\n4.euro islemleri\n0.cikis")
    secim = int(input("Sec: "))
    
    if secim == 1:
        bakiye = para_cek(bakiye)
    elif secim == 2:
        bakiye = para_yatir(bakiye)
    elif secim == 3:
        bakiye = dolar_islemi(bakiye)
    elif secim == 4:
        bakiye = euro_islemi(bakiye)
    elif secim == 0:
        print("Programdan cikiliyor...")
        break
    else:
        print("Hatali secim yaptiniz. Tekrar deneyin.")