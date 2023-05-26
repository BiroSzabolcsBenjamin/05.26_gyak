class Negyzet:
    def __init__(self,oldal):
        self.oldal=oldal
    def kerulet(self):
        return 4*oldal
    def terulet(self):
        return oldal*oldal

negyzet=[]
oldal=int(input("Oldal hossza: "))
negy=Negyzet(oldal)
negyzet.append(negy)

print("A négyzet kerülete: ",negy.kerulet(),"cm")
print("A négyzet területe: ",negy.terulet(),"cm²")