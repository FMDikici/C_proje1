from functools import reduce  # reduce fonksiyonu son sürümlerde functools modülüne taşındı.
reduce(lambda x,y : x + y , [12,18,20,10])

reduce(lambda x,y : x * y , [1,2,3,4,5])

reduce(lambda x,y : x * y , [3,4,5,10])

# reduce ile max fonksiyonu
def maksimum(x,y):
    if (x > y):
        return x
    else:
        return y

reduce(maksimum, [-2,1,100,35,32])
#basamak sistemi uygulanır