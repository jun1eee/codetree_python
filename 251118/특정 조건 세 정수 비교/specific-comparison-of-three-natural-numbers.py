a, b, c = map(int, input().split())

min = min(a, b, c)

if (min==a):
    a1 = 1
else:
    a1=0

if (a==b & b==c & c==a):
    a2 = 1
else:
    a2 = 0

print(f"{a1} {a2}")