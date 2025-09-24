s = input()
arr = list(s)
for i in range(1,len(arr)) :
    if arr[i] == arr[1] :
        arr[i] = arr[0]
print("".join(arr))