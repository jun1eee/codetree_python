n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dirs = [(-1,0),(1,0),(0,-1),(0,1)]
visited = [[False for _ in range(n)] for _ in range(n)]
cnt = 0
bomb_cnt = 0
max_cnt = -1 
def dfs(r,c,k) :
    global cnt
    for dr, dc in dirs :
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] == k:
            visited[nr][nc] = True
            cnt += 1
            dfs(nr,nc,k)


for i in range(n) :
    for j in range(n) :
        if not visited[i][j] :
            visited[i][j] = True
            cnt = 1
            dfs(i,j,grid[i][j])
            if cnt >= 4 : 
                bomb_cnt += 1        
            if cnt > max_cnt :
                max_cnt = cnt
print(bomb_cnt, max_cnt)