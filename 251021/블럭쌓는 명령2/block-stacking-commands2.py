n, k = map(int, input().split())
arr = [0] * (n+1)

for _ in range(k) :
    l, r = map(int, input().split())
    for i in range(l,r+1) :
        arr[i] += 1

print(max(arr))