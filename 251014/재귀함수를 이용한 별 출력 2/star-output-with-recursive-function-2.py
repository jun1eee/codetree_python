n = int(input())

def f(n) :
    if n == 0 :
        return
    print("* "*n, end=" ")
    print()
    f(n-1)
    print("* "*n, end=" ")
    print()
f(n)