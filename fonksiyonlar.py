"""def faktoriel(numara):
    faktoriyel=1
    for i in range(1,numara+1):
        faktoriyel*=i
        print("faktoriyel:",faktoriyel)


sayi=int(input("faktoriyel giriniz:"))

faktoriel(sayi)

"""
"""
def kokbul(a,b,c):
    delta=(b*b-4*a*c)
    if(delta<0):
        print("Reel kok yok")
        return


x1=(-b - delta**0.5)/2*a
x2=(-b + delta**0.5)/2*a

a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

sonuc=kokbul(a,b,c)

print(sonuc)"""

def faktoriyel(sayi):

    if((sayi==0) or (sayi==1)):
        return 1
    else:
        return faktoriyel(sayi-1)*sayi
    
sayii=int(input("Sayiyi giriniz:"))    
a=faktoriyel(sayii)  

print(a)