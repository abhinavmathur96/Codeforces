import sys

n,q,c = map(int,raw_input().strip().split())
grid = [[[0 for x in range(101)] for i in range(101)] for j in range(11)]

for i in range(n):
    x,y,z = map(int,raw_input().strip().split())
    grid[z][x][y]+=1

for i in range(c+1):
    for j in range(1,101):
        for k in range(1,101):
            grid[i][j][k] += (grid[i][j-1][k]+grid[i][j][k-1]-grid[i][j-1][k-1])

for i in range(q):
    t,x1,y1,x2,y2 = map(int,raw_input().strip().split())
    ans = 0
    for j in range(c+1):
        temp = (j+t)%(c+1)
        amt = (grid[j][x2][y2]-grid[j][x1-1][y2]-grid[j][x2][y1-1]+grid[j][x1-1][y1-1])
        ans += temp*amt
    print ans
