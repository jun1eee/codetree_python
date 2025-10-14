N = int(input())

sum = 0
def f(N) :
    global sum
    if N == 0 :
        return sum
    sum += N
    return f(N-1)

print(f(N))