"""class Kitap():
    pass

kitap1 = Kitap() # __init__ metodu çağrılıyor.

len(kitap1) # __len__ metodu çağrılacak ancak tanımlı değil. Bunu özellikle bizim tanımlamamız gerekiyor.
#şimdilik hata verecek

print(kitap1) # __str__ metodu çağrılır.

del kitap1 # del anahtar kelimesi bir objeyi siler ve __del__ metodu çağrılır. 
#şimdilik hata verecek

kitap1
#şimdilik hata verecek
"""
###

class Kitap():
    def __init__(self,isim,yazar,sayfa_sayısı,tür): 
        print("Kitap Objesi oluşuyor....")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayısı = sayfa_sayısı
        self.tür = tür
kitap1 = Kitap("İstanbul Hatırası","Ahmet Ümit",561,"Polisiye") # Kendi metodumuz 


print(kitap1)


class Kitap():
    def __init__(self,isim,yazar,sayfa_sayısı,tür): 
        print("Kitap Objesi oluşuyor....")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayısı = sayfa_sayısı
        self.tür = tür
    def __str__(self):
        # Return kullanmamız gerekli
        return "İsim: {}\nYazar: {}\nSayfa Sayısı: {}\nTür: {}".format(self.isim,self.yazar,self.sayfa_sayısı,self.tür)
    def __len__(self):
        return self.sayfa_sayısı
    def __del__(self):
        print("Kitap objesi siliniyor.......")
kitap1 = Kitap("İstanbul Hatırası","Ahmet Ümit",561,"Polisiye") # Kendi metodumu

del kitap1
#artık üstte hata veren del metodu burda hata vermeyecektir

len(kitap1)
#artık üstte hata veren len metodu burda hata vermeyecektir