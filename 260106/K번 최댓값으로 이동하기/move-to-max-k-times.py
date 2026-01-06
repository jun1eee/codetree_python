import collections

NOT_EXISTS = (-1, -1)

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
curr_cell = (r-1, c-1)

dirs = [(-1,0),(1,0),(0,-1),(0,1)]

q = collections.deque()
visited = [[0 for _ in range(n)] for _ in range(n)]

def bfs():
    x, y = curr_cell
    visited[x][y] = True
    q.append(curr_cell)

    num = grid[x][y]

    while q:
        x, y = q.popleft()

        for dx, dy in dirs :
            nx, ny = x + dx, y + dy

            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and grid[x][y] < num :
                q.append((nx,ny))
                visited[nx][ny] = True

def update(best, new) :
    if best == NOT_EXISTS:
        return True
    
    best_x, best_y = best
    new_x, new_y = new

    return (grid[new_x][new_y], -new_x, -new_y) > (grid[best_x][best_y], -best_x, -best_y)

def move():
    global curr_cell

    for i in range(n) :
        for j in range(n) :
            visited[i][j] = 0
    
    bfs()

    best = NOT_EXISTS
    for i in range(n) :
        for j in range(n) :
            if not visited[i][j] or (i,j) == curr_cell :
                continue
            new = (i, j)
            if update(best, new) :
                best = new
    
    if best = NOT_EXISTS :
        return False
    else :
        curr_cell = best
        return True

for _ in range(k) :
    is_moved = move()
    if not is_moved :
        break

final_x, final_y = curr_cell
print(final_x + 1, final_y + 1)