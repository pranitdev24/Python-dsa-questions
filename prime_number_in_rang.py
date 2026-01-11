num1 = int(input("Enter the starting of the range: "))
num2 = int(input("Enter the end of the range: "))

primes = []

for i in range(num1, num2 + 1):
    if i > 1:  # prime numbers are greater than 1
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            primes.append(i)

print("Prime numbers are:", primes)






