import heapq

n,m = map(int, input().split())
k = int(input())

graph = [[] for _ in range(n+1)]
pq = []

dist = [float("inf")] * (n+1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
    graph[y].append((x, z))

dist[k] = 0

# (거리, 정점 번호) 형태로 넣어준다.
heapq.heappush(pq, (0,k))

while pq:
    min_dist, min_index = heapq.heappop(pq)

    # min_dist가 최신 dist[min_index]값과 다르다면 pass
    if min_dist != dist[min_index]:
        continue
    
    for target_index, target_dist in graph[min_index]:
        new_dist = dist[min_index] + target_dist
        if dist[target_index] > new_dist:
            dist[target_index] = new_dist
            heapq.heappush(pq, (new_dist, target_index))

for i in range(1,n+1):
    if dist[i] == float("inf"):
        print(-1)
    else:
        print(dist[i])