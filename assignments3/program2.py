# You will be given a list of integers, arr, and a single integer k. You must sort the numbers in ascending order and create an array of length k from elements of arr to minimize its unfairness. Call that array arr’. Unfairness of an array is calculated as = max(arr’) – min(arr’)

# Where:- max denotes the largest integer in arr’- min denotes the smallest integer in arr’

# Input Format

# 1,11,25,98,66,53 4

# Constraints

# NA

# Output Format

# 1 11 25 53

arr = list(map(int, input().split(',')))
k = int(input())

res = None
arr = sorted(arr)
min_unfairness = float('inf')

for i in range(len(arr) - k + 1):
    window = arr[i:i+k]
    max_ele = max(window)
    min_ele = min(window)
    
    unfairness = max_ele - min_ele
    if unfairness < min_unfairness:
        min_unfairness = unfairness
        res = window
    
print(*res)