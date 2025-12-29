n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
cnt = 0

def dfs(n) :
    global cnt 
    for v in graph[n] :
        if not visited[v] :
            visited[v] = True
            cnt += 1
            dfs(v)

for i in range(m) :
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited[1] = True
dfs(1)
print(cnt)