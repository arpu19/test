class A:
    
    def fact(self,num):
        num=num
        fact=1
        for i in range(1,num+1):
            fact= fact*i
        print("factorail nuber",fact)
        

    def prime(self,no):
    #print(no)
        f=0   
        for s in range(2,int(no)):  
         if(int(no)%s==0):
            f=1
            break
        if(f==0):
            print("the given number is prime number",no)
        else:
            print("the given nuber is not prime number",no)  

    def my_fibo(self,numm):
        a=0
        b=1
        while(int(numm)>0):
            c=a+b
            print("fibo of number",c)
            a=b
            b=c
            numm=int(numm)-1
    
    def  Table(self,num):  
     i= 1
     while(i<=10):
      print(num*i)
      i+=1

    def findOdd(self,n1,n2):
        while(n1<=n2):
            if(n1%2!=0):
                print(n1," The number is odd number:")
            n1+=1 




    
   
    



a = A()
a.fact(5)
a.prime(8)
a.my_fibo(6)
a.Table(5)
a.findOdd(30,40)

  












