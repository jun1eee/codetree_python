x, y = 0, 0
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1] # 동서남북

n = int(input())
for _ in range(n) :
    dir, dist = input().split()
    dist = int(dist)
    if dir == 'E' :
        move_dir = 0
    elif dir == 'W' :
        move_dir = 1 
    elif dir == 'S' :
        move_dir = 2
    else :
        move_dir = 3
    x += dx[move_dir] * dist
    y += dy[move_dir] * dist

print(x, y)
