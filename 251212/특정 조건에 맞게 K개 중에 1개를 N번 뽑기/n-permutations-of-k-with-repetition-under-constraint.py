K, N = map(int, input().split())

list = []

def back(depth, num) :
    if depth == N :
        for i in list :
            print(i, end=" ")
        print()
        return
    if num == 3 :
        return
    for index in range(1,K+1) :
        list.append(index)
        if len(list) > 1 and list[-1] == list[-2]:
            if num == 2:
                list.pop()
                continue
            back(depth+1,num+1)
        else :
            back(depth+1, 1)
        list.pop()

back(0,1)
