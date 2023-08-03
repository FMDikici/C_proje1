"""liste=["345","sadas","324a","14","kemal"]

for eleman in liste:
    try:
        eleman=int(liste)
        print(liste)
    except:
        pass
"""
"""
def çift_mi(sayı):
    
    if (sayı % 2 == 0):
        return sayı
    else:
        raise ValueError
liste = [34,2,1,3,33,100,61,1800]

for i in liste:
    try:
        print(çift_mi(i))
    except ValueError:
        pass    
        """"

a = int("324234dsadsad") # Burası ValueError hatası veriyor.

try:
    
    a =  int("324234dsadsad") # Burası ValueError hatası veriyor.
    print("Program burada")
except: # Hatayı belirtmezsek bütün hatalar bu kısma giriyor.
    print("Hata oluştu")  # Burası çalışır.
    
print("Bloklar sona erdi")