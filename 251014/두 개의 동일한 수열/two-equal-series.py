n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()
check = True
for i in range(n) :
    if A[i] != B[i] :
        check = False
if check == True :
    print("Yes")
else :
    print("No")