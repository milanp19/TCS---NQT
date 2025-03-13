# Write a program that takes an array that denotes the daily closing prices of a stock to determine the maximum profit by buying and selling one share of the stock.

# Input Format

# 310,315,275,260,270,290,230,255,250

# Constraints

# NA

# Output Format

# 30

arr = map(int, input().split(','))
min, max = float('inf'), 0

for num in arr:
    if num < min:
        min = num
        
    elif num - min > max:
        max = num - min

print(max)