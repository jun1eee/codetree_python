n = int(input())
visited =[False] * (n+1)
ans = []
def back(num) :
    if num == n + 1 :
        for a in ans :
            print(a, end=" ")
        print()
    
    for i in range(1, n+1) :
        if visited[i] :
            continue
        visited[i] = True
        ans.append(i)
        back(num+1)
        ans.pop()
        visited[i] = False
back(1)
