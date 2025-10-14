N, M = map(int, input().split())
A = list(map(int, input().split()))

sum = 0
def f() :
    global M, sum
    while M != 1 :
        sum += A[M-1]
        if M % 2 == 1 :
            M -= 1
        else :
            M //= 2

f()
print(sum + A[0])