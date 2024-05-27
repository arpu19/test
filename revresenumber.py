def my_aramstrong(no):
    r=0
    org=no
    qsum=0
    while(int(no) > 0):
        r=int(no)%10
        no=int(no)/10
        qsum+=r*r*r
        print(r)
    print("qsum: ",qsum)
    if org == qsum:
        print(org," is Aromstrong number")
    else:
        print(org," is no an armstrong number")    


my_aramstrong(154)



