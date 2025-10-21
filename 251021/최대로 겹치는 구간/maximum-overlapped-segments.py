n = int(input())
events = []  # (x, delta)  start:+1, end:-1

for _ in range(n):
    x1, x2 = map(int, input().split())
    # 닫힌 구간 [x1, x2]이지만 '끝점만 접촉'은 겹침 아님 => end를 먼저 처리
    events.append((x1, +1))   # 시작
    events.append((x2, -1))   # 끝

# 같은 x에서는 end(-1)를 start(+1)보다 먼저 처리
events.sort(key=lambda e: (e[0], 0 if e[1] == -1 else 1))

curr = 0
ans = 0
for _, d in events:
    curr += d
    if curr > ans:
        ans = curr

print(ans)
