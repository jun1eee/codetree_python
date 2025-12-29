n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
dirs = [(-1,0),(1,0),(0,-1),(0,1)]
visited = [[False for _ in range(m)] for _ in range(n)]
def dfs(r,c,k) :
    for dr, dc in dirs :
        nr, nc = r + dr, c + dc
        if 0<=nr<n and 0<=nc<m and not visited[nr][nc] and grid[nr][nc] > k :
            visited[nr][nc] = True
            dfs(nr,nc,k)
def get_cnt(k) :
    global cnt
    cnt = 0
    for i in range(n) :
        for j in range(m) :
            visited[i][j] = False
    for i in range(n) :
        for j in range(m) :
            if 0<=nr<n and 0<=nc<m and not visited[nr][nc] and grid[nr][nc] > k :
                visited[nr][nc] = True
                cnt += 1
                dfs(i,j,k)
max_cnt = -1
answer = 0
for num in range(1, 101) :
    get_cnt(num)

    if cnt > max_cnt :
        max_cnt, answer = cnt, num

print(answer,max_cnt)

