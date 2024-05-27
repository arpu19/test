def my_fibo(num):
    if(num==0):
        return 0
    elif(num==1):
        return 1
    else:
        return(my_fibo(num-1) + my_fibo(num-2))
          

my_fibo(5)
print("the fibo of number is",my_fibo(5))



    