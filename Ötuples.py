list1=[1,2,3,4] 

thistuple=(1,2,"altı",False)

print(type(list1))  #liste biçiminde
print(type(thistuple)) #demet biçiminde

#TUPLESTEKİ AMAÇ YAZILAN KODUN DEĞİŞMESİNİ,EKLENMESİNİ ENGELLEMEKTİR(GÜVENLİK VB.)

print(list1[0])
print(thistuple[0])
print(len(list1))
print(len(thistuple))
#len metodu içersinide kaç tane öğe olduğunu gösterir.!!!

list1[0]= 6
print(list1)

"thistuple[2]=4"
"print(thistuple)"
#demetlerde değiştirme olamaz!

list1.append(10)
print(list1)

"thistuple.append(40)"
"print(thistuple)"
#demetlere ekleme yapamazsın!

print(list1.count(2))
print(thistuple.count(1))
#ikisinde de içine kaç tane olduğunu sorabilirsiniz

print(list1[0])
print(thistuple[1])




