
arabaAudi= {
    "marka" : "Audi",
    "model" : "A5",
    "yıl" : 2019,
}

#değerlere erişme

sonuc = arabaAudi["marka"]
sonuc = arabaAudi.get("marka")

#sorgulama işlemleri

sonuc= "marka" in arabaAudi
sonuc= len(arabaAudi)

#ekleme işlemleri

arabaAudi["renk"] = "siyah"

#silme işlemleri

arabaAudi.pop("yıl")
arabaAudi.popitem()

del arabaAudi["marka"]
del arabaAudi

arabaAudi.clear()

#objeyi kopyalama

araba= arabaAudi.copy() #değişen değiştirme misali
araba["marka"] ="mercedes"

#değer güncelleme

arabaAudi.update(
    {
        "marka"= "BMW",
        "model"= 2022,
    }
)
print(sonuc)