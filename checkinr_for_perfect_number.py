number = int(input("Enter a number: "))

sum_of_divisors = 0

# Find divisors and sum them (excluding the number itself)
for i in range(1, number):
    if number % i == 0:
        sum_of_divisors += i

# Check if sum of divisors equals the number
if sum_of_divisors == number:
    print("Perfect Number")
else:
    print("Not a Perfect Number")