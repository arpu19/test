def fact(num):
    fact=1
    for i in range(1,num+1):
        fact= fact*i
    return fact


print("the fact is" ,fact(5))

