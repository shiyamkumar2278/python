"""TASK 6 – Recursion and Its Limits
Problem Context: Counting Ways to Climb Temple Steps
"""

from functools import lru_cache
import sys


def ways_naive(n):
    """Calculate ways using plain recursion."""
    if n <= 1:
        return 1
    return ways_naive(n - 1) + ways_naive(n - 2)


calls = 0

@lru_cache(maxsize=None)
def ways_memo(n):
    """Calculate ways using memoisation."""
    global calls
    calls += 1
    if n <= 1:
        return 1
    return ways_memo(n - 1) + ways_memo(n - 2)


def ways_iterative(n):
    """Calculate ways using an iterative approach."""
    if n <= 1:
        return 1

    previous = 1
    current = 1

    for i in range(2, n + 1):
        previous, current = current, previous + current

    return current


if __name__ == "__main__":
    print("Recursive Implementation")
    for n in range(1, 7):
        print(n, "steps:", ways_naive(n))

    print("\\nRecursive Implementation Using Memoisation")
    print("Ways:", ways_memo(25))
    print("Function calls:", calls)

    print("\\nComplete Code – Naive and Memoised Versions")
    calls = 0
    print("naive:", ways_naive(25), "calls =", calls)

    calls = 0
    ways_memo.cache_clear()
    print("memo :", ways_memo(25), "calls =", calls)

    print("\\nRecursion Limit")
    print(sys.getrecursionlimit())

    print("\\nAlternative Concept – Iterative Approach")
    print(ways_iterative(1000))
