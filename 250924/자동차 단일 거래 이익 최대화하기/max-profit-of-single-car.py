n = int(input())
price = list(map(int, input().split()))
profit = 0
for i in range(n-1) :
    maxValue = max(price[i+1:])
    if maxValue > price[i] :
        if profit < maxValue - price[i] :
            profit = maxValue - price[i]
print(profit)