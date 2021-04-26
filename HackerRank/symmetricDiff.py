# Link -> https://www.hackerrank.com/challenges/symmetric-difference/problem

n = int(input())
set1 = set(map(int, input().split()))

m = int(input())
set2 = set(map(int, input().split()))

print(*sorted(list((set1.difference(set2)).union(set2.difference(set1)))), sep = "\n")