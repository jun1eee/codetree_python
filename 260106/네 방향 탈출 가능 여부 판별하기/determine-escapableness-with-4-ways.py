from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

visited = [[False for _ in range(m)] for _ in range(n)]
dirs = [(-1,0),(1,0),(0,-1),(0,1)]

q = deque()

def bfs() :
    while q :
        r, c = q.popleft()
        
        for dr, dc in dirs : 
            nr, nc = r + dr, c + dc

            if 0<=nr<n and 0<=nc<m and a[nr][nc] and not visited[nr][nc] :
                q.append((nr, nc))
                visited[nr][nc] = True
q.append((0,0))
visited[0][0] = True

bfs()

answer = 1 if visited[n-1][m-1] else 0 
print(answer)
