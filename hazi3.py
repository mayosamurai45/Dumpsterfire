def oszto(*float):
    try:

        print(a/b)
    except ZeroDivisionError:
        print("Division by zero not allowed")
    finally:
        print("Out of try except blocks")
        

if __name__=="__main__":
    while 1==1:
        a=float(input("enter 'a' value: "))
        b=float(input("enter 'b' value: "))
        oszto(a,b)
    
