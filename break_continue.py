"""
isimler="Fatih Mehmet Dikici"

for i in isimler:
    if(i== "e"):
        break
    print(i)
"""
"""
i=0

while (i<10):
    i+=1
    if (i==5):
        continue
    print(i)
"""
#while döngüsü ile 100'e kadar tek sayıları yazdırma
i=0
toplam=0
while(i<100):
    i+=1
    if(i%2==0):
        continue
    toplam=toplam+i
print(toplam)