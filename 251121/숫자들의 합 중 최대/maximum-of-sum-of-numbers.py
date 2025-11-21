X, Y = map(int, input().split())

max_sum = 0
for i in range(X, Y+1) :
    sum = 0
    arr = list(str[i])
    for a in arr :
        sum += int(a)
    max_sum = max(max_sum, sum)
print(max_sum)