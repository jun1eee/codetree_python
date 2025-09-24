n = int(input())
arr = list(map(int, input().split()))
min = arr[1] - arr[0]

for i in range(1,n-1) :
    if (min > arr[i+1] - arr[i]) :
        min = arr[i+1] - arr[i]
print(min)