n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

dict = {}
for x, y in points:
    if x in dict :
        dict[x] = min(dict[x], y)
    else :
        dict[x] = y

sum = 0
for v in dict.values() :
    sum += v

print(sum)