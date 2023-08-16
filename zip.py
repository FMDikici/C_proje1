liste1 = [1,2,3,4,5]
liste2 = [6,7,8,9,10,11]

# sonucu [(1,6),(2,7),(3,8),(4,9),(5,10)] yapmaya çalışalım.
#zip olmadan aynısını yapmak
"""i = 0
sonuç = list()
while (i < len(liste1) and i < len(liste2)):
    sonuç.append((liste1[i],liste2[i]))
    
    i +=1
print(sonuç)"""
#[(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]

#zip ile yapmak
"""
zip(liste1,liste2) #bellekte nerde oldugunu gösteriyor
list(zip(liste1,liste2))
"""

# Sözlükleri zipleyelim.
"""
sözlük1 = {"Elma":1,"Armut":2,"Kiraz":3}
sözlük2 = {"Sıfır":0,"Bir":1,"İki":2}
list(zip(sözlük1,sözlük2)) # Anahtarlar eşleşti.
[('Elma', 'Sıfır'), ('Armut', 'Bir'), ('Kiraz', 'İki')]
list(zip(sözlük1.values(),sözlük2.values())) # Değerler eşleşti
[(1, 0), (2, 1), (3, 2)]
"""