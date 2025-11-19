N, M, K = map(int, input().split())

arr = [0] * (N+1)

ans = -1
for _ in range(M) :
    tmp = int(input())
    arr[tmp] += 1
    if arr[tmp] >= K :
        ans = tmp
        break
print(ans)