no=int(input("enter the value"))
flag=0
for s in range(2,int(no)):
    #print(s)  
    if(int(no)%s==0):
        flag=1
        break
    
    
if(flag==0):
    print("the given number is prime number",no)
else:
    print("the given nuber is not prime number",no)



