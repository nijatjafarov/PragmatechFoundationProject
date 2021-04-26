# Link -> https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

n = int(input())
nums = input()

numSet = set(map(int, nums.split(" ")))

numSet.discard(max(numSet))
print(max(numSet))
