import sys
arr = list(map(int,input().split()))
maxValue = -sys.maxsize
minValue = sys.maxsize

for i in arr :
    if i > 500 :
        if minValue > i :
            minValue = i
    else :
        if maxValue < i :
            maxValue = i
print(maxValue, minValue)