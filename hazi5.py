

if __name__=="__main__":
    elrendezes = "{0:>4}{1:>6}{2:>6}{3:>4}{4:>4}{5:>4}{6:>4}{7:>4}{8:>4}{9:>4}{10:>4}{11:>4}"

    print(elrendezes.format("1", "2","3", "4","5", "6","7", "8","9", "10","11", "12" ))
    print(":---------------------------------------------------")
    for i in range(1,13):
        print( elrendezes.format(i, i*2, i*3,i*4, i*5, i*6,i*7,i*8,i*9,i*10,i*11,i*12))
    szo=input("kérek egy szöveget: ")
    munka=""
    for betu in szo:
        if betu !=" ":
            munka+=betu
    igazsag=True
    for i in range(0,len(munka)):
        if i==0:
            if munka[i]!=munka[-1]:
                igazsag=False
        else:    
            if munka[i]!=munka[-(i+1)]:
                igazsag=False
    if igazsag==False:
        print("a szó nem palindróm")
    else:
        print("A szó palindróm")






