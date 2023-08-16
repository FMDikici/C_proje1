"""def hepsi(liste):
    for i in liste:
        if not i:
            return False
    return True
# Bütün değerler True ise True en az birisi False ise False döndürmek istiyoruz.
liste = [True,False,True,False,True]
        
hepsi(liste) # En az birisi False
"""

liste = [True,False,True,False,True]
all(liste)
#False
liste = [1,2,3,4,5]
all(liste)
#True


liste = [True,False,True,False,True]
any(liste)
#True
liste = [0,0,0,0,0,0,0]
any(liste)
#False