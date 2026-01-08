n = int(input())
lines = []
for _ in range(n):
    l, r = map(int, input().split())
    lines.append((l, r))

lines.sort(key=lambda x: (x[1], x[0]))

count = 0
last_end = -float('inf')

for start, end in lines:
    if start > last_end:
        count += 1
        last_end = end

print(count)