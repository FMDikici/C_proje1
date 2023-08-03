defkullanici = "dartyet1"
defsifre = "16032003"

while (True):
    kullanici = input("Kullanıcı Adı:")
    sifre = input("Sifre:")
    if (kullanici == defkullanici) and (sifre == defsifre):
        print("Hoşgeldin" , kullanici)
        break
    elif (kullanici != defkullanici) and (sifre == defsifre):
        print("Kullanıcı Adı Yanlış")
        print("Kullanıcı Adını dğeiştirmmek ister misiniz ? [E/H]")
        cevap2 = input()
        if (cevap2 == "E"):
            yeniisim = input("Yeni Kullanıcı Adı girin:")
            print("Yeni Kullanıcı adı Başarıyla kaydedildi.")
            defisim = yeniisim
            print("Tekrar deneyin")

    elif (kullanici == defkullanici) and (sifre != defsifre):
        print("Şifre Yanlış")
        print("Şifreyi değiştirmek ister misiniz ? [E/H]")
        cevap = input()
        if (cevap == "E"):
            yenisifre = input("Yeni şifrenizi girin:")
            print("Şifreniz Başarıyla Kaydedildi")
            defsifre = yenisifre
            print("Tekrar deneyin")
    elif (kullanici != defkullanici) and (sifre != defsifre):
        print("Kullanıcı Adı ve Şifre Yanlış")
        print("Tekrar deneyin")

    else:
        print("Tekrar deneyin")