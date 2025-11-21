n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

min_nul = 0
for i in range(n) :
    nul = 0
    min_x = 0
    min_y = 0
    max_x = 0
    max_y = 0
    for j in range(n) :
        if i==j : 
            continue
        min_x = min(min_x,x[j])
        min_y = min(min_y,y[j])
        max_x = max(max_x,x[j])
        max_y = max(max_y,y[j])
    nul = (max_x - min_x) * (max_y - min_y)
    min_nul = min(min_nul, nul)
print(min_nul)
