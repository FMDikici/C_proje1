#list içindekileri değişir
#tuple içindekileri değişmez ve daha hızlı
#dictionary anahtar-kilit işlemi
#sets index(sıralama) yok ve değişmez

markalar={"Audi","Mercedes","Bmw","Toyota"}
markalar2= {"Renault","Mazda","Honda"}
"""
sonuc= markalar[0] #sets'de böyle olmuyor
"""
sonuc= "Bmw" in markalar #True

markalar.add("Opel") #sona koymaz rastgele
markalar.update(["Honda","Skoda"])

sonuc= len(markalar)  #silmek istediğimizi belirtiyorsak remove komutu lazım
markalar.remove("Opel")
sonuc= markalar.pop() #rastgele siler
markalar.clear() #liste içini tamamen siler
sonuc=markalar.union(markalar2) #2 set listesini birleştirir


