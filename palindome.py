no=0
r=0
sum=0
no=int(input("Enter the number"))
n=no
while(no>0):
    r=no%10
    no=no//10
    sum=sum+r

print("the sum of digits",sum)