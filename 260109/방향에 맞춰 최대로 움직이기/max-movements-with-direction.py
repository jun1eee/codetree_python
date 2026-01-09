n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
move_dir = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r, c = r-1, c-1
dirs = [(0,0),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

ans = 0
curr_ans = []

def back(r,c):
    global ans, curr_ans
    
    ans = max(ans,len(curr_ans))

    for i in range(n) :
        d = move_dir[r][c]
        nr, nc = r + dirs[d][0]*i, c + dirs[d][1]*i

        if 0<=nr<n and 0<=nc<n and num[r][c] < num[nr][nc] :
            curr_ans.append(num[nr][nc])
            back(nr,nc)
            curr_ans.pop()
back(r,c)
print(ans)
    # dr, dc = dirs[move_dir[r][c]]
    # while True :
    #     nr, nc = r + dr, c + dc
    #     if 0<=nr<n and 0<=nc<n and grid[nr][nc]>grid[r][c] :
    #         r, c = nr, nc
    #         cnt += 1
    #         back(num+1)
    # for dr,dc in dirs:
    #     while True :
    #         nr, nc = r + dr, c + dc
    #         if 0<=nr<n and 0<=nc<n and 

