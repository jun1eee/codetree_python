from collections import deque

n, k, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
q = deque()

dirs = [(-1,0),(1,0),(0,-1),(0,1)]
ans = 0

stone_pos = []
for i in range(n) :
    for j in range(n) :
        if arr[i][j] == 1 :
            stone_pos.append((i,j))

selected_stones = []

start_pos = []

def initialize_visited() :
    for i in range(n) :
        for j in range(n) :
            visited[i][j] = False
def bfs() : 
    while q :
        x, y = q.popleft()
        for dx, dy in dirs :
            nx, ny = x + dx, y + dy
            if 0<=nx<n and 0<=ny<n and not arr[nx][ny] and not visited[nx][ny] :
                q.append((nx, ny))
                visited[nx][ny] = True

def calc() :
    for x, y in selected_stones :
        arr[x][y] = 0

    initialize_visited()

    for x, y in start_pos :
        q.append((x,y))
        visited[x][y] = True
    
    bfs()

    for x, y in selected_stones :
        arr[x][y] = 1
    
    cnt = 0
    for i in range(n) :
        for j in range(n) :
            if visited[i][j] :
                cnt += 1
    return cnt

def find_max(idx, cnt) :
    global ans

    if idx == len(stone_pos) :
        if cnt == m :
            ans = max(ans, calc())
        return

    selected_stones.append(stone_pos[idx])
    find_max(idx+1, cnt+1)
    selected_stones.pop()
    find_max(idx+1, cnt)

for _ in range(k) :
    r, c = map(int, input().split())
    start_pos.append((r-1,c-1))
find_max(0,0)
print(ans)    
