print("Adjon egy mondatot:")
mondat=input()


betuszam={}

print("betuk gyakorisága ")
print(betuszam)
print("fordítva: "+mondat[::-1])
szolista=[mondat.split(' ')]
print(szolista)





print("Adjon meg egy számot és egy mértékegységet (cm/inch):")
szam=float(input())
mertekegyseg=input()
ered=0.0
if mertekegyseg=="inch":
    ered=(szam)*2.54
    print(ered)
    print("cm")
elif mertekegyseg=="cm":
    ered=szam/2.54
    print(ered)
    print("inch")
else:
    print("Not correct unit")


