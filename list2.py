#listelere yeni eleman ekleme,çıkarma güncellemeler

"""iller= ["istanbul","ankara","izmir","bursa"]

sonuc=iller
sonuc=iller[2]
sonuc=iller[0:2] #0 ve 1. indexleri yazar
sonuc=iller[1:] #1'den sona kadar yazar
sonuc=iller[-1] #sonuncu index yazar

iller[0]= "Tekirdağ" # istanbul yerine tekirdag yazdirdik
iller= iller +["adana"] #adanayi ekledik 
print(iller)

#liste elemanlarının sayisini almak için len fonksiyonu kullanılır(int olarak gelir)
#silmek için del yazilir
sonuc=len(iller)

print(sonuc)

del iller[0]
print(iller)

"""




fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
#belli bir şeyi sildi

print(fruits)
