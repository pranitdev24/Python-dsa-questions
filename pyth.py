"""num=int (input ("enter the number"))
lenth=len(str(num))
sun_=0
tem=num
while tem>0:
    dig=tem%10
    sum_ += dig ** lenth
    
    num//=10

if sum==num:
        print("It is the armstopng number")
else:
        print("not the armstrong number")        """



num = int(input("Enter the number: "))
length = len(str(num))
sum_ = 0
tem=num

while tem > 0:
    dig = sum % 10
    sum_ += dig ** length
    sum //= 10

if sum_ == num:
    print("It is an Armstrong number")
else:
    print("Not an Armstrong number")