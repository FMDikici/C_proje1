import random
import msvcrt

class kumanda:
    def __init__(self,tv_durum="kapali",tv_ses=0,kanal_listesi=["TRT"],kanal="TRT"):
        print("kumanda olusturuluyor")

        self.tv_ses=tv_ses
        self.tv_durum=tv_durum
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal
    def sesi_azalt_arttir(self):
        while True:
            karakter=input("Azaltmak için '<',arttirmak icin '>' tamam ise 'q'ya basiniz")
            if(karakter == "<"):
                if(self.tv_ses!=0):
                    self.tv_ses-=1
                    print("ses:",self.tv_ses)
            elif(karakter ==">"):
                if(self.tv_ses!=32):
                    self.tv_ses+=1
                    print("ses:",self.tv_ses)
            elif(karakter=="q"):
                print("ses güncellendi:",self.tv_ses)
                break
    def tv_kapat(self):
        print("TV kapatiliyor")
        self.tv_durum="Kapali"
    def tv_ac(self):
        print("Tv aciliyor")
        self.tv_durum="Acik"
    def __str__(self):
        return "Tv Durumu : {}\nSes: {}\nKanallar: {}\nŞu anki kanal: {}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)
    def __len__(self):
        return len(self.kanal_listesi)
    def rastgele_kanal(self):
        rastgele=random.randint(0,len(self.kanal_listesi)-1)
        self.kanal=self.kanal_listesi[rastgele]
        print("su anki kanal:",self.kanal)
    def kanal_ekle(self,kanal):
        print("kanal eklendi",kanal)
        self.kanal_listesi.append(kanal)


kumanda=kumanda()
print("""************************

Televizyon Uygulaması

İşlemler ;

1. Televizyonu Aç

2. Televizyonu Kapat

3. Televizyon Bilgileri

4. Kanal Sayısını Öğrenme

5. Kanal Ekle

6. Rastgele Kanal'a Geç

7. Sesi Azalt Ya da Artır
Çıkmak için 'q' ya basın.
*******************""")

while True:
    islem=input("islemi giriniz:")

    if (islem == "q"):
        print("Programdan Çıkılıyor...")
        break
    if (islem == "1"):
        kumanda.tv_aç()
    elif (islem == "2"):
        kumanda.tv_kapat()
    elif (islem == "3"):
        print(kumanda)
    elif (islem == "4"):
        print("Kanal Sayısı: ",len(kumanda))
    elif (islem == "5"):
        kanallar = input("Eklemek İstediğiniz Kanalları ',' ile ayırarak girin:")
        eklenecekler = kanallar.split(",")
        for i in eklenecekler:

            kumanda.kanal_ekle(i)
        print("Kanal Listesi Başarıyla Güncellendi.")
    elif (islem == "6"):
        kumanda.rastgele_kanal()
    elif (islem == "7"):
        kumanda.sesi_azalt_artir()
    else:
        print("Geçersiz İşlem...")
