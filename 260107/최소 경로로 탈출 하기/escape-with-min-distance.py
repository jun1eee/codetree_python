import sys
from collections import deque
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dirs = [(-1,0),(1,0),(0,-1),(0,1)]

q = deque()
visited = [[False for _ in range(m)] for _ in range(n)]
dist = [[0 for _ in range(m)] for _ in range(n)]

ans = sys.maxsize

def bfs() :
    global ans
    while q :
        r, c = q.popleft()
        for dr, dc in dirs :
            nr, nc = r + dr, c + dc
            if 0<=nr<n and 0<=nc<m and a[nr][nc] and not visited[nr][nc] :
                visited[nr][nc] = True
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr,nc))
    if visited[n-1][m-1] :
        ans = dist[n-1][m-1]

q.append((0,0))
bfs()
if ans == sys.maxsize :
    ans = -1

print(ans)
            


