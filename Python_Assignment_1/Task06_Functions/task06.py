"""Task 6: Organise payment logic into reusable functions."""
from decimal import Decimal, ROUND_HALF_UP

BASE_RATE = Decimal("30.00")
BASE_FAT = Decimal("3.5")
BASE_SNF = Decimal("8.5")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")
STEP = Decimal("0.1")
CENT = Decimal("0.01")

def money(value):
    return value.quantize(CENT, rounding=ROUND_HALF_UP)

def rate_per_litre(fat, snf):
    fat, snf = Decimal(str(fat)), Decimal(str(snf))
    fat_steps = ((fat - BASE_FAT) / STEP).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    snf_steps = ((snf - BASE_SNF) / STEP).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    return money(BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE)

def payout(litres, fat, snf):
    litres = Decimal(str(litres))
    if litres <= 0:
        raise ValueError("Litres must be greater than zero.")
    if not Decimal("2.0") <= Decimal(str(fat)) <= Decimal("7.0"):
        raise ValueError("Fat must be between 2.0 and 7.0.")
    if not Decimal("5.0") <= Decimal(str(snf)) <= Decimal("12.0"):
        raise ValueError("SNF must be between 5.0 and 12.0.")
    return money(litres * rate_per_litre(fat, snf))

def ten_day_total(entries):
    return money(sum((payout(*entry) for entry in entries), Decimal("0.00")))

if __name__ == "__main__":
    entries = [
        ("10", "3.5", "8.5"),
        ("8.5", "4.2", "8.7"),
        ("12", "3.1", "8.3")
    ]
    for litres, fat, snf in entries:
        rate = rate_per_litre(fat, snf)
        amount = payout(litres, fat, snf)
        print(f"{litres} L | Fat {fat}% | SNF {snf}% | Rate Rs.{rate} | Payment Rs.{amount}")
    print("Ten-day total: Rs.", ten_day_total(entries))
