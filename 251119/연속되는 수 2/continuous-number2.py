n = int(input())
arr = [int(input()) for _ in range(n)]

max_cnt = 1
cnt = 1
for i in range(1,n) :
    if arr[i] == arr[i-1] :
        cnt += 1
    if max_cnt < cnt :
        max_cnt = cnt

print(max_cnt)
