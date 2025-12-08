n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

for i in range(s1-1,e1) :
    blocks[i] = -1

for i in range(0,e2) :
    if blocks[i] == -1 :
        continue
    if i >= s2-1 :
        blocks[i] = -1
cnt = 0
for i in range(n) :
    if blocks[i] != -1 :
        cnt += 1
print(cnt)
if cnt == 0 :
    return ;
else :
    for i in blocks :
        if i != -1 :
            print(i)