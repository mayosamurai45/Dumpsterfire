def beolvas():

    
    adatLista=[]
    with open ("D:\dumpsterfire projects\Dumpsterfire\playlist.csv","r", encoding='utf-8') as file:
        for sor in file:
            seged=sor.split(";")
            szotar=dict(eloado = seged[0], cim = seged[1], mufaj = seged[2],hossz=int(seged[3]))
            adatLista.append(szotar)
        return adatLista
def teljes(adat):
    szamlalo=0
    seged=[]
    for rekord in adatok:
        szamlalo+=rekord["hossz"]
        
    szamlalo=szamlalo/60
    seged=str(szamlalo).split(".")
    print("perc:"+seged[0]+" masodperc:"+seged[1] )
    with open (r"D:\dumpsterfire projects\Dumpsterfire\02_hossz.txt ","w", encoding='utf-8') as file:
        file.write("perc:"+seged[0]+" masodperc:"+seged[1] )
def leghoszabb(adat):
    leghoszabb=""
    for rekord in adatok:    
        if rekord["mufaj"]=="rock" and len(rekord["cim"])>len(leghoszabb):
            leghoszabb=rekord["cim"]
    print (leghoszabb)
    with open (r"D:\dumpsterfire projects\Dumpsterfire\03_hossz.txt ","w", encoding='utf-8') as file:
        file.write(leghoszabb)
def leggyakoribb(adat):
    
    lista=[]
    for rekord in adatok:
        if rekord["mufaj"] not in lista:
            szotar=dict(mufaj=rekord["mufaj"],menny=1)
            lista.append(szotar)
        else:
            for x in lista:
                if x["mufaj"]==rekord["mufaj"]:
                    x["menny"]+=1
    legnagyobb=0
    vegso=""
    for y in lista:
        if y["menny"] > legnagyobb:
            legnagyobb=y["menny"]
            vegso=y["mufaj"]
    print(vegso)
    lista.sort()
        
    
if __name__== "__main__":
    adatok=beolvas()
    teljes(adatok)
    leghoszabb(adatok)
    leggyakoribb(adatok)
    
        
        
    
    
        



























    

    
