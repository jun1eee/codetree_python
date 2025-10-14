a, b = map(int, input().split())

def cal(a, b) :
    if a > b :
        a = a + 25
        b = 2 * b
    else :
        a = 2 * a
        b = b + 25
    return a, b

a, b = cal(a, b)
print(a, b)