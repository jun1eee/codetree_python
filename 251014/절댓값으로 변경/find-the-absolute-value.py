n = int(input())
arr = list(map(int, input().split()))

def abs(arr) :
    for i in range(n) :
        if arr[i] < 0 :
            arr[i] = - arr[i]
abs(arr)
for ele in arr :
    print(ele, end=" ")