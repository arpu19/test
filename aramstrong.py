def aramstrong(num):
       
        sum=0 
        temp=num
        revno=0

        while temp > 0:
                revno= temp%10
                sum+=revno*revno*revno
                temp=temp//10
                print(revno)        


        if sum==num:
                print(num,"The given number is Armstrong")
        else:
                print(num,"The  given number is not Armstrong")   

a=aramstrong(153)



        