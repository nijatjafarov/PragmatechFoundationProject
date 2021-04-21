# Python sade suallar Vol.2, 1
values = ["Che", 5, 9]
amount = 0

for value in values:
  try:
    amount += int(value)
  except:
    print("There is a problem")
    break

print(amount)


# Python sade suallar Vol.2, 2
a = [10, 20, 30, 40, 10]
b = [15, 25, 33, 40, 11]


def checkNum(list1, list2):
  for num in list1:
    if num in list2:
      return True
  return False


print(checkNum(a, b))


# Python sade suallar Vol.2, 3
import random
colors = ['Red', 'Blue', 'Green', 'White', 'Black']

print(colors[random.randint(0, 4)])


# Python sade suallar Vol.2, 4
randomItems = ["abc", "xyz", "11", "abc", 1221]
total = 0

for i in randomItems:
  temp = str(i)
  if len(temp) > 2:
    if temp == temp[::-1]:
      total += 1

print(total)


# Python sade suallar Vol.2, 5
nums = [5, 6, 7, 15, 23, 26, 32]
moreThan20 = []
lessThan20 = []
for num in nums:
  if num % 2 == 0:
    if num > 20:
      moreThan20.append(num)
    else:
      lessThan20.append(num)

print(moreThan20, lessThan20)


# Python sade suallar Vol.2, 6
list1 = [5, 6, 5, 4, 3]
list2 = [5, 7, 3, 9, 4]
commonItems = set()

for i in list1:
  if i in list2:
    commonItems.add(i)

print(list(commonItems))


# Python sade suallar Vol.2, 7
arr = [5, 6, 5, 17, 23, 32, 23]

for i in arr:
  if arr.count(i) == 1:
    print(i, end=" ")

print()
# Python sade suallar Vol.2, 8
complexList = [[15, 25, 32], [4, 3, 5], [7, 8, 10]]
result = 1
for i in complexList:
  result *= max(i)

print(result)
