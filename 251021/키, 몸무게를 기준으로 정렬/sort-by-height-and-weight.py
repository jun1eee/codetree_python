class Person :
    def __init__(self, name, height, weight) :
        self.name = name
        self.height = int(height)
        self.weight = int(weight)
    
n = int(input())
People = []
for _ in range(n) :
    n, h, w = input().split()
    People.append(Person(n, h, w))
People.sort(key = lambda x : (x.height, -x.weight))
for p in People :
    print(p.name, p.height, p.weight)