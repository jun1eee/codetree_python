n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

max_gold = 0

for row in range(n) :
    for col in range(n) :
        if row + 2 >= n or col + 2 >= n :
            continue
        
        num_of_gold = 0
        for r in range(row, row+3) :
            for c in range(col, col+3) :
                num_of_gold += grid[r][c]
        
        max_gold = max(max_gold, num_of_gold)

print(max_gold)
