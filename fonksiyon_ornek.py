"""
1.
def fonksiyon(x):
    if x==0:
        return 1
    else:
        return x*fonksiyon(x-1)
    
sonuc=fonksiyon(5)

print(sonuc)


2.

def fibonacci(x):
    if x<=2:
        return 1
    else:
        return fibonacci(x-1)+fibonacci(x-2)
    
sonuc=fibonacci(6)    

print(sonuc)



3.
def rakamToplami(x):
        if len(str(x)) == 1:
            return int(x)
        else:
            return int(str(x)[0]) + rakamToplami(str(x)[1:])
        
sonuc=rakamToplami(45)
print(sonuc)        


4.

def degisim(yil):
    if yil==0:
        return 5000
    else:
        return degisim(yil-1)*0.9
    
while(a!=0):
    a=input("sayi gir")
    a+=1
    b=degisim(a)
    print(b)


5.


def topla(islem):
    toplam=0

    for i in islem:
        toplam+=i
        return toplam

print(topla([1,2,3,4]))

"""

6.

def topla(liste):
    if (len(liste)) == 0:
        return 0
    else:
        return liste[0] + (topla(liste[1:]))
    
print(topla([1,2,3,4]))