filter(lambda x : x % 2 == 0, [1,2,3,4,5,6,7,8,9,10])
#<filter at 0xa4bab50438> list koymadık
list(filter(lambda x : x % 2 == 0, [1,2,3,4,5,6,7,8,9,10])) # Çift olan sayılar [2, 4, 6, 8, 10]

def asal_mi(x):
    i = 2
    if (x == 1):
        return False # Asal değil
    elif(x == 2):
        return True # Asal sayı
    else:
        while(i < x):
            if (x % i == 0):
                return False # Asal Değil
            i += 1
    return True

asal_mi(34)
#False
asal_mi(2)
#True
asal_mi(1)
#False
asal_mi(3)
#True
asal_mi(4)
#False

list(filter(asal_mi,range(1,100))) # 1 den 100' e kadar olan asal sayılar.