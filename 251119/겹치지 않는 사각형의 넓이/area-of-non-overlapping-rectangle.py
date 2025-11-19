x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())  # A
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())  # B
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())  # M

# A, B의 원래 넓이
def rect_area(i):
    return (x2[i] - x1[i]) * (y2[i] - y1[i])

# i번째 직사각형과 M(2번)의 겹치는 넓이
def overlap_with_M(i):
    w = min(x2[i], x2[2]) - max(x1[i], x1[2])
    h = min(y2[i], y2[2]) - max(y1[i], y1[2])

    if w > 0 and h > 0:
        return w * h
    return 0

ans = 0
for i in range(2):  # 0: A, 1: B
    ans += rect_area(i) - overlap_with_M(i)

print(ans)
