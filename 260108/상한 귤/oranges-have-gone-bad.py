from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dirs = [(-1,0),(1,0),(0,-1),(0,1)]

dist = [[float('inf')] * n for _ in range(n)]
rotten = []
for i in range(n) :
    for j in range(n) :
        if grid[i][j] == 0 :
            dist[i][j] = -1
        elif grid[i][j] == 2 :
            rotten.append((i,j))
            dist[i][j] = 0

def bfs(sr, sc) :
    q = deque()
    visited = [[False] * n for _ in range(n)]
    q.append((sr, sc, 0)) 
    visited[sr][sc] = True

    while q :
        r, c, distance = q.popleft()
        for dr, dc in dirs :
            nr, nc = r + dr, c + dc
            if 0<=nr<n and 0<=nc<n and grid[nr][nc]==1 and not visited[nr][nc] :
                if dist[nr][nc] > distance + 1 :
                    dist[nr][nc] = distance + 1
                visited[nr][nc] = True
                q.append((nr, nc, dist[nr][nc]))

for rr, cc in rotten :
    bfs(rr, cc)

for i in range(n) :
    for j in range(n) :
        if dist[i][j] == float('inf') :
            dist[i][j] = -2

for i in range(n) :
    for j in range(n) :
        print(dist[i][j], end=" ")
    print()
    