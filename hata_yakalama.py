a = int("324234dsadsad") # Burası ValueError hatası veriyor

try:
    
    a =  int("324234dsadsad") # Burası ValueError hatası veriyor.
    print("Program burada")
except: # Hatayı belirtmezsek bütün hatalar bu kısma giriyor.
    print("Hata oluştu")  # Burası çalışır.
    
print("Bloklar sona erdi")

#veya

try:
    
    a =  int("324234") # Burası normal çalışıyor
    print("Program burada")
except ValueError: # Hatayı belirtirsek ValueError hatası bu kısma giriyor.
    print("Hata oluştu") # Hata olmadığı için çalışmadı.
    
print("Bloklar sona erdi")

try:
    a = int(input("Sayı1:"))
    b = int(input("Sayı2:"))
    print(a / b) 
except (ValueError,ZeroDivisionError):
    print("ZeroDivision veya ValueError hatası")  #ister tek tek istersen hepsi bir yerde

#//2

try:
    a = int(input("Sayı1:"))
    b = int(input("Sayı2:"))
    print(a / b) # Hata burada oluşuyor. ZeroDivisionError'a bloğuna giriyoruz.
except ValueError:
    print("Lütfen inputları doğru girin.")
except ZeroDivisionError:
    print("Bir sayı 0'a bölünemez.")
finally:
    print("Her durumda çalışıyorum.")
    #finally her durumda çalışması gereken kodlarda kullnılır
    #dosya kapamak gibi