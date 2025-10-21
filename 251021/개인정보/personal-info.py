class Person :
    def __init__(self, name, height, weight) :
        self.name = name
        self.height = int(height)
        self.weight = float(weight)
n = 5
people = []
for _ in range(n) :
    n, h, w = input().split()
    people.append(Person(n, h, w))

people_name = sorted(people, key = lambda x : x.name)
people_height = sorted(people, key = lambda x : -x.height)

print("name")
for p in people_name :
    print(f"{p.name} {p.height} {p.weight:.1f}")
print()
print("height")
for p in people_height :
    print(f"{p.name} {p.height} {p.weight:.1f}")

