import random, time, sys

readings = [random.uniform(-60, 60) for _ in range(10000)]

def loop_clean(data):
    valid=[]
    for x in data:
        if -50 <= x <= 50: valid.append(x)
    return valid

def comprehension(data):
    return [x for x in data if -50 <= x <= 50]

def map_filter(data):
    return list(map(lambda x: x, filter(lambda x: -50 <= x <= 50, data)))

valid = comprehension(readings)
fahrenheit = [round(c*9/5+32, 2) for c in valid]
alarms = [(minute, temp) for minute,temp in enumerate(readings) if temp < 2 or temp > 8]
print("Valid count:", len(valid))
print("Celsius first 5:", valid[:5])
print("Fahrenheit first 5:", fahrenheit[:5])
print("Alarm minutes first 10:", alarms[:10])
for fn in (loop_clean, comprehension, map_filter):
    start=time.perf_counter()
    result=fn(readings)
    print(fn.__name__, round(time.perf_counter()-start, 6), "sec; same:", result == valid)
print("List size:", sys.getsizeof(valid))
gen = (x for x in readings if -50 <= x <= 50)
print("Generator object size:", sys.getsizeof(gen))
