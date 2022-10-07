class team:
    def __init__(self,nev,projekt,szerep):
        self._nev=nev
        self._projekt=projekt
        self._szerep=szerep
        print("-- Developer létrehozva. -- ")
        print(self)
    def __str__(self):
        return self._nev + " a " + self._projekt + "-en dolgozik " + self._szerep + " szerepkorben"
def kozos(*team):
    print("bejuttottam")
    for developer in lista:
        
        for developermasik in lista:
            
            if developer._projekt==developermasik._projekt and developer._nev!=developermasik._nev:
                mondat=developer._nev+" és "+developermasik._nev+" dolgoznak egy projekten "
                print (mondat)
                lista.remove(developer)
                
        
if __name__=="__main__":
    lista=[]
    lista.append(team("jános","legyen","fennajánoshegyen"))
    lista.append(team("péter","legyen","pilóta"))
    kozos(lista)
    
    

    
