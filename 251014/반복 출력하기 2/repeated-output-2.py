n = int(input())

def printStars(n) :
    if n == 0 :
        return
    print("HelloWorld")
    printStars(n-1)

printStars(n)