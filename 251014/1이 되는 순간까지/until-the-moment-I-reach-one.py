N = int(input())

def f(n) :
    if n == 1 :
        return 1
    if n % 2 == 0 :
        return f(n//2) + 1
    else :
        return f(n//3) + 1
print(N)