# Imagine you are helping a student with their mathematics homework which involves a lot of problems based on matrix addition. You decide to write a program to automate the task of adding two matrices, which would make the homework a breeze!

# Write a program to add two matrices. The program should:

# Prompt the user to enter the dimensions of the matrices (assume both matrices have the same dimensions).

# Accept the elements of the two matrices from the user.

# Display the two matrices.

# Add the two matrices.

# Print the resultant matrix.

# Kindly check the sample test case for input and output format.

# Input Format

# 2 2 1 2 3 4 5 6 7 8

# Constraints

# NA

# Output Format

# First Matrix: 1 2 3 4 Second Matrix: 5 6 7 8 Sum of the two matrices is: 6 8 10 12

m, n = map(int, input().split())

mat1 = [list(map(int, input().split())) for _ in range(m)]
mat2 = [list(map(int, input().split())) for _ in range(m)]

res = [[0 for _ in range(n)] for _ in range(m)]

for i in range(m):
    for j in range(n):
        res[i][j] = mat1[i][j] + mat2[i][j]

print("First Matrix:")
for i in mat1:
    print(*i)
    
print("Second Matrix:")
for i in mat2:
    print(*i)
    
print("Sum of the two matrices is:")
for i in range(m):
    for j in range(n):
        print(res[i][j], end = " ")
    print()
    