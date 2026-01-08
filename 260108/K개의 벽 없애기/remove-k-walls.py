from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
r1, c1, r2, c2 = r1-1, c1-1, r2-1, c2-1

dirs = [(-1,0),(1,0),(0,-1),(0,1)]
walls = []

def bfs() :
    q = deque()
    visit = [[False] * n for _ in range(n)]
    dist = [[0] * n for _ in range(n)]
    q.append((r1, c1))
    visit[r1][c1] = True

    while q :
        r, c = q.popleft()
        
        if r == r2 and c == c2 :
            return dist[r2][c2]

        for dr, dc in dirs :
            nr, nc = r + dr, c + dc
            if 0<=nr<n and 0<=nc<n and not grid[nr][nc] and not visit[nr][nc] :
                visit[nr][nc] = True
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr,nc))
    return -1

for i in range(n) :
    for j in range(n) :
        if grid[i][j] == 1 :
            walls.append((i,j))

ans = -1
choose_walls = []
def back(idx, cnt) :
    global ans
    if idx == len(walls) :
        if cnt == k :
            for r, c in choose_walls :
                grid[r][c] = 0
            
            result = bfs()
            
            if result != -1 :
                if ans == -1 or result < ans :
                    ans = result
            for r, c in choose_walls :
                grid[r][c] = 1
        return
    
    choose_walls.append(walls[idx])
    back(idx+1, cnt+1)
    choose_walls.pop()
    back(idx+1, cnt)

back(0,0)
print(ans)