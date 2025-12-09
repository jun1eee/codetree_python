n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

for row in range(n):
    blocked = False
    for j in range(k-1, k+m-1):
        if grid[row][j] != 0:
            blocked = True
            break

    if blocked:
        pos = row - 1
        break
    else:
       pos = n - 1

for j in range(k-1, k+m-1):
    grid[pos][j] = 1

for row in grid:
    for r in row :
        print(r, end=" ")
    print()