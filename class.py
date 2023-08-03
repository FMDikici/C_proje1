class araba():
    model='toyota corolla'
    yil=2011
    hp=124
    renk='fume'

araba1=araba()

araba1.hp

class araba():
    def __init__(self):
        print("init cagirildi")


class araba():
    def __init__(self,model,renk,hp,yil):        
        self.model=model
        self.renk=renk
        self.hp=hp
        self.yil=yil

araba1=araba("toyota corolla","fume",124,2011)

araba1.hp