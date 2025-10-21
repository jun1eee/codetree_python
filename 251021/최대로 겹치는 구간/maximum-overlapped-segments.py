n = int(input().strip())
events = []                 # (x, type)  type: +1 = 시작, -1 = 끝

for _ in range(n):
    x1, x2 = map(int, input().split())
    # 구간 [x1, x2] (닫힌 구간) 가정
    events.append((x1, +1))
    events.append((x2, -1))

# 같은 좌표일 때 시작을 끝보다 먼저 처리해야 닫힌 구간 겹침이 반영됨
events.sort(key=lambda e: (e[0], 0 if e[1] == +1 else 1))

curr = 0
ans = 0
for _, t in events:
    curr += t
    if curr > ans:
        ans = curr

print(ans)
