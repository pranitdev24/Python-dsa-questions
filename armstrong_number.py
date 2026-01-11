num=int(input("inter the number to chake"))
lenth=len(str(num))
sum=0
tem=num
print(lenth)
while tem >0:
    digit=tem%10
    cube=digit**lenth
    sum+=cube
    tem//=10

if sum==num:
    print("yes")
else:
    print("no")
        


        




