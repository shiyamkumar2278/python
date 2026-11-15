"""Task 4: Expressions, precedence, rounding and validation."""
import math

BASE_RATE = 30.00
FAT_RATE = 0.40
SNF_RATE = 0.30
BASE_FAT = 3.5
BASE_SNF = 8.5
STEP = 0.1

litres, fat, snf = 12.5, 4.2, 8.7
fat_steps = round((fat - BASE_FAT) / STEP)
snf_steps = round((snf - BASE_SNF) / STEP)
fat_adjustment = fat_steps * FAT_RATE
snf_adjustment = snf_steps * SNF_RATE
rate = BASE_RATE + fat_adjustment + snf_adjustment
payment = round(litres * rate, 2)

print("Fat steps:", fat_steps)
print("SNF steps:", snf_steps)
print("Fat adjustment:", fat_adjustment)
print("SNF adjustment:", snf_adjustment)
print("Rate per litre:", f"{rate:.2f}")
print("Payment:", f"{payment:.2f}")

print("\nOperator precedence")
print("2 ** 3 ** 2 =", 2 ** 3 ** 2)
print("-2 ** 2 =", -2 ** 2)
print("(-2) ** 2 =", (-2) ** 2)

print("\nRounding methods")
print("round(3.7) =", round(3.7))
print("int(3.7) =", int(3.7))
print("floor(3.7) =", math.floor(3.7))
print("round(-3.7) =", round(-3.7))
print("int(-3.7) =", int(-3.7))
print("floor(-3.7) =", math.floor(-3.7))

valid = 2.0 <= fat <= 7.0 and 5.0 <= snf <= 12.0 and litres > 0
print("\nEntry valid:", valid)
print("Unexpected results:", 0.1 + 0.2, -7 // 2, -2 ** 2, round(2.5))
