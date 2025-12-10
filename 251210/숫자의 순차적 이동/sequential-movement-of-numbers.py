import sys
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dirs = [(1,0),(-1,0),(0,-1),(0,1),(1,-1),(-1,-1),(1,1),(-1,1)]

for _ in range(m) :
    for num in range(1, n*n+1) :
        r, c = -1, -1
        for i in range (n) :
            for j in range(n) :
                if grid[i][j] == num :
                    r, c = i, j
                    break
        max_num = -sys.maxsize
        mr, mc = -1, -1
        for dr, dc in dirs :
            nr = r + dr
            nc = c + dc
            if 0<=nr<n and 0<=nc<n and grid[nr][nc]>max_num :
                max_num = grid[nr][nc]
                mr, mc = nr, nc
        grid[mr][mc], grid[r][c] = grid[r][c], grid[mr][mc]

for i in range(n) :
    for j in range(n) :
        print(grid[i][j], end=" ")
    print()