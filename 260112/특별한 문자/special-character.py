str = input()

dict = {}

for s in str :

    if s in dict :
        dict[s] += 1
    else :
        dict[s] = 1

for s in str :
    if dict[s] == 1 :
        print(s)
        break
