import random, time

def weekly_totals(readings):
    return [sum(readings[i:i+7]) for i in range(0, len(readings), 7)]

def moving_naive(data, window=7):
    return [sum(data[i:i+window])/window for i in range(len(data)-window+1)]

def moving_running(data, window=7):
    if len(data) < window: return []
    total = sum(data[:window])
    result = [total/window]
    for i in range(window, len(data)):
        total += data[i] - data[i-window]
        result.append(total/window)
    return result

if __name__ == "__main__":
    readings = [round(random.uniform(0, 30), 1) for _ in range(365)]
    print("Weekly totals:", weekly_totals(readings))
    print("Wettest week:", max(range(len(weekly_totals(readings))), key=weekly_totals(readings).__getitem__)+1)
    print("Driest week:", min(range(len(weekly_totals(readings))), key=weekly_totals(readings).__getitem__)+1)
    print("7-day averages (first 5):", moving_running(readings)[:5])
    print("Dry days:", [i+1 for i,x in enumerate(readings) if x == 0])
    for n in (365, 36500, 365000):
        data = [random.random()*30 for _ in range(n)]
        for fn in (moving_naive, moving_running):
            t=time.perf_counter(); fn(data); print(n, fn.__name__, round(time.perf_counter()-t, 5), "sec")
