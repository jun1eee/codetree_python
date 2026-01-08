n, m = map(int, input().split())
A = list(map(int, input().split()))

ans = 0

def back(idx, num, curr_val) :
    global ans

    if num == m :
        ans = max(ans, curr_val)
        return
    
    if idx >= n or n - idx < m - num :
        return
    
    back(idx+1, num, curr_val)
    back(idx+1, num+1, curr_val ^ A[idx])
back(0,0,0)
print(ans)