"""
def faktoriyel(fak):

    if ((fak==0) or (fak==1)):
        return 1
    else:
        return faktoriyel(fak-1)*fak
    


fak=int(input("sayi giriniz:"))

a=faktoriyel(fak)

print(a)
"""

def kayit_ekle(ad="bilgi yok",soyad="bilgi yok",yas="bilgi yok"):
    print("Kaydediliyor...\n\n")

    print("Lütfen Bekleyiniz...!")

    print("AD:{}\nSOYAD:{}\nYAŞ:{}\n".format(ad,soyad,yas))

kayit_ekle("Fatih Mehmet","Dikici")    


print("Kayıt Başarı İle Oluşturuldu...!")
