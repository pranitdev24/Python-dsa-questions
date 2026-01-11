print("welcom to number guessing game")

import random
num=random.randint(1,5)
print(num)
guess = True
while guess:
    inpnum=int(input("inter the number"))
    if inpnum<num:
         print("too low")
    elif inpnum>num:
        print("too high")    
    elif inpnum==num:
        print("mmmm")
        break



    
    
