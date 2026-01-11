num1=int(input("inter the string of the range"))
num2=int(input("inter the endding of them range"))
count=0
for i in range(num1,num2):
    if i%2!=0:
        count +=i
print(count)
