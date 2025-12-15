import sys
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n 
array = []
max_min = -sys.maxsize
def back(num) :
    global max_min
    if num == n :
        max_min = max(max_min, min(array))
    for i in range(n) :
        if visited[i] :
            continue
        
        visited[i] = True
        array.append(grid[num][i])
        back(num+1)
        array.pop()
        visited[i] = False
back(0)
print(max_min)

        
