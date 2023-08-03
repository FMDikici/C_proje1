##kalıtım
1.
"""
class calisan:
    def __init__(self,ad,soyad,maas,departman):
        self.ad=ad
        self.soyad=soyad
        self.maas=maas
        self.departman=departman
    def bilgileri_goster(self):
        print('''calisan bilgileri
        ad={}
        soyad={}
        maas={}
        departman={}
        '''.format(self.ad,self.soyad,self.maas,self.departman))
    def departman_degis(self,yeni_departman):
        print("departman degistiriliyor..")
        self.departman=yeni_departman

class yonetici(calisan):
    pass
yonetici1=yonetici("fatih mehmet","dikici",15000,"bilisim")

yonetici1.departman_degis("yazilim")
yonetici1.bilgileri_goster()
"""
class calisan:
    def __init__(self, ad, soyad, maas, departman):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.departman = departman
    
    def bilgileri_goster(self):
        print("""Çalışan bilgileri:
        Ad: {}
        Soyad: {}
        Maaş: {}
        Departman: {}
        """.format(self.ad, self.soyad, self.maas, self.departman))
    
    def departman_degis(self, yeni_departman):
        print("Departman değiştiriliyor...")
        self.departman = yeni_departman


class yonetici(calisan):
    def zam_yap(self, zam_miktarı):
        print("Maaşa zam yapılıyor....")
        self.maas += zam_miktarı


yonetici1 = yonetici("fatih mehmet", "dikici", 15000, "bilisim")

yonetici1.departman_degis("yazilim")
yonetici1.bilgileri_goster()

yonetici2 = yonetici("murat", "coskun", 3000, "Bilişim")  # Yönetici objesi

yonetici2.zam_yap(5000)
yonetici2.bilgileri_goster()

print(dir(yonetici1))





