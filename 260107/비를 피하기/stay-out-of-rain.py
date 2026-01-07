from collections import deque

n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dirs = [(-1,0),(1,0),(0,-1),(0,1)]
distance = [[0] * n for _ in range(n)]
people = []
place = []

for i in range(n) :
    for j in range(n) :
        if grid[i][j] == 2 :
            people.append((i,j))
        elif grid[i][j] == 3 :
            place.append((i,j))

def bfs() :
    while q :
        rr, cc, dist = q.popleft()
        if grid[rr][cc] == 3 :
            return dist
        for dr, dc in dirs :
            nr, nc = rr + dr, cc + dc
            if 0<=nr<n and 0<=nc<n and grid[nr][nc] != 1 and not visited[nr][nc] :
                visited[nr][nc] = True
                q.append((nr,nc, dist + 1))
    return -1


while people :
    r, c = people.pop()
    q = deque()
    visited = [[False] * n for _ in range(n)]
    q.append((r,c,0))
    visited[r][c] = True
    distance[r][c] = bfs()

for i in range(n) :
    for j in range(n) :
        print(distance[i][j], end=" ")
    print()

# from collections import deque

# n, h, m = map(int, input().split())
# grid = [list(map(int, input().split())) for _ in range(n)]

# dirs = [(-1,0), (1,0), (0,-1), (0,1)]
# distance = [[0] * n for _ in range(n)]

# def bfs(sr, sc):
#     visited = [[False] * n for _ in range(n)]
#     q = deque([(sr, sc, 0)])
#     visited[sr][sc] = True
    
#     while q:
#         r, c, dist = q.popleft()
        
#         # 대피소 도착!
#         if grid[r][c] == 3:
#             return dist
        
#         for dr, dc in dirs:
#             nr, nc = r + dr, c + dc
#             if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] != 1 and not visited[nr][nc]:
#                 visited[nr][nc] = True
#                 q.append((nr, nc, dist + 1))
    
#     return -1  # 대피소에 갈 수 없음

# # 모든 사람(2)에 대해 BFS
# for i in range(n):
#     for j in range(n):
#         if grid[i][j] == 2:
#             distance[i][j] = bfs(i, j)

# # 출력
# for i in range(n):
#     for j in range(n):
#         print(distance[i][j], end=" ")
#     print()