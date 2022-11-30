sayilar=(1,2,4,8,12,50,100)
harfler=("a","b","h","f","ğ","r")

sonuc=min(sayilar)
sonuc=max(sayilar)
"minimum ve maximum sonuçlarını söyler"

#ekleme
sayilar.append(20)
harfler.append("p")
sayilar.insert(3,11)
harfler.insert(4,"c")
"append sona ekler insert nereye koymak istersen"

#silme
sayilar.pop()
harfler.pop()
sayilar.remove(50)
"pop sondan silmeye başlar ama remove belirttiğini siler"

#sıralama
sayilar.sort()
harfler.sort()
sayilar.reverse()
"sort küçükten büyüğe reverse ise büyükten küçüğe sıralar"

print(sayilar.count(8)) #8'in kaç kere geçtiğine bakar
print(sayilar.index(12)) #12'nin kaçıncı indexte olduğunu söyler
sayilar.clear() #sayilar değişkeni içinde olan komutları siler


print(sonuc)