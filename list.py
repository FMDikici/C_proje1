#c'deki diziler ile aynı anlama geliyor

yazi="benim adim fatih dikici. kayseri'de yasiyorum".split()
#split metodu her kelimeyi tek tek dizi elemani yapar.

print(yazi[1]) #adim yazdı

print(yazi[0][1]) #benim'den e harfini yazdirdik

sayilar= [1,2,3,4,5,6]

sonuc=sayilar
sonuc=sayilar[0]

print(sonuc)

#listemert=["mert",18]
#listefatih=["fatih",20] 
ogrenciler= [["mert",18],["fatih",20]]
#ogrenciler= [[listemert],[listeceyda]]
print(ogrenciler[0])
print(ogrenciler[0][1])