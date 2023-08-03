"""
class bilgisayar:
    def __init__(self,marka,model,ram,disk):
        self.marka=marka
        self.model=model
        self.ram=ram
        self.disk=disk
    def __str__(self):
        return "marka:{},model:{},ram:{},disk:{}".format(self.marka,self.model,self.ram,self.disk)
    def __len__(self):
        return self.ram
    
    bilgisayar=("Asus Tuf","A15",16,512)

    bilgisayar1=bilgisayar

    print(bilgisayar1)
"""

class Hayvan:
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas
    
    def bilgileri_goster(self):
        print("İsim:", self.isim)
        print("Yaş:", self.yas)


class Köpek(Hayvan):
    def __init__(self, isim, yas, cins):
        super().__init__(isim, yas)
        self.cins = cins
    
    def havla(self):
        print("Hav hav!")


class Kuş(Hayvan):
    def __init__(self, isim, yas, kanat_uzunluğu):
        super().__init__(isim, yas)
        self.kanat_uzunluğu = kanat_uzunluğu
    
    def uc(self):
        print("Uçuyorum!")


class At(Hayvan):
    def __init__(self, isim, yas, renk):
        super().__init__(isim, yas)
        self.renk = renk
    
    def kos(self):
        print("Koşuyorum!")


# Hayvan örneği
hayvan1 = Hayvan("Hayvan", 5)
hayvan1.bilgileri_goster()

# Köpek örneği
kopek1 = Köpek("Karabaş", 3, "Golden Retriever")
kopek1.bilgileri_goster()
kopek1.havla()

# Kuş örneği
kus1 = Kuş("Cıvık", 1, 10)
kus1.bilgileri_goster()
kus1.uc()

# At örneği
at1 = At("Şahbatur", 7, "Kestane")
at1.bilgileri_goster()
at1.kos()