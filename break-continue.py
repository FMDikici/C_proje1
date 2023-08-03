"""defkullanici=12345
defparola=123456

while(True):
    kullanici=input("girin")
    parola=input("girin")
    if((defkullanici!=kullanici) or (defparola!=parola)):
        print("Tekrar Deneyiniz:")
    else:
        print("Tebrikler")
        break
"""

i=0

while(i<10):
    print(i)
    if(i==2):
        continue
    i+=1