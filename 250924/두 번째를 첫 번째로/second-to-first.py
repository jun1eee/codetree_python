s = input()
arr = list(s)
a = arr[1]
for i in range(1,len(arr)) :
    if arr[i] == a :
        arr[i] = arr[0]
print("".join(arr))