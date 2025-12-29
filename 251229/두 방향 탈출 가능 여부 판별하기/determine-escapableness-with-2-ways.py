n, m = map(int, input().split())
dirs = [(0,1),(1,0)]
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

def dfs(r, c) :
    for dr, dc in dirs : 
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == 0 and grid[nr][nc] == 1:
            visited[nr][nc] = 1
            dfs(nr, nc)
visited[0][0] = 1
dfs(0,0)
print(visited[n-1][m-1])
