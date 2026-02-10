n = int(input())
arr = list(map(int, input().split()))
dp = [-1]*(n+1)
dp[1] = 0
for i in range(1,n+1):
    if dp[i] == -1:
        continue
    tmp = min(n, i+arr[i-1])
    for j in range(i+1,tmp+1):
        dp[j] = max(dp[j],dp[i]+1)
print(max(dp))

