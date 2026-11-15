"""Task 10: Compare float and Decimal totals and execution time."""
import time
from decimal import Decimal

def float_total(n):
    total = 0.0
    for _ in range(n):
        total += 0.1
    return total

def decimal_total(n):
    total = Decimal("0.00")
    for _ in range(n):
        total += Decimal("0.10")
    return total

for n in (300, 6000, 150000):
    start = time.perf_counter()
    f_total = float_total(n)
    f_time = time.perf_counter() - start

    start = time.perf_counter()
    d_total = decimal_total(n)
    d_time = time.perf_counter() - start

    print(f"\nPayments: {n}")
    print("Float total:", f_total)
    print("Decimal total:", d_total)
    print(f"Float time: {f_time:.6f} seconds")
    print(f"Decimal time: {d_time:.6f} seconds")
    print("Float error:", abs(Decimal(str(f_total)) - d_total))
