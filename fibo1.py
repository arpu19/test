no=input("enter the number")
a=0
b=1
while(int(no)>0):
    c=a+b
    print("fibo of number",c)
    a=b
    b=c
    no=int(no)-1
    
def my_fibo(no):
    a=0
    b=1
    fibolist=[]
    while(int(no)>0):
        c=a+b
        print("fibo of number",c)
        fibolist.append(c)
        a=b
        b=c
        no=int(no)-1
    return fibolist





res=my_fibo(6)
print("result",res)



