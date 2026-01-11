a=int(input("enter the numbe a"))
b=int(input("enter the number b"))

while b>0:
    r=a%b
    a=b
    b=r

gcd=a
print("gcd is eqval to",gcd)    