import time
import statistics

def build_plus(parts):
    text = ""
    for p in parts:
        text += p + ";"
    return text

def build_join(parts):
    return "".join(p + ";" for p in parts)

def build_fstring(parts):
    return "".join(f"{p};" for p in parts)

def measure(fn, items):
    times, result = [], ""
    for _ in range(3):
        start = time.perf_counter()
        result = fn(items)
        times.append(time.perf_counter() - start)
    return result, statistics.mean(times)

if __name__ == "__main__":
    for n in (1000, 10000, 200000):
        items = [f"Item{i}:Rs{i % 50}" for i in range(n)]
        a, ta = measure(build_plus, items)
        b, tb = measure(build_join, items)
        c, tc = measure(build_fstring, items)
        print(f"\nItems: {n:,} | same output: {a == b == c}")
        print(f"+= {ta:.6f}s | join {tb:.6f}s | f-string {tc:.6f}s")
