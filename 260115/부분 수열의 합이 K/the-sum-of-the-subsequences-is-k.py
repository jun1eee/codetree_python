n, k = map(int, input().split())
arr = list(map(int, input().split()))

prefix_sum = [0] * n
prefix_sum[0] = arr[0]
for i in range(1,n):
    prefix_sum[i] = arr[i] + prefix_sum[i-1]

cnt = 0
for num in prefix_sum:
    if num == k:
        cnt += 1
        
for i in range(0,n-1):
    for j in range(i+1,n):
        if prefix_sum[j] - prefix_sum[i] == k:
            cnt += 1
print(cnt)
