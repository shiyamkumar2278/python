from collections import defaultdict
import random, time

timetable = {
 "12601": {"name":"Chennai Express","stops":[("Chennai","08:00","08:10"),("Katpadi","10:00","10:05"),("Bengaluru","13:00","13:10")],"days":{"Mon","Wed","Fri"}},
 "12602": {"name":"Coastal Express","stops":[("Chennai","09:00","09:15"),("Villupuram","11:00","11:05"),("Cuddalore","12:00","12:05")],"days":{"Tue","Thu","Sat"}},
 "12603": {"name":"Southern Express","stops":[("Madurai","06:00","06:10"),("Trichy","09:00","09:05"),("Chennai","14:00","14:10")],"days":{"Mon","Tue","Wed"}},
 "12604": {"name":"Hill Express","stops":[("Chennai","07:00","07:10"),("Katpadi","09:00","09:05"),("Coimbatore","12:00","12:10")],"days":{"Sun","Fri"}},
 "12605": {"name":"Delta Express","stops":[("Thanjavur","05:00","05:10"),("Cuddalore","08:00","08:05"),("Chennai","10:00","10:10")],"days":{"Sat","Sun"}}
}
station_index = defaultdict(list)
for train, info in timetable.items():
    for station, arrival, departure in info["stops"]:
        station_index[station].append((train, departure))

def find_trains(station, day):
    matches=[]
    for train, info in timetable.items():
        if day in info["days"]:
            for stop, arrival, departure in info["stops"]:
                if stop == station: matches.append((train, info["name"], departure))
    return sorted(matches, key=lambda x:x[2])

print("Trains at Chennai on Monday:", find_trains("Chennai","Mon"))
print("Third station departure for 12601:", timetable["12601"]["stops"][2][2])
print("Indexed trains at Chennai:", station_index["Chennai"])
