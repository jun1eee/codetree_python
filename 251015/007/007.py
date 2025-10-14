secret_code, meeting_point, time = input().split()
time = int(time)

class spy :
    def __init__(self, secret_code, meeting_point, time) :
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time

s = spy(secret_code, meeting_point, time)

print(f"secret code : {s.secret_code}")
print(f"meeting point : {s.meeting_point}")
print(f"time : {s.time}")