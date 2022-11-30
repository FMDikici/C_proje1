#34=>"istanbul"
#35=>"izmir"

sehirler= ["istanbul","izmir"]
plakalar= [34,35]

print(sehirler[0],plakalar[0])
print(sehirler.index("istanbul"))

#key-value

plakalar= {"izmir":35,"istanbul":34}
print(plakalar["izmir"])
print(plakalar["istanbul"])
#sonuclarını gösterdi

plakalar["eskişehir"]=26    
plakalar["bursa"]=16
#sözlüğe sonradan ekleme yapabilieriz

print(plakalar)

urunler={
    100:{
        "urunAdi": "monitör",
        "urunAcıklamasi": "16 inç",
        "garantiSuresi": 3,
        "urunFiyati": [800,944]
    }
    101:{
        "urunAdi": "ssd",
        "urunAcıklamasi": "256gb",
        "garantiSuresi": 2,
        "urunFiyati": [1500,1770]
    }
}
#sonuc=urunler

#print(sonuc)
#print(type(sonuc))

sonuc= urunler[100]["urunFiyati"]
tutar= urunler[100]["urunFiyati"][0] +urunler[101]["urunFiyati"][0]
print(tutar