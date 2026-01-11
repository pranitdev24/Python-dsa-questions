# def pyramid(height):
#     for i in range(1, height + 1):
#         print(" " * (height - i) + "*" * (2 * i - 1))

# def diamond(height):
#     # Upper pyramid
#     for i in range(1, height + 1):
#         print(" " * (height - i) + "*" * (2 * i - 1))
#     # Lower inverted pyramid
#     for i in range(height - 1, 0, -1):
#         print(" " * (height - i) + "*" * (2 * i - 1))

# # Example usage
# patternType = "pyramid"  # Change to "diamond" for diamond pattern
# height = 5

# if patternType.lower() == "pyramid":
#     pyramid(height)
# elif patternType.lower() == "diamond":
#     diamond(height)
# else:
    # print("Invalid pattern type. Choose 'pyramid' or 'diamond'.")

#TO PRINTH STEAR PRAMIT

# n=int(input ("enter the number of the row"))
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for j in range(i+1):
#         print("*",end=" ")    
#     print()    
#TO PRINT THE ULTA PRAMIT

# num=int(input("enter the number of the row "))
# for i in range (num):
#     for j in range (i):
#         print(" ",end="")
#     for j in range (2*(num-i)-1)  :#we can also use (num-i)
#         print("*",end="")
#     print()      


# n=int(input("enter the number of the row"))
# for i in range (n):
#     for j in range(n):
#         if i==0  or j==0 or i==(n-1) or j==(n-1)or i==j or i+j==(n-1):
#             print("*",end="")
#         else:
#             print(" ",end="")    
#     print() 

#TO FIND THE FACTOEAL OF THE NUMBER

# num=int(input("enter the number that factorial you want to find"))
# fat=1
# for i in range (1,num+1):
#     fat=i*fat
# print(f"the factorial of the {num} is ",fat)
 #TO FIND THE SUM OF THE DIGIE OF THE NUMBER 
# 

# arry=[4,5,4,7,8,6]
# arry.sort()

# smallest=arry[0]

# big=arry[-1]
# print(f"big number :{big}")
# print(f"smallest numbr:{smallest}")

# def hepp():
#     print("happy birthday")


# hepp()

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        return()

    def _init_ (self):
        print("Name:", self.name)
        print("Age:", self.age)
        return()
a=Student()
        