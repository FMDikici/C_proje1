1.
import math
math.factorial(5) 

2.
import math as matematik #artık matematik olarak çağıracağız
matematik.factorial(5)

3.
from math import * #math modulünün içindeki her şeyi kullanıyoruz
factorial(5) 

4.
from math import ceil,factorial #sadece ceil ve factorial'i kullanabiliyoruz

#ilk önce faktoriyel fonksiyonu yazıp sonra modül entegre edersek modül uygulanır(en son neyse o)

"""kendi modülünü yazma
1. Herhangi bir tane klasör oluşturuyoruz.
2. Modülümüz ve deneme Python dosyamız aynı dizinde olması gerektiği için 2 tane Python dosyasını da bu klasör altında oluşturuyoruz.
3. modul1.py ve deneme.py dosyası oluşturuyoruz.
4. modull.py dosyasının içine istediğimiz kadar fonksiyonu yazıyoruz.
5. Son olarak da deneme.py dosyasının içinde bu modul1.py modülünü kullanıyoruz.
"""
#kapsamlı modul isterseniz pytohn klasorü içine atabilirsiniz(modul1 yapıp attık)