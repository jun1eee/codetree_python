n = int(input())
words = [input() for _ in range(n)]

groups = {}
for word in words:
    sorted_word = ''.join(sorted(word))

    if sorted_word in groups :
        groups[sorted_word] += 1
    else :
        groups[sorted_word] = 1
print(max(groups.values()))
