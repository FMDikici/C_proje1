yazi="merhaba adım fatih mehmet dikici. kayseri'de yaşıyorum."


sonuc=yazi.upper() #tüm harfleri büyütür
sonuc=yazi.lower() #tüm harfleri küçültür
sonuc=yazi.title() #ilk harfleri büyük yapar
sonuc=yazi.capitalize() #cümleyi büyük harfle başlatır
sonuc=yazi.islower() #is soru sorar (küçük mü)(bool fonksiyonu)

sonuc=yazi.strip() #boşlukları temizler 
sonuc=yazi.split() #boşluğa göre kelimeleri böler   """araya ne koyarsan ona göre de böler"""
sonuc="-".join(yazi) #her kelime arasına kısa çizgi koydu  """araya ne koyarsan ona göre de koyar"""

sonuc=yazi.index("fatih") #kaçıncı sıradan itibaren fatih dediğini söyler

sonuc=yazi.startswith("m") #cümlenin o yazılan kelime ile başlayıp başlamadığını onaylar True/False
sonuc=yazi.endswith("m") #cümlenin o yazılan kelime ile bitip bitmediğini onaylar True/False

sonuc=yazi.replace("kayseri" , "maraş") #yazılan kelimeyi değiştirmek için kullanılır
sonuc=yazi.replace("ı","i").replace("ş","s") #bu şekide ard arda değişim de yapılabilir

print(sonuc)

""" DAHA FAZLASINI https://www.w3schools.com/python/python_ref_string.asp DEN ÖĞRENEBİLİRSİN"""

