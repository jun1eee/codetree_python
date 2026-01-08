n = int(input())
lines = []
for _ in range(n) :
    l, r = map(int, input().split())
    lines.append((l,r))

lines.sort(key=lambda x: (x[1],x[0]))

cnt = 0
last_end = -1

for start, end in lines :
    if start > last_end :
        cnt += 1
        last_end = end
print(cnt)