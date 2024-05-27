def my_fun(no):
    #print(no)
    f=0
    for s in range(2,int(no)):  
        if(int(no)%s==0):
            f=1
            break
    if(f==0):
        print("the given number is prime number",no)
    else:
        print("the given nuber is not prim,e number",no)

my_fun(6)


