arr = ['L', 'E', 'B', 'R', 'O', 'S']
a = input()

index = -1
for i, char in enumerate(arr):
    if char == a:
        index = i

if index == -1:
    print("None")
else:
    print(index)
