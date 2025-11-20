n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 0, 0         
dir = 0              
arr[x][y] = 1        


for num in range(2, n * m + 1):
    nx, ny = x + dx[dir], y + dy[dir]

    if not (0 <= nx < n and 0 <= ny < m) or arr[nx][ny] != 0:
        dir = (dir + 1) % 4
        nx, ny = x + dx[dir], y + dy[dir]

    arr[nx][ny] = num
    x, y = nx, ny


for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print()
