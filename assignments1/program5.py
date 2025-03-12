# Given a sorted (in ascending order) integer array nums of n elements and a target value, find if there exists any pair of elements (nums[i], nums[j], i!=j) such that their sum is equal to target.

# Input Format

# 5 -3 -1 0 1 2 -2

# Constraints

# 1 < nums.length <100

# Output Format

# Yes

n = int(input())

arr = map(int, input().split())
target = int(input())

l = []
for num in arr:
    c = target - num
    if num not in l:
        l.append(c)
    else:
        print("Yes")
        break
else:
    print("No")