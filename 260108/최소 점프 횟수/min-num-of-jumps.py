import sys
n = int(input())
num = list(map(int, input().split()))

ans = sys.maxsize
cur_ans = 0

def back(cnt):
    global ans, cur_ans
    if cnt >= n-1 :
        ans = min(ans, cur_ans)
        return
    
    for i in range(1, num[cnt]+1):
        cur_ans += 1
        back(cnt+i)
        cur_ans -= 1
back(0)

print(ans) if ans != sys.maxsize else print(-1)