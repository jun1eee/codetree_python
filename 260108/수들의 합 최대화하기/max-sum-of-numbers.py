n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

choose = []
ans = 0
visited = [False] * n 
def calc() :
    hab = 0
    for r,c in choose:
        hab += grid[r][c]
    return hab 

def back(num) :
    global ans
    if num == n :
        ans = max(ans, calc())
    
    for i in range(n) :
        if visited[i] :
            continue
        visited[i] = True
        choose.append((i,num))
        back(num+1)
        choose.pop()
        visited[i] = False

back(0)
print(ans)