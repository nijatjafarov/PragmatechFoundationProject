# Link -> https://www.hackerrank.com/challenges/list-comprehensions/problem

x = int(input())
y = int(input())
z = int(input())
n = int(input())
    
combs = []
    
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i + j + k != n:
                combs.append([i, j, k])
                    
print(combs)


"""
Daha optimal varianti. Men yazmamisam, oyrenmek ucun yapisdirdim

x, y, z, n = int(input()), int(input()), int(input()), int(input())
print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])

"""