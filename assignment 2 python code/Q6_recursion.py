import sys
from functools import lru_cache
import time

calls = 0
def ways_naive(n):
    global calls
    calls += 1
    if n <= 1:
        return 1
    return ways_naive(n-1) + ways_naive(n-2)

memo_calls = 0
@lru_cache(maxsize=None)
def ways_memo(n):
    global memo_calls
    memo_calls += 1
    if n <= 1:
        return 1
    return ways_memo(n-1) + ways_memo(n-2)

def ways_loop(n):
    if n <= 1: return 1
    a, b = 1, 1
    for _ in range(2, n+1):
        a, b = b, a+b
    return b

if __name__ == "__main__":
    for n in range(1, 7):
        print(f"Ways for {n} steps:", ways_loop(n))
    for n in (10, 20, 25, 30):
        calls = memo_calls = 0
        ways_memo.cache_clear()
        start = time.perf_counter(); x = ways_naive(n); t1 = time.perf_counter()-start
        start = time.perf_counter(); y = ways_memo(n); t2 = time.perf_counter()-start
        print(f"n={n}, result={x}, naive calls={calls}, memo calls={memo_calls}, times={t1:.6f}/{t2:.6f}s")
        assert x == y
    print("Recursion limit:", sys.getrecursionlimit())
    try:
        ways_memo(1000)
    except RecursionError as e:
        print("RecursionError:", e)
    print("Loop handles n=1000; digits:", len(str(ways_loop(1000))))
