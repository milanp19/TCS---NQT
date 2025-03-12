# Write a program to check whether the given integer is a prime number or not. Read an integer from the console as input.

# If the integer is a prime number, print "n is a prime number", where n is the value of the integer. Else, print "n is not a prime number".

# Kindly check the sample test case for more clarity.

# Input Format

# 7

# Constraints

# NA

# Output Format

# 7 is a prime number

n = int(input())

for i in range(2, n//2):
    if n % i == 0:
        print(f"{n} is not a prime number")
        break
else:
    print(f"{n} is a prime number")