class Data :
    def __init__(self, date, day, weather) :
        self.date = date
        self.day = day
        self.weather = weather

rain_days = []
n = int(input())

for _ in range(n) :
    date, day, weather = input().split()
    if weather == "Rain" :
        rain_days.append(Data(date,day,weather))

earliest_rain = min(rain_days, key=lambda x: x.date)

print(earliest_rain.date, earliest_rain.day, earliest_rain.weather)
        

