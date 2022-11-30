name= 'fatih'
surname= 'dikici'
age= '19'

text= " merhaba benim adım " + name + " soyadım ise " + surname + " yaşım da " + age + "."

print(text[1]) #ilk harfi gösterir
print(text[15]) # 15. harfi gösterir
print(text[8]) #8 boşluğa denk geliyor terminalde boşluk olur
print(text[-2]) #sağdan 2 sayı sayıp o harfi seçer

print(text[0:9]) #0'dan 9'a kadar hepsini alır
print(text[1:25]) #1'den başlayıp 25'e kadar (merhaba benim adım fatih)
print(text[:19]) #nerden başlayacağını demedik ama duracağı yeri söyledik (merhaba benim adım)
print(text[10:]) #10dan başlayıp bitene kadar

print(text[-20 :-1]) #tersten okur (dikici yaşım da 19)
print(text[-23:]) #tersten okur başlangıç belli değil ama sonu belli(ise dikici yaşım da 19)


print(text[10:36:2]) #10'dan 36'ya kadar 2'şer şekilde gider
print(text[::2]) #baştan sona 2'şer ilerleyip gider
print(text[::-3]) #sondan başa 3'er 3'er gider









