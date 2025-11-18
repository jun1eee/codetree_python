N = int(input())
for _ in range(N) :
    a, b = map(int, input().split())
    mul = 1
    for i in range(a, b+1) :
        mul *= i
    print(mul)