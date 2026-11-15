"""Task 3: Variables, named constants, dynamic typing and assignment."""
from decimal import Decimal

BASE_RATE = Decimal("30.00")
BASE_FAT = Decimal("3.5")
BASE_SNF = Decimal("8.5")
FAT_RATE = Decimal("0.40")
SNF_RATE = Decimal("0.30")
FAT_STEP = Decimal("0.1")
SNF_STEP = Decimal("0.1")
MIN_FAT, MAX_FAT = Decimal("2.0"), Decimal("7.0")
MIN_SNF, MAX_SNF = Decimal("5.0"), Decimal("12.0")
PAYMENT_PERIOD = 10
ROUNDING_DIGITS = 2

farmer_id = "F001"
litres = Decimal("12.5")
fat_percent = Decimal("4.2")
snf_percent = Decimal("8.7")

print("Constants:", BASE_RATE, FAT_RATE, SNF_RATE, PAYMENT_PERIOD)
print("Farmer:", farmer_id, litres, fat_percent, snf_percent)

# Python constants are conventions; reassignment is technically possible.
print("\nDynamic typing demonstration:")
value = 10
print(value, type(value))
value = "Milk"
print(value, type(value))

# Multiple assignment
farmer_id, litres, fat_percent = "F002", Decimal("10.0"), Decimal("3.8")
print("\nMultiple assignment:", farmer_id, litres, fat_percent)

# Swapping
a, b = 30, 40
a, b = b, a
print("After swapping: a =", a, "b =", b)

# Named-constant rate calculation
fat_steps = (fat_percent - BASE_FAT) / FAT_STEP
snf_steps = (snf_percent - BASE_SNF) / SNF_STEP
rate = BASE_RATE + fat_steps * FAT_RATE + snf_steps * SNF_RATE
print("Calculated rate:", rate)
