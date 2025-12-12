n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

max_cnt = 0
horses = [1 for _ in range(k)]

def back(depth) :
    global max_cnt
    if depth == n :
        cnt = 0
        for h in horses :
            if h >= m :
                cnt += 1
        if cnt >= max_cnt :
            max_cnt = cnt
        return
    for i in range(k) :
        horses[i] += nums[depth]
        back(depth+1)
        horses[i] -= nums[depth]
back(0)
print(max_cnt)
