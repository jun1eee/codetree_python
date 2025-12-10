import sys 
n, m, t = map(int, input().split())

# Create n x n grid
a = [list(map(int, input().split())) for _ in range(n)]

# Get m marble positions
marbles = [tuple(map(int, input().split())) for _ in range(m)]
r = [pos[0]-1 for pos in marbles]
c = [pos[1]-1 for pos in marbles]

dirs = [(0,-1),(0,1),(-1,0),(1,0)]

cnt_array = [[0 for _ in range(n)] for _ in range(n)]


for _ in range(t) :
    for index in range(m) :
        rr = r[index]
        cc = c[index]
        cnt_array[rr][cc] = 0
        max_num = -sys.maxsize
        for dr, dc in dirs : 
            nr = rr + dr
            nc = cc + dc
            if 0<=nr<n and 0<=nc<n and a[nr][nc] > max_num :
                r[index] = nr
                c[index] = nc
                max_num = a[nr][nc]
    
    for index in range(m) :
        cnt_array[r[index]][c[index]] += 1

cnt = 0
for i in range(n) :
    for j in range(n) :
        if cnt_array[i][j] == 1 :
            cnt += 1
print(cnt)
    
    
        

