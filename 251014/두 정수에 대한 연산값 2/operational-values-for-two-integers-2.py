a, b = map(int, input().split())

def cal(a, b) :
    if a < b :
        a += 10
        b *= 2
    else :
        b += 10
        a *= 2
    return a, b

a, b = cal(a, b)
print(a,b)