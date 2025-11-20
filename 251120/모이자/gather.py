import sys
n = int(input())
A = list(map(int, input().split()))

min_sum = sys.maxsize

for i in range(n) :
    sum = 0
    for j in range(n) :
        sum += abs(i-j) * A[j]
    
    min_sum = min(min_sum, sum)

print(min_sum)