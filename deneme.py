class calisan:
    def __init__(self,isim,maas,departman):
        self.isim=isim
        self.maas=maas
        self.departman=departman
    def bilgilerigoster(self):
        
        print("Çalışan sınıfının bilgileri.....")
        
        print("İsim : {} \nMaaş: {} \nDepartman: {}\n".format(self.isim,self.maaş,self.departman))
    def departman_degistir(self,yeni_departman):
        print("Departman değişiyor....")
        self.departman = yeni_departman

class yonetici(calisan):
    def __init__(self,isim,maas,departman,kisi_sayisi):
        super().__init__(isim,maas,departman)
        print("yonetici sinifinin init fonksiyonu")
        self.kisi_sayisi=kisi_sayisi
    def bilgileri_goster(self):
        print("""
        calisan bilgisi:
        İsim : {}
        Maaş: {}
        kisi sayisi={} 
        Departman: {}""".format(self.isim,self.maas,self.departman,self.kisi_sayisi))
    def zam_yap(self,zam_miktarı):
        print("Maaşa zam yapılıyor....")
        self.maas += zam_miktarı
        c=yonetici("Oğuz Artıran",3000,"İnsan Kaynakları",4)
        c.bilgilerigoster()
