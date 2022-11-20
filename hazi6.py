

if __name__=="__main__":
    sorok=""
    ujsorok=""
    
    tilos=[".","!","?","-","a","á","e","é","i","í","o","ó","ö","ő","u","ú","ü","ű","\n",","," ","\""]
    with open(r"hazi.txt", 'r',encoding='utf8') as file:                
        sorok=file.read().lower()
    for betu in sorok:
        if betu not in tilos:
            ujsorok+=betu
    with open(r"haziatirt.txt", 'w',encoding='utf8') as file:
        file.write(ujsorok)
 
    
        

           


        
            
    
      
        
    






