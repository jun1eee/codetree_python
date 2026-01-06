from collections import deque
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

q = deque()
visited = [[False for _ in range(n)] for _ in range(n)]
dirs = [(-1,0),(1,0),(0,-1),(0,1)]

def bfs() : 
    while q : 
        r, c = q.popleft()
        for dr, dc in dirs :
            nr, nc = r + dr, c + dc

            if 0<=nr<n and 0<=nc<n and not grid[nr][nc] and not visited[nr][nc] :
                q.append((nr,nc))
                visited[nr][nc] = True
for _ in range(k) :
    r, c = map(int, input().split())
    q.append((r-1, c-1))
    visited[r-1][c-1] = True

bfs()

ans = 0
for i in range(n) :
    for j in range(n) :
        if visited[i][j] :
            ans += 1
print(ans)