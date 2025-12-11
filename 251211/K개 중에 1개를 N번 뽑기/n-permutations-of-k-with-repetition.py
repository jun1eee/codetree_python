K, N = map(int, input().split())

num = 1
answer = []

def back(num) :
    if num == N :
        for l in answer :
            print(l, end=" ")
        print()
        return
    
    for i in range(1,K+1) : 
        answer.append(i)
        back(num+1)
        answer.pop()
back(0)