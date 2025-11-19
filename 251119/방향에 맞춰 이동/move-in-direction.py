x, y = 0, 0
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1] # 동서남북

n = int(input())
for _ in range(n) :
    dir, dist = input().split()
    dist = int(dist)
    if dir == 'E' :
        x += dx[0] * dist
        y += dy[0] * dist 
    elif dir == 'W' :
        x += dx[1] * dist
        y += dy[1] * dist 
    elif dir == 'S' :
        x += dx[2] * dist
        y += dy[2] * dist
    else :
        x += dx[3] * dist
        y += dy[3] * dist

print(x, y)
