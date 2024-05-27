def statement(a,b,c):
    if a>b and a>c :
        print("The  greater number:",a)
    elif b>a and b>c:
        print("The greater number:",b)
    else:
        print("The greater number:",c)
  

a = int(input("Enter the 1St number:"))
b = int(input("Enter the  2nd number:"))
c = int(input("Enter the  3rd number:"))
statement(a,b,c)        