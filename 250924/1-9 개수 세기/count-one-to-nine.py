N = int(input())
arr = list(map(int, input().split()))

cnt = [0] * 10
for i in arr : 
    cnt[i] += 1
for i in cnt[1:] :
    print(i)