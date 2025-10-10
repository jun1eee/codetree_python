a, b = map(int, input().split())
def f(n) :
    check = True
    for i in range(2,n) :
        if n % i == 0 :
            check = False
sum = 0
for i in range(a, b+1) :
    if f(i) :
        sum += i
print(sum)

