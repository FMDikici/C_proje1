class yazilimci:
    def __init__(self,ad,soyad,numara,maas,diller):
        self.ad=ad
        self.soyad=soyad
        self.numara=numara
        self.maas=maas
        self.diller=diller
    def bilgileri_goster(self):
        print("""
        calisan bilgisi:
         ad={}
         soyad={}
         numara={}
         maas={}
         diller={}
         """.format(self.ad,self.soyad,self.numara,self.maas,self.diller))
    def dil_ekle(self,yeni_dil):
        print("dil ekleniyor...")
        yazilimci1.diller.append(yeni_dil)
    def zam(self,yeni_maas):
        print("maas ekleniyor..")
        self.maas+=yeni_maas

yazilimci1=yazilimci("Fatih Mehmet","Dikici","222503008",15000,["c","python"])

yazilimci1.dil_ekle("c++")
yazilimci1.zam(5000)

yazilimci1.bilgileri_goster()
