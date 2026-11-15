"""Task 2: Explore values, types, operators and float precision."""
from decimal import Decimal

print("1. DATA TYPES")
for value in (10, 10.0, "10", True, [10, 8.5]):
    print(repr(value), "->", type(value))

print("\n2. DIVISION OPERATORS")
print("7 / 2 =", 7 / 2)
print("7 // 2 =", 7 // 2)
print("7 % 2 =", 7 % 2)
print("-7 // 2 =", -7 // 2)

print("\n3. FLOAT PRECISION")
print("0.1 + 0.2 =", 0.1 + 0.2)
print("0.1 + 0.2 == 0.3:", 0.1 + 0.2 == 0.3)
print("Decimal addition =", Decimal("0.1") + Decimal("0.2"))

payments = ["33.40"] * 1000 + ["0.10"] * 3
float_total = sum(float(x) for x in payments)
decimal_total = sum((Decimal(x) for x in payments), Decimal("0.00"))
print("\n4. TOTAL COMPARISON")
print("Float total:", float_total)
print("Decimal total:", decimal_total)

# Alternative: integer-paise calculation
total_paise = sum(int(Decimal(x) * 100) for x in payments)
print("Integer paise:", total_paise)
print("Integer rupees:", Decimal(total_paise) / 100)
