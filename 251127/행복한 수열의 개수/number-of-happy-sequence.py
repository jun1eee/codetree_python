n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

cnt = 0

for row in range(n) :
    for start in range(n-m+1) :
        check = True
        for i in range(m) :
            if grid[row][start] != grid[row][start + i] :
                check = False
                break
        
    if check == True :
        cnt += 1

for col in range(n) :
    for start in range(n-m+1) :
        check = True
        for j in range(m) :
            if grid[start][col] != grid[start + j][col] :
                check = False
                break
    if check == True :
        cnt += 1
print(cnt)