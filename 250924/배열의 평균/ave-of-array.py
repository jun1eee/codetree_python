arr = [list(map(int,input().split())) for _ in range(3)]

for i in range(2) :
    print(f"{sum(arr[i])/4:.1f}", end=" ")
print()
for j in range(4) :
    sumCol = 0;
    for i in range(2) :
        sumCol += arr[i][j]
    print(f"{sumCol/2 :.1f}", end=" ")
print()
sumAll = 0
for i in range(2) :
    for j in range(4) :
        sumAll += arr[i][j]
print(f"{sumAll/8 :.1f}")