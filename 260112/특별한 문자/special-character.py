str = input()

dict = {}

for s in str :

    if s in dict :
        dict[s] += 1
    else :
        dict[s] = 1

check = False
for s in str :
    if dict[s] == 1 :
        print(s)
        check = True
        break

if not check:
    print("None")
