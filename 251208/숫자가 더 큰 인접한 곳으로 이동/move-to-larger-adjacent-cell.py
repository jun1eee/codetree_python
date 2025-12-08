n, r, c = map(int, input().split())
r -= 1
c -= 1
grid = [list(map(int, input().split())) for _ in range(n)];
dirs = [(-1,0),(1,0),(0,-1),(0,1)]
path = []
max_value = grid[r][c]
while True :

    path.append(grid[r][c])
    check = False
    for dr, dc in dirs :
        nr = r + dr
        nc = c + dc
        if 0<=nr<n and 0<=nc<n and grid[nr][nc] > max_value :
            r = nr 
            c = nc
            max_value = grid[nr][nc]
            check = True
            break
        
    if not check :
        break

for i in path :
    print(i, end=" ")


