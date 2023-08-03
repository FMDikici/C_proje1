kullaniciadi="FMDikici"
kullaniciparola=123456

ad=input("kullanici adinizi giriniz: ")
parola=int(input("parolayi giriniz: "))

if ((ad==kullaniciadi) and(parola==kullaniciparola)):
    print("Hos Geldiniz!")
elif ((ad!=kullaniciadi) and (parola==kullaniciparola)):
    print("Kullanici Adi yanlis")
elif((ad==kullaniciadi) and (parola!=kullaniciparola)):
    print("Parola Yanlis")
else:
    print("Tekrar Deneyiniz!")