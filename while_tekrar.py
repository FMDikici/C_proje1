#tek-çift sayi
"""
i=1
while (i<50):
    if (i%2==1):
        print("{0} tek sayi".format(i))
    else:
        print("{0} cift sayi".format(i))
    
    i+=1
"""
"""
i=0
result=0

while(i<100):
    i+=1
    if(i%2==1):
        continue
    result+=i
    
    print({result})
    """

baslangic=int(input("baslangic degeri giriniz"))
bitis=int(input("bitis degeri giriniz"))

i=baslangic

while(i<bitis):
    i+=1
    if(i%2==1):
        print(i)