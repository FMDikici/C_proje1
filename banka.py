class BankaHesabi:
    def __init__(self, hesap_numarasi, sahip_adi, bakiye=0):
        self.hesap_numarasi = hesap_numarasi
        self.sahip_adi = sahip_adi
        self.bakiye = bakiye

    def para_yatir(self, miktar):
        if miktar >= 0:
            self.bakiye += miktar
            print(f"{miktar} birim yatirildi. Yeni Bakiye: {self.bakiye}")
        else:
            print("Geçersiz yatirma miktari")

    def para_cek(self, miktar):
        if miktar >= 0:
            if self.bakiye - miktar < 0:
                print("Hesapta yeterli bakiye bulunmamaktadır.")
            else:
                self.bakiye -= miktar
                print(f"{miktar} para hesabınızdan çekildi. Yeni bakiye: {self.bakiye}")
        else:
            print("Geçersiz çekim miktarı")

    def bakiye_sorgula(self):
        return self.bakiye

    def __str__(self):
        return f"Hesap Numarası: {self.hesap_numarasi}\nSahip: {self.sahip_adi}\nBakiye: {self.bakiye}"

def ana_program():
    hesaplar = []

    while True:
        print("\nBanka ATM Menüsü:")
        print("1. Hesap oluştur")
        print("2. Varolan bir hesaba eriş")
        print("3. Çikiş")

        secim = input("Seçiminizi girin: ")

        if secim == "1":
            hesap_numarasi = input("Hesap numarasini girin: ")
            sahip_adi = input("Sahibin adini girin: ")
            hesap = BankaHesabi(hesap_numarasi, sahip_adi)
            hesaplar.append(hesap)
            print("Hesap başariyla oluşturuldu")

        elif secim == "2":
            hesap_numarasi = input("Hesap numarasini girin: ")
            secilen_hesap = None
            for hesap in hesaplar:
                if hesap.hesap_numarasi == hesap_numarasi:
                    secilen_hesap = hesap
                    break
            if secilen_hesap:
                print(str(secilen_hesap))

                while True:
                    print("\nHesap Menüsü:")
                    print("1. Para Yatir")
                    print("2. Para Çek")
                    print("3. Bakiye Sorgula")
                    print("4. Hesaptan Çik")

                    alt_secim = input("Seçiminizi girin: ")

                    if alt_secim == "1":
                        try:
                            miktar = float(input("Yatirilacak miktari girin: "))
                            secilen_hesap.para_yatir(miktar)
                        except ValueError:
                            print("Geçersiz miktar girişi")

                    elif alt_secim == "2":
                        try:
                            miktar = float(input("Çekilecek miktari girin: "))
                            secilen_hesap.para_cek(miktar)
                        except ValueError:
                            print("Geçersiz miktar girişi")

                    elif alt_secim == "3":
                        print(f"Mevcut bakiye: {secilen_hesap.bakiye_sorgula()}")

                    elif alt_secim == "4":
                        break

                    else:
                        print("Geçersiz seçim.")

            else:
                print("Hesap bulunamadi.")

        elif secim == "3":
            print("ATM'den çikiliyor. İyi günler!")
            break

        else:
            print("Geçersiz seçim.")

if __name__ == "__main__":
    ana_program() #burada chatgpt yardımı var anlamadım ne oldugunu

                



