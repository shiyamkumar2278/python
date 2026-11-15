"""Task 12: Revised milk payment module with seasonal rates and volume bonus."""
from decimal import Decimal, ROUND_HALF_UP

STANDARD_RATE = Decimal("30.00")
STANDARD_FAT_STEP = Decimal("0.40")
STANDARD_SNF_STEP = Decimal("0.30")

SEASONAL_RATE = Decimal("32.00")       # April, May, June
SEASONAL_FAT_STEP = Decimal("0.45")
SEASONAL_SNF_STEP = Decimal("0.30")

BONUS_RATE = Decimal("0.50")
BONUS_LIMIT = Decimal("500")
STEP = Decimal("0.1")
CENT = Decimal("0.01")

def rounded(value, quantum=Decimal("0.01")):
    return value.quantize(quantum, rounding=ROUND_HALF_UP)

def round_step(value):
    return value.quantize(Decimal("1"), rounding=ROUND_HALF_UP)

def select_rate_card(month):
    if month in (4, 5, 6):
        return {
            "base_rate": SEASONAL_RATE,
            "fat_step_value": SEASONAL_FAT_STEP,
            "snf_step_value": SEASONAL_SNF_STEP
        }
    if 1 <= month <= 12:
        return {
            "base_rate": STANDARD_RATE,
            "fat_step_value": STANDARD_FAT_STEP,
            "snf_step_value": STANDARD_SNF_STEP
        }
    raise ValueError("Month must be from 1 to 12.")

def rate_per_litre(fat, snf, month):
    fat, snf = Decimal(str(fat)), Decimal(str(snf))
    card = select_rate_card(month)
    fat_steps = round_step((fat - Decimal("3.50")) / STEP)
    snf_steps = round_step((snf - Decimal("8.50")) / STEP)
    rate = (card["base_rate"]
            + fat_steps * card["fat_step_value"]
            + snf_steps * card["snf_step_value"])
    return rounded(rate)

def payout(litres, fat, snf, month):
    litres = Decimal(str(litres))
    if litres <= 0:
        raise ValueError("Litres must be greater than zero.")
    if not Decimal("2.0") <= Decimal(str(fat)) <= Decimal("7.0"):
        raise ValueError("Fat must be between 2.0 and 7.0.")
    if not Decimal("5.0") <= Decimal(str(snf)) <= Decimal("12.0"):
        raise ValueError("SNF must be between 5.0 and 12.0.")
    return rounded(litres * rate_per_litre(fat, snf, month))

def bonus(total_litres):
    total_litres = Decimal(str(total_litres))
    if total_litres > BONUS_LIMIT:
        return rounded(total_litres * BONUS_RATE)
    return Decimal("0.00")

def ten_day_total(entries, month):
    """Entries are tuples of (litres, fat, snf)."""
    total_litres = sum((Decimal(str(row[0])) for row in entries), Decimal("0"))
    milk_payment = sum(
        (payout(litres, fat, snf, month) for litres, fat, snf in entries),
        Decimal("0.00")
    )
    bonus_amount = bonus(total_litres)
    return {
        "total_litres": total_litres,
        "milk_payment": rounded(milk_payment),
        "bonus": bonus_amount,
        "final_payment": rounded(milk_payment + bonus_amount)
    }
