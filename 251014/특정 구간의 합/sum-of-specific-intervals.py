n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

ps = [0] * (n+1);
for i in range(1, n+1) :
    ps[i] = ps[i-1] + arr[i-1]

for a1, a2 in queries :
    print(ps[a2] - ps[a1-1])