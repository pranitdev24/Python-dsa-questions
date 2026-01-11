# recurionnum=int(input("enter the no"))
num=int(input("enter the no"))
def fact(n):
    
    if(n==1 or n==0):
        return 1
    

    return fact(n-1)  *  n
print(fact(num))