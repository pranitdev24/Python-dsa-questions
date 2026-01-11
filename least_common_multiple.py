a=int(input("enter the first number"))
b=int(input ("enter the second number"))
if(a>b):
    minm1=a
else:
    minm1=b
    while(1):
        if (minm1%a==0 and minm1%b==0):
            print("LCM is :", minm1)
            break
            
        minm1=minm1+1