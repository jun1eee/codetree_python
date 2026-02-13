import sys
input = sys.stdin.readline
n = int(input())

tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v, d = map(int,input().split())
    tree[u].append((v,d))
    tree[v].append((u,d))

def dfs(start, distance):
    for next, next_d in tree[start]:
        if visited[next] == -1:
            visited[next] = distance + next_d
            dfs(next, distance + next_d)

visited = [-1] * (n+1)
visited[1] = 0
dfs(1,0)

last_node = visited.index(max(visited))
visited = [-1] * (n+1)
visited[last_node] = 0
dfs(last_node, 0)

print(max(visited))