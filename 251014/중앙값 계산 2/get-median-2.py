n = int(input())
arr = list(map(int, input().split()))

for i in range(0, len(arr), 2) :
    arr2 = arr[:i+1]
    arr2.sort()
    print(arr2[i//2], end=" ")