N = int(input())

def f(N) :
    if N <= 0 :
        return 0    
    return f(N-2) + N

print(f(N))
