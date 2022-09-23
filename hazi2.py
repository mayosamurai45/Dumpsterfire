def haromszog_ellenor(*float):
    valasz=("A {},{} és {} oldalú háromszog")
    if aldal+boldal>=coldal and boldal+coldal>=aldal and aldal+coldal>=boldal:
        print(valasz.format(aldal,boldal,coldal), "szerkesztheto")
    else:
        print(valasz.format(aldal,boldal,coldal), "NEM szerkesztheto")

if __name__ == "__main__":
    aldal=input("a oldal (cm):")
    boldal=input("b oldal (cm):")
    coldal=input("c oldal (cm):")
    haromszog_ellenor(aldal,boldal,coldal)