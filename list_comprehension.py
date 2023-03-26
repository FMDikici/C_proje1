for i in range(10):
    i**=2
    print(i)

sayilar=[i**2 for i in range(10)]    

print(sayilar)

#synı işlemi görür biri yukarıdan aşşağı biri tek sıra


"""
koşul ile nasil olur
"""

sayilar=[1,3,7,12,22,34]
sonuc=[]

for sayi in sayilar:
    if (sayi%2==0):
        sonuc.append(sayi)
        print(sonuc)    
#.append bir diziyi başka bir diziye eklemek          

