n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

ans = float('inf')
choose = []

def cal_dist() :
    global choose
    max_dist = -1
    for i in range(len(choose)) :
        for j in range(len(choose)) :
            distance = (choose[i][0]-choose[j][0])**2 + (choose[i][1]-choose[j][1])**2
            max_dist = max(max_dist, distance)
    return max_dist

def back(idx, num) :
    global ans
    if num == 2 :
        ans = min(ans, cal_dist())
        return
    if idx == n :
        return
    choose.append(points[idx])
    back(idx+1, num+1)
    choose.pop()
    back(idx+1, num)

back(0,0)
print(ans)