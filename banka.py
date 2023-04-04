bakiye=input("bakiye giriniz:")
print("Banka Hesabindaski Bakiye {}".format(bakiye))

print("lutfen yapmak istediginiz islemi seciniz:")
print("1.para yatirma\n2.para cekme\n3.doviz islemleri\n4.altin islemleri")
sec=input("yapilan secim:")

if (sec==1):
    print("Yatirilacak para miktarini giriniz:")
    yatirilacak=input()
    print("Lutfen Bekleyiniz...")
    print("Sayim Yapiliyor")
    print("Başarili..!")
    bakiye=yatirilacak+bakiye
    print("Yeni Bakiyeniz {}".format(bakiye))

elif(sec==2):
    print("Cekilecek Para Tutari Nedir?")
    cekilecek=input("Tutar:")
    bakiye=bakiye-cekilecek
    print("Lutfen Bekleyiniz..")
    print("Sayim Yapiliyor..")
    if(bakiye>=0):
        print("Basarili")
    else:
        print("Bakiyeniz Bu Duruma Uygun Degil! Kartinizi Tekrar Vermeye Calisiyoruz..")
        print("Bizi Tercih Ettiginiz İcin Tesekkur Ederiz..")

elif(sec==3):
    print("Yapmak İstediginiz İslem Doviz Almak mi[1], Satmak Mi[2]?")
    islem=input()
    if(islem==1):
        print("Yapmak istediğiniz Doviz Birimi hangisidir?")
        print("1.Euro\n2.Dolar")
        dovizsec1=int(input())
        if(dovizsec1==1):
            print("Su an güncel Euro Alimi '21,2824TL' ") 
            print("Kaynak:'https://www.isbank.com.tr/doviz-kurlari'")
            print("Almak İstediginiz Tutari Giriniz:")
            alim=input()
            eurotutar=alim*21.2824
            bakiye=bakiye-eurotutar
            if(bakiye>0):
                print("Basarili")
            else:
                print("lutfen Bekleyiniz..")
                print("Bakiyeniz Bu islem icin Uygun Degildir!")
                print("Bizi Tercih Ettiginiz İcin Tesekkur Ederiz..")
        elif(dovizsec1==2):
            print("Su an güncel Dolar Alimi '19,5197TL' ") 
            print("Kaynak:'https://www.isbank.com.tr/doviz-kurlari'")
            print("Almak İstediginiz Tutari Giriniz:")
            alim=float(input())
            dolartutar=alim*19.5197
            bakiye=bakiye-dolartutar
            if(bakiye>=0):
                print("Basarili")
            else:
                print("lutfen Bekleyiniz..")
                print("Bakiyeniz Bu islem icin Uygun Degildir!")
                print("Bizi Tercih Ettiginiz İcin Tesekkur Ederiz..")
    
    elif(islem==2):
        print("Yapmak istediğiniz Doviz Birimi hangisidir?")
        print("1.Euro\n2.Dolar")
        dovizsec=int(input())
        if(dovizsec==1):
            print("Su an güncel Euro Satimi '20,884TL' ") 
            print("Kaynak:'https://www.isbank.com.tr/doviz-kurlari'")
            print("Satmak İstediginiz Tutari Giriniz:")
            satim=input()
            eurotutar=satim*21.2824
            bakiye=bakiye+eurotutar
            print("Basarili. Yeni Bakiyeniz {}".format(bakiye))
        elif(dovizsec==2):
            print("Su an güncel Dolar Satimi '19.1543TL' ") 
            print("Kaynak:'https://www.isbank.com.tr/doviz-kurlari'")
            print("Satmak İstediginiz Tutari Giriniz:")
            satim=input()
            dolartutar=alim*19.5197
            bakiye=bakiye+dolartutar
            print("Basarili. Yeni Bakiyeniz{}".format(bakiye))
elif(sec==4):
    print("Altin Almak Mi[1] Yoksa Satmak Mi[2] İstersiniz")
    secim=input()
    if(secim==1):
        print("Lutfen Bekleyiniz..")
        print("Alim fiyatlari:'1249.68TL'")
        print("Kaynak: https://altin.doviz.com/gram-altin")
        print("Kac Gram Almak İstiyorsunuz?")
        altinalim=input()
        altinalim=altinalim*1249.68
        bakiye=bakiye-altinalim
        if(bakiye>0):
            print("başarili..")
        else:
            print("Bakiyeniz Bunun İcin Yeterli Değildir..")
            print("bizi Tercih Ettiginiz İcin Tesekkurler..")
    elif(secim==2):
        print("Lutfen Bekleyiniz..")
        print("Satis fiyatlari:'1248,85TL'")
        print("Kaynak: https://altin.doviz.com/gram-altin")
        print("Kac Gram Satmak İstiyorsunuz?")
        altinsatim=input()
        bakiye=bakiye+altinsatim
        print("Yeni Bakiyeniz{}".format(bakiye))

