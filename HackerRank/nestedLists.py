# Link -> https://www.hackerrank.com/challenges/nested-list/problem

marks = []
students = []

for _ in range(int(input())):
    name = input()
    mark = float(input())
    students.append([name, mark])
    marks.append(mark)
minimum = sorted(list(set(marks)))[1]

for student in sorted(students):
    if student[1] == minimum:
        print(student[0])

