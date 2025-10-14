A = input()

def find(A) :
    return len(set(A)) >= 2

print("Yes" if find(A) else "No")

