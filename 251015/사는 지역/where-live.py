class Info :
    def __init__(self, name, address, region) :
        self.name = name
        self.address = address
        self.region = region

n = int(input())
people = []

for _ in range(n) :
    name, address, city = input().split()
    people.append(Info(name, address, city))

max_person = max(people, key=lambda x: x.name)

print("name", max_person.name)
print("addr", max_person.address)
print("city", max_person.region)