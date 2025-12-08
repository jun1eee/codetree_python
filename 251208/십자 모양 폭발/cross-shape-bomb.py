N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
r,c = map(int, input().split())
r -= 1
c -= 1

power = board[r][c]
dirs = [(0,0), (-1,0), (1,0), (0,-1), (0,1)]

for dr, dc in dirs :
    for k in range(power) :
        nr = r + dr*k
        nc = c + dc*k
        if 0<=nr<N and 0<=nc<N :
            board[nr][nc] = 0

new_board = [[0 for _ in range(N)] for _ in range(N)]
for j in range(N) :
    row = N-1
    for i in range(N-1,-1,-1) :
        if board[i][j] :
            new_board[row][j] = board[i][j]
            row -= 1
for i in range(N) :
    for j in range(N) :
        print(new_board[i][j], end=" ")
    print()

        

