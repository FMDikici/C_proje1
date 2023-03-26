
name="fatih"
age=20
weight=80.5
isStudent=True


print(type(name))
print(type(age))
print(type(weight))
print(type(isStudent))

#float to int

result= float(age)

print(result)
print(type(result))

#int to float

result= int(weight)

print(result)
print(type(result))

#str to bool

result= bool(name)

print(result)
print(type(result))

#bool to str

result=str(isStudent)

print(result)
print(type(result)) 



name='hatice'
surname='şaşkın'
age='35'

exam='merhaba benim adım' +' '+ name +' '+ surname +' ' + 'yaşım ise'+' ' + age +'.'



print(exam[4])
print(exam[10:18])
print(exam[1:30:4])

print(exam[-25:-3:4])

name='fatih'
surname='dikici'
age=19

print('hello my name is {}'.format(name))
print('hello my name is {n} {s}'.format(n=name,s=surname))
print('hello my name is {0} {2} . i am {1} years old' .format(name,surname,age))

number=5/3

print('the result is {n:1.3}'.format(n=number))


yazi='merhaba herkese.benim adım fatih dikici.20 yaşındayım'

"""result=yazi.upper()
result=yazi.lower()"""
result=yazi.islower()


print(result)