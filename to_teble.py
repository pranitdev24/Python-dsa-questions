num=int (input("inter the number which table you want to print  : "))
teb=0
for i in range(1,11):
    if i <=10:
        print(f"{num} * {i} = {num*i}")
