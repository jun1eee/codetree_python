n, k = map(int, input().split())
arr = list(map(int, input().split()))

max_sum = 0
for i in range(0, n-k+1) :
    sum = 0
    for j in range(0,k) :
        sum += arr[i+j]
    max_sum = max(max_sum, sum)
print(max_sum)
