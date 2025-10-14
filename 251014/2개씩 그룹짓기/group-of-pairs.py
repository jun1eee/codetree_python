n = int(input())
nums = list(map(int, input().split()))

nums.sort()

max_sum = 0

for i in range(n) :
    pair_sum = nums[i] + nums[-i-1]
    if pair_sum > max_sum :
        max_sum = pair_sum
print(max_sum)