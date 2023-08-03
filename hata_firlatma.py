# Verilen string'i ters çevirmek
def terscevir(s):
    if(type(s)!=str):
        raise ValueError("lütfen doğru bir input giriniz")
    else:
        return s[::-1]

print(terscevir("Python"))
 
print(terscevir(15)) 
""" ---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
 in ()
----> 1 print(terscevir(12))

 in terscevir(s)
      2 def terscevir(s):
      3     if (type(s) != str):
----> 4         raise ValueError("Lütfen doğru bir input girin.")
      5     else:
      6         return s[::-1]

ValueError: Lütfen doğru bir input girin.  
"""