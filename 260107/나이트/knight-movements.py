import sys
from collections import deque
n = int(input())
r1, c1, r2, c2 = map(int, input().split())

dirs = [(-1,-2),(-2,-1),(-1,2),(-2,1),(1,-2),(2,-1),(1,2),(2,1)]
visited = [[False for _ in range(n)] for _ in range(n)]
dist = [[0 for _ in range(n)] for _ in range(n)]

q = deque()
ans = sys.maxsize

def bfs() :
    global ans
    while q :
        r, c = q.popleft()
        if r == r2 and c == c2 :
            ans = dist[r2][c2]
            return

        for dr, dc in dirs :
            nr, nc = r + dr, c + dc
            if 0<=nr<n and 0<=nc<n and not visited[nr][nc] :
                visited[nr][nc] = True
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr,nc))

q.append((r1, c1))
visited[r1][c1] = True
bfs()

if ans == sys.maxsize :
    ans = -1
print(ans)
