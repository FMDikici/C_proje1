name="Fatih"
surname="Dikici"
age=19

print("My name is {}".format(name)) 
print("My name is {} {}".format(name,surname)) #Fatih Dikici
print("My name is {0} {1}".format(name,surname)) #Fatih Dikici
print("My name is {1} {0} ".format(name,surname)) #Dikici Fatih
print("My name is {n} {s} ".format(n=name,s=surname)) #değişken değiştirme ile
print("My name is {} {}. I'm {} years old".format(name,surname,age))
print("My name is {0}{1}.I'm {2} years old.{2}".format(name,surname,age))
print("My name is {n}{s}.I'm {a} years old.{a}".format(n=name,s=surname,a=age))#değişken değiştirme

number=5/3

print("the result is {n:1.3}".format(n=number))#sağdaki 3 virgülden sonra kaç basamak olacağı
print("the result is {n:1.7}".format(n=number))#sağdaki 7 virgülden sonra kaç basamak olacağı


number=7/3
print("the result is {n:1.5}".format(n=number))#sağdaki 3 virgülden sonra kaç basamak olacağı



"""%s - String (or any object with a string representation, like numbers)

%d - Integers

%f - Floating point numbers

%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

%x/%X - Integers in hex representation (lowercase/uppercase)
"""



