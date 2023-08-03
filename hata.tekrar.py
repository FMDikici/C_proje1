def terscevir(c):
    if type(c)!=str:
        raise ValueError("lutfen duzgun input giriniz.")
    else:
        return c[::-1]
    
print(terscevir("python"))

print(terscevir(15))