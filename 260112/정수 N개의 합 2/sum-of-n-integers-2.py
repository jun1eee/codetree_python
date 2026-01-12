n, k = map(int, input().split())
arr = list(map(int, input().split()))

prefix_sum = [0] * n
prefix_sum[0] = arr[0]

for i in range(1,n):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]

max_num = prefix_sum[k-1]
for i in range(k, n):
    max_num = max(max_num, prefix_sum[i]-prefix_sum[i-k])
print(max_num)
