def fibonacci(deger):
    if (deger<2):
        return 1
    else:
        return fibonacci(deger-1)+fibonacci(deger-2)
    

deger=int(input("sayiyi girinz:"))

a=fibonacci(deger)

print(a)




