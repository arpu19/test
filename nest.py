def nest(a,b,c):
    if(a>b):
        
        if(a>c):
            print("The A is greater number:",a)
        else:
            print("The 3rd  number is greater number:",c)
    else:
        if(b>c):
            print("b is greater number",b)
        else:
            print("c is greter number",c)


a=int(input("Enter the 1st  number: "))
b= int(input("Enter the 2nd number:"))
c = int (input("Enter the 3rd  number:"))

nest(a,b,c)