n = int(input())
cnt = 0
answer = []
def is_beautiful() :
    i = 0
    while i < n :
        if answer[i] >= n - i + 1 :
            return False
        for j in range(i, i + answer[i]) :
            if answer[j] != answer[i] : 
                return False
        i += answer[i]
    return True
def back(depth) :
    global cnt
    if depth == n :
        if is_beautiful() :
            cnt += 1
        return
    
    for i in range(1, 5) :
        answer.append(i)
        back(depth + 1)
        answer.pop()
back(0)
print(cnt)