def Mondat_szabdalo(name):
    betuszam={}
    szam=0
    for x in mondat:
        for y in mondat:
    
            if  x==y:
                szam=szam+1
                betuszam[x]=szam
        szam=0       
    print("betuk gyakorisága:",betuszam)
    print("fordítva: "+mondat[::-1])
    szolista=[mondat.split(' ')]
    print(szolista)
def converter(name,int):
    ered=0.0
    if mertekegyseg=="inch":
        ered=(szam)*2.54
        print(ered,"cm")
    elif mertekegyseg=="cm":
        ered=szam/2.54
        print(ered,"inch")
    else:
        print("Not correct unit")
    


        


if __name__ == "__main__":
    mondat=input("Adjon egy mondatot:")
    Mondat_szabdalo(mondat)
    szam=float(input("Adjon meg egy számot:"))
    mertekegyseg=input("Adjon meg egy mértékegységet (cm/inch):")
    converter(szam,mertekegyseg)
