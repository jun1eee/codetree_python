n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

# 총 이동 시간 (둘이 같다고 했으므로 하나만 써도 됨)
T = sum(t)

posA = 0
posB = 0

idxA = 0
idxB = 0
remA = t[0]       # 현재 구간에서 A가 앞으로 더 이동해야 할 초
remB = t2[0]      # 현재 구간에서 B가 앞으로 더 이동해야 할 초

answer = -1

for sec in range(1, T + 1):
    # A 이동
    if d[idxA] == 'L':
        posA -= 1
    else:  # 'R'
        posA += 1
    remA -= 1
    if remA == 0 and idxA + 1 < n:
        idxA += 1
        remA = t[idxA]

    # B 이동
    if d2[idxB] == 'L':
        posB -= 1
    else:  # 'R'
        posB += 1
    remB -= 1
    if remB == 0 and idxB + 1 < m:
        idxB += 1
        remB = t2[idxB]

    # 처음 만나는 시각 체크
    if posA == posB:
        answer = sec
        break

print(answer)
