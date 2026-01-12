n, k = map(int, input().split())
arr = list(map(int, input().split()))

cnt = dict()
ans = 0

for elem in arr :
    diff = k - elem
    
    if diff in cnt :
        ans += cnt[diff]

    if elem in cnt:
        cnt[elem] += 1
    else :
        cnt[elem] = 1

print(ans)