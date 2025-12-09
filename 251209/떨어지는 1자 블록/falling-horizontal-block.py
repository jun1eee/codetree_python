n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

for row in range(n-1,-1,-1) :
    check = False
    for j in range(k-1,k+m-1) :
        if grid[row][j] != 0 :
            check = True
            break
    if not check : 
        for j in range(k-1,k+m-1) :
            grid[row][j] = 1
        break
        
for row in grid :
    for r in row :
        print(r, end=" ")
    print()
    