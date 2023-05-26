class Diak:
    def __init__(self,nev,osztaly,szuletesiev):
        self.nev=nev
        self.osztaly=osztaly
        self.szuletesiev=szuletesiev
    def eletkor(self):
        r=2023-szuletesiev
    def mondat(self):
        return "szia, "+nev+" vagyok, a "+osztaly+" osztályba járok, "+str(self.kor)+" éves vagyok."
                                                                           
diak=[]
nev=input("Név: ")
osztaly=input("Osztály: ")
szuletesiev=int(input("Születési év: "))
diak1=Diak(nev,osztaly,szuletesiev)
diak.append(diak1)


print(diak1)
