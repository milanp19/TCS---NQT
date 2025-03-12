# Write a program to display all the multiples of 3 within the range n and m. Read the value of n and m from the first two lines of the console as input. Print all the multiples of 3 within the range of n and m as output (exclude n and m).

# Kindly check the sample test case for more clarity.

# Input Format

# 10 50

# Constraints

# NA

# Output Format

# 12 15 18 21 24 27 30 33 36 39 42 45 48

n = int(input())
m = int(input())

i = n + 1
while i < m:
    if i % 3 == 0:
        print(i, end = " ")
    
    i += 1