n = int(input())
arr = input().split()
string = "".join(arr)

for i in range(0,len(string),5) :
    print(string[i:i+5])
    
