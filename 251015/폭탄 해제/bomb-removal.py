class Solve :
    def __init__(self, code, color, second) :
        self.code = code
        self.color = color
        self.second = second
unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)
s = Solve(unlock_code, wire_color, seconds)
print("code : "+ s.code)
print("color : "+ s.color)
print(f"second : {s.second}")