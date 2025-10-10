import sys

def has369(x) :
    # x의 자릿수에 3, 6, 9가 하나라도 있으면 True
    while x:
        d = x % 10
        if d in (3, 6, 9):
            return True
        x //= 10
    return False

def is_ok(n) :
    return (n % 3 == 0) or has369(n)

A, B = map(int, input().split())
cnt = 0
for i in range(A, B + 1):
    if is_ok(i):
        cnt += 1
print(cnt)
