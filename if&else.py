"""
ad=input("adinizi giriniz")
print("hosgeldiniz ", ad)
"""
"""
kacKarakter=len(ad)
print("isminiz  {} karakterden olusuyor".format(kacKarakter))
"""

vize=int(input("vize notunuzu giriniz:"))
final=int(input("final notunuzu giriniz:"))

ort= vize*0.4+final*0.6

if(ort>=80):
    print("AA ile geçtiniz")
elif(ort<80 and ort>=60):
    print("BB ile geçtiniz")
elif(ort<60 and ort>=40):
    print("CC ile geçtiniz")
elif(ort<40 and ort>=20):
    print("DD ile şartli geçtiniz")
else:
    print("FF ile kaldiniz")     