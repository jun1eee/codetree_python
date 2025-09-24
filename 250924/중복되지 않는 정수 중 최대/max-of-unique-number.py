n = int(input())
nums = list(map(int, input().split()))

cnt = [0] * (max(nums)+1)
for i in nums :
    cnt[i] += 1

max_val = -1
for i in range(len(cnt)) :
    if cnt[i] == 1 :
        max_val = i

print(max_val)