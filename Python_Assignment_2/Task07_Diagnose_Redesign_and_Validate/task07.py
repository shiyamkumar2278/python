"""TASK 7 – Diagnose, Redesign and Validate
Selected Program: Temple Step Counter
"""

import time


def ways_naive(n):
    if n <= 1:
        return 1
    return ways_naive(n - 1) + ways_naive(n - 2)


def ways_iterative(n):
    """Calculate the number of ways using dynamic programming."""
    if n < 0:
        raise ValueError("Number of steps cannot be negative")

    if n <= 1:
        return 1

    previous = 1
    current = 1

    for i in range(2, n + 1):
        next_value = previous + current
        previous = current
        current = next_value

    return current


def count_naive_calls(n):
    calls = 0

    def calculate(value):
        nonlocal calls
        calls += 1
        if value <= 1:
            return 1
        return calculate(value - 1) + calculate(value - 2)

    result = calculate(n)
    return result, calls


def validate_redesign():
    print("Revised Python Program")
    for n in range(1, 7):
        print(f"Steps: {n}, Ways: {ways_iterative(n)}")

    print("Ways for 1000 steps:", ways_iterative(1000))

    print("\\nFunction Call Comparison")
    test_values = [10, 20, 25, 30]

    for n in test_values:
        result, calls = count_naive_calls(n)
        loop_iterations = max(0, n - 1)
        print(
            f"{n} steps | Recursive calls: {calls:,} | "
            f"Iterative loop iterations: {loop_iterations} | Result: {result}"
        )

    print("\\nValidation Tests")
    expected_values = {
        0: 1,
        1: 1,
        2: 2,
        3: 3,
        4: 5,
        5: 8,
        6: 13
    }

    for n, expected in expected_values.items():
        actual = ways_iterative(n)
        status = "PASS" if actual == expected else "FAIL"
        print(f"n={n}: expected={expected}, actual={actual} -> {status}")

    print("\\nExperimental Timing (three runs)")
    for n in test_values:
        original_times = []
        revised_times = []

        for _ in range(3):
            start = time.perf_counter()
            original_result = ways_naive(n)
            original_times.append(time.perf_counter() - start)

            start = time.perf_counter()
            revised_result = ways_iterative(n)
            revised_times.append(time.perf_counter() - start)

        print(
            f"{n} steps | Original average: {sum(original_times) / 3:.8f}s | "
            f"Revised average: {sum(revised_times) / 3:.8f}s | "
            f"Same result: {original_result == revised_result}"
        )

    print("\\nValidation for 1000 Steps")
    result = ways_iterative(1000)
    print("Number of ways for 1000 steps:")
    print(result)


if __name__ == "__main__":
    validate_redesign()
