import sys
input = sys.stdin.readline

n, m, t = map(int, input().split())

# 격자
a = [list(map(int, input().split())) for _ in range(n)]

# 구슬 초기 위치 (0-index)
marbles = [tuple(map(int, input().split())) for _ in range(m)]
r = [pos[0] - 1 for pos in marbles]
c = [pos[1] - 1 for pos in marbles]

# 상 하 좌 우 (우선순위)
dirs = [(-1,0), (1,0), (0,-1), (0,1)]

for _ in range(t):
    # 1) 모든 구슬 이동 결과를 임시 배열에 저장
    new_r = [0] * m
    new_c = [0] * m

    for i in range(m):
        rr, cc = r[i], c[i]
        max_num = -sys.maxsize
        br, bc = rr, cc

        for dr, dc in dirs:
            nr = rr + dr
            nc = cc + dc
            if 0 <= nr < n and 0 <= nc < n:
                if a[nr][nc] > max_num:
                    max_num = a[nr][nc]
                    br, bc = nr, nc

        new_r[i] = br
        new_c[i] = bc

    # 2) 위치별 구슬 개수 세기
    cnt_array = [[0] * n for _ in range(n)]
    for i in range(m):
        cnt_array[new_r[i]][new_c[i]] += 1

    # 3) 1개만 있는 칸의 구슬만 다시 r, c 에 넣기 (충돌한 구슬 제거)
    nr_list = []
    nc_list = []
    for i in range(m):
        if cnt_array[new_r[i]][new_c[i]] == 1:
            nr_list.append(new_r[i])
            nc_list.append(new_c[i])

    r, c = nr_list, nc_list
    m = len(r)  # 남아 있는 구슬 수 갱신

# T초 후 남아 있는 구슬 수
print(m)
