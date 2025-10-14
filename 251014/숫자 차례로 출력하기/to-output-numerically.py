n = int(input())

def f1(n) :
    if n == 0 :
        return
    f1(n-1)
    print(n, end=" ")

def f2(n) :
    if n == 0 :
        return
    print(n, end=" ")
    f2(n-1)

f1(n)
print()
f2(n)