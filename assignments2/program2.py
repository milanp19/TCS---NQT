# Write a program to find the average of n numbers using a while loop. Read an integer, n from the console, which will be the number of values.

# Write a while loop to read n numbers from the console and find the average of all these numbers. Print the average value as the output with a precision of 3 decimal places.

# Input Format

# 3 4.5 5.5 6

# Constraints

# NA

# Output Format

# The average is: 5.333


n = int(input())
i = 0
res = 0
while i < n:
    num = float(input())
    res += num
    i += 1
    
print(f"The average is: {(res / n):.3f}")