import sys

def has369(x: int) -> bool:
    # x의 자릿수에 3, 6, 9가 하나라도 있으면 True
    while x:
        d = x % 10
        if d in (3, 6, 9):
            return True
        x //= 10
    return False

def is_ok(n: int) -> bool:
    return (n % 3 == 0) or has369(n)

A, B = map(int, sys.stdin.readline().split())
cnt = sum(1 for n in range(A, B + 1) if is_ok(n))
print(cnt)
