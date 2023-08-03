#dosyayı otomatik kapatma
#encoding komutu türkçe karakterlerin yazılmasına izin verir

with open("bilgiler.txt","r",encoding="utf-8") as file:
    for i in file:
        print(i)

#ileri geri sarmak

#.tell() imlecin kaçıncı byte'da olduğunu bize söyler
#.seek(number) number değeri nerdeyse o karaktere gider

with open("bilgiler.txt","r",encoding="utf-8") as file:
    file.seek(3)
    icerik=file.read(10)
    print(file.tell)
    print(icerik)