# Redesign of Q6: replace repeated plain recursion with memoisation and a loop.
from functools import lru_cache
import time

def original(n):
    if n <= 1: return 1
    return original(n-1) + original(n-2)

@lru_cache(maxsize=None)
def memoised(n):
    if n <= 1: return 1
    return memoised(n-1) + memoised(n-2)

def iterative(n):
    if n <= 1: return 1
    a, b = 1, 1
    for _ in range(2, n+1):
        a, b = b, a+b
    return b

def measure(fn, n):
    start = time.perf_counter()
    value = fn(n)
    return value, time.perf_counter()-start

if __name__ == "__main__":
    for n in (10, 20, 25, 30):
        original_value, t0 = measure(original, n)
        memoised.cache_clear()
        memo_value, t1 = measure(memoised, n)
        loop_value, t2 = measure(iterative, n)
        print(f"n={n}: original={t0:.6f}s, memo={t1:.6f}s, loop={t2:.6f}s")
        print("Results match:", original_value == memo_value == loop_value)
    value, elapsed = measure(iterative, 1000)
    print("n=1000 digits:", len(str(value)), "| loop time:", f"{elapsed:.6f}s")
