def double(x):
    return x * 2

map(double,[1,2,3,4,5,6,7]) # fonksiyon bir tane argüman alıyor ve listenin her bir elemanı üzerinde uygulanıyor.
#<map at 0x5522e9e208> çıktısını verir int almak için list içine koymak gerek

list(map(double,[1,2,3,4,5,6,7]))
list(map(double,(1,2,3,4,5,6,7)))

#Buradaki fonksiyonları lambda ifadeleriyle de yazabiliriz.

map(lambda x : x ** 2, [1,2,3,4,5,6,7,8,9])
#<map at 0x5522e9e438> çıktısı (yine list içine girmesi gerek)
list(map(lambda x : x ** 2, [1,2,3,4,5,6,7,8,9]))


liste1 = [1,2,3,4]
liste2 = [5,6,7,8]
liste3 = [9,10,11,12,13]

map(lambda x,y : x * y , liste1,liste2)
list(map(lambda x,y : x * y , liste1,liste2))
list(map(lambda x,y,z : x * y * z , liste1,liste2,liste3))
