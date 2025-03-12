# Write a program to find the count of odd numbers from a given integer array.

# The program will take the following as inputs :

# -> length of an integer array, n -> n number of elements

# If the total number of odd numbers is 4 in an integer array, then you need to print "Odd Elements: 4" without quotes.

# If there are no odd numbers within the integer array or the array is empty then print "No odd elements are present" without quotes.

# For example, Length of an integer array: 6 Elements are: 3, 5, 7, 10, 12, 15

# So the output will be, "Odd Elements: 4".

# Similarly for the case where no odd elements were found within the integer array.

# Length of an integer array: 4 Elements are: 10, 12, 50, 64

# So output will be, "No odd elements are present".

# Note:

# You can use/refer to the below given sample input and output to verify your solution.

# Input Format

# 6 3 5 7 10 12 15

# Constraints

# NA

# Output Format

# Odd Elements: 4

n = int(input())
count = 0
for i in range(n):
    num = int(input())
    
    if num % 2 != 0:
        count += 1
        
if count != 0:
    print(f"Odd Elements: {count}")
else:
    print("No odd elements are present")