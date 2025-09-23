arr = list(map(int, input().split()))
arr3 = arr[2::3]
avg3 = sum(arr3)/len(arr3)
print(f"{sum(arr[1::2])} {avg3:.1f}")