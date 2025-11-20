n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

drs, dcs = [1, -1, 0, 0], [0, 0, 1, -1]

ans = 0

for r in range(n) :
    for c in range(n) :
        cnt = 0
        for dr, dc in zip(drs, dcs) :
            nr = r + dr
            nc = c + dc

            if nr < 0 or nr >= n or nc < 0 or nc >= n : 
                continue
            elif grid[nr][nc] == 1 :
                cnt += 1
        
        if cnt >= 3 :
            ans += 1
print(ans)
                
    