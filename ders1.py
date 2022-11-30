
from operator import truediv


urun1=7500
urun2=500

print(urun1+(urun1*0.18))

x=1
print(type(x))

y=7.45
print(type(y))

name="fatih"
print(type(name))

isStudent= True
print(type(isStudent))

a, b, name, isStudent = 10, 40.10, "Fatih", False

print(a, b, name, isStudent)


#bool to str

result=str(isStudent)
print(type(result))


#int to float 

result=float(40)
print(type(result))



name="fatih"
age=16
print("hello my name is {} i am {} years old".format (name,age))

print("my name is {n} i am {a} years old".format(n=name, a=age))

