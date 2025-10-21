class Student :
    def __init__(self, height, weight, num) :
        self.height, self.weight, self.num = height, weight, num

n = int(input())
students = []
for i in range(n) :
    h, w = map(int, input().split())
    students.append(Student(h,w,i+1))
students.sort(key = lambda x : (x.height, -x.weight))

for s in students :
    print(s.height, s.weight, s.num)