num1=int(input("enter the staring number"))
num2=int(input("enter teh end number"))
sum=0
for i in range(num1,num2+1):
    if i%2==0:
        sum+=i
print(sum)
