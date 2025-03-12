# Given an integer array nums, print "true" if any value appears at least twice in the array, and print "false" if every element is distinct.

# Read n, the number of values in the first line, followed by the comma-seperated n numbers in the next line.

n = int(input())
arr = list(map(int, input().split()))

if len(set(arr)) == len(arr):
    print("false")
else:
    print("true")