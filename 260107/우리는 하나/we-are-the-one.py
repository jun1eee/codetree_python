from collections import deque
n, k, u, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
dirs = [(-1,0),(1,0),(0,-1),(0,1)]

q = deque()

def initialize_visit() :
    for i in range(n) :
        for j in range(n) :
            visited[i][j] = False

def bfs() :
    while q :
        r, c = q.popleft()
        for dr, dc in dirs :
            nr, nc = r + dr, c + dc
            if 0<=nr<n and 0<=nc<n and u<=abs(grid[nr][nc]-grid[r][c])<=d and not visited[nr][nc] :
                visited[nr][nc] = True
                q.append((nr,nc))

def count_visited() :
    cnt = 0
    for i in range(n) :
        for j in range(n) :
            if visited[i][j] :
                cnt += 1
    return cnt

choose = []
max_cnt = 0

def back(idx) :
    global max_cnt
    if len(choose) == k :
        initialize_visit()
        q.clear()

        for r,c in choose :
            visited[r][c] = True
            q.append((r,c))
        
        bfs()

        cnt = count_visited()
        max_cnt = max(max_cnt, cnt)
        return
    
    for i in range(idx, n*n) :
        r = i // n
        c = i % n
        choose.append((r,c))
        back(i+1)
        choose.pop()
back(0)
print(max_cnt)
        
