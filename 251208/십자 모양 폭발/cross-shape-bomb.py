import sys
input = sys.stdin.readline

N = int(input().strip())

board = [list(map(int, input().split())) for _ in range(N)]

r, c = map(int, input().split())
r -= 1  # 0-index
c -= 1

power = board[r][c]      # 폭발 범위를 결정하는 숫자
dirs = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]  # 자기 자신 + 상하좌우

# 1. 폭발 처리 (십자 모양으로 0으로 만든다)
for dr, dc in dirs:
    for k in range(power):
        nr = r + dr * k
        nc = c + dc * k
        if 0 <= nr < N and 0 <= nc < N:
            board[nr][nc] = 0

# 2. 중력 처리: 각 열마다 숫자를 아래로 떨어뜨리기
for col in range(N):
    temp = []
    # 아래에서 위로 숫자만 모은다
    for row in range(N - 1, -1, -1):
        if board[row][col] != 0:
            temp.append(board[row][col])

    # 다시 아래에서부터 채우고, 나머지는 0
    idx = 0
    for row in range(N - 1, -1, -1):
        if idx < len(temp):
            board[row][col] = temp[idx]
            idx += 1
        else:
            board[row][col] = 0

# 3. 결과 출력
for i in range(N) :
    for j in range(N) :
        print(board[i][j], end=" ")
    print()