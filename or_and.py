#and operator kullanımı

x=15
sonuc=10<x<20
# (x>10) and (x<20) diye de yazılabilir

"""
true and true ==> true
true and false ==> false
false and false ==> false
"""


print(sonuc)

#or operatoru

"""
true or true ==> true
true or false ==> true
false or false ==> false
"""

sonuc=(x<10) or (x%3==0)

sonuc=not(x>0)

print(sonuc)