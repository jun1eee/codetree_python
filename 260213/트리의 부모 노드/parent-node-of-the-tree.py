import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

parent = [0] * (n+1)
visited = [False] * (n+1)

q = deque([1])
visited[1] = True

while q:
    cur = q.popleft()
    for nxt in graph[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            parent[nxt] = cur
            q.append(nxt)

for i in range(2,n+1):
    print(parent[i])
