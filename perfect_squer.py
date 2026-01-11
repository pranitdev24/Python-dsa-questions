num=int(input("enter the the number the check= "))
i=1
perfect_squer=False
while i*i <=num:
    if i*i==num:
        perfect_squer=True
        break
    i +=1
if perfect_squer:
    print(f"{num} is perfect squer number")
else:
    print(f"{num} is not a perfect squer number")
