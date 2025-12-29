n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

people_num = 0
people_nums = []

dirs = [(-1,0),(1,0),(0,-1),(0,1)]
def dfs(r, c) :
    global people_num
    for dr, dc in dirs :
        nr, nc = r + dr, c + dc
        if 0<=nr<n and 0<=nc<n and grid[nr][nc] == 1 and not visited[nr][nc] :
            visited[nr][nc] = True
            people_num += 1
            dfs(nr, nc)

for i in range(n) :
    for j in range(n) :
        if grid[i][j] == 1 and not visited[i][j] :
            visited[i][j] = True
            people_num = 1
            dfs(i,j)
            people_nums.append(people_num)
people_nums.sort()
print(len(people_nums))
for p in people_nums :
    print(p)
