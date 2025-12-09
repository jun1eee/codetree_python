n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

for row in range(n) :
    check = True
    for j in range(k-1,k+m-1) :
        if grid[row][j] != 0 :
            check = False
            break
    if not check : 
        for j in range(k-1,k+m-1) :
            grid[row-1][j] = 1
        break

for row in grid :
    for r in row :
        print(r, end=" ")
    print()
    