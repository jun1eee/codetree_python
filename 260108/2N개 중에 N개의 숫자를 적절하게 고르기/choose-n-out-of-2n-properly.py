n = int(input())
num = list(map(int, input().split()))

total = sum(num)
min_diff = float('inf')

def back(idx, group1, cnt1):
    global min_diff

    if cnt1 == n :
        group2 = total - group1
        diff = abs(group1 - group2)
        min_diff = min(min_diff, diff)
        return
    
    if cnt1 > n or idx == 2*n :
        return
    
    back(idx+1, group1+num[idx], cnt1+1)
    back(idx+1, group1, cnt1)

back(0, 0, 0)
print(min_diff)