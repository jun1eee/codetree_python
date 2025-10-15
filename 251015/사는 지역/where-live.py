n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

class Info :
    def __init__(self, name, address, region) :
        self.name = name
        self.address = address
        self.region = region

person = Info(name[-1], street_address[-1], region[-1])

print("name", person.name)
print("addr", person.address)
print("city", person.region)