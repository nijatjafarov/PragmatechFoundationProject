# Link -> https://www.hackerrank.com/challenges/finding-the-percentage/problem

n = int(input())
students = {}
for _ in range(n):
    student = input().split()
    students[student[0]] = list(map(float, student[1:]))

calledStudent = input()
print(sum(students[calledStudent])/len(students[calledStudent]))

# Netice float .0 verir, HackerRank .00 isteyir