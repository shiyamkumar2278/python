from decimal import Decimal, ROUND_HALF_UP

# Original rate card
BASE_RATE = Decimal("30.00")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")

# Seasonal rate card: April to June
SEASONAL_BASE_RATE = Decimal("32.00")
SEASONAL_FAT_STEP_VALUE = Decimal("0.45")

SNF_SEASONAL_STEP_VALUE = Decimal("0.30")

BONUS_LIMIT = Decimal("500")
BONUS_PER_LITRE = Decimal("0.50")


def nearest_steps(value, standard):
    """Calculate the nearest 0.1% steps."""
    difference = (Decimal(str(value)) - Decimal(str(standard))) / Decimal("0.1")
    return int(difference.quantize(Decimal("1"), rounding=ROUND_HALF_UP))


def rate_per_litre(fat, snf, season="normal"):
    """Calculate the milk rate per litre."""

    fat = Decimal(str(fat))
    snf = Decimal(str(snf))

    if season.lower() in ["apr_jun", "april-june"]:
        base = SEASONAL_BASE_RATE
        fat_value = SEASONAL_FAT_STEP_VALUE
        snf_value = SNF_SEASONAL_STEP_VALUE
    else:
        base = BASE_RATE
        fat_value = FAT_STEP_VALUE
        snf_value = SNF_STEP_VALUE

    fat_steps = nearest_steps(fat, Decimal("3.5"))
    snf_steps = nearest_steps(snf, Decimal("8.5"))

    rate = base + (fat_steps * fat_value) + (snf_steps * snf_value)

    return rate.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def payout(litres, fat, snf, season="normal"):
    """Calculate payment for a milk entry."""

    litres = Decimal(str(litres))

    if litres < 0:
        raise ValueError("Litres cannot be negative")

    if not Decimal("2.0") <= Decimal(str(fat)) <= Decimal("7.0"):
        raise ValueError("Fat must be between 2.0 and 7.0")

    if Decimal(str(snf)) < 0:
        raise ValueError("SNF cannot be negative")

    rate = rate_per_litre(fat, snf, season)

    amount = litres * rate

    return amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def ten_day_total(payments):
    """Calculate the total payment for ten days."""

    total = sum(payments, Decimal("0.00"))

    return total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def bonus_amount(total_litres):
    """Calculate bonus when total supply exceeds 500 litres."""

    total_litres = Decimal(str(total_litres))

    if total_litres > BONUS_LIMIT:
        bonus = total_litres * BONUS_PER_LITRE
    else:
        bonus = Decimal("0.00")

    return bonus.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


if __name__ == "__main__":

    test_entries = [
        (10, 3.5, 8.5),
        (8.5, 4.2, 8.7),
        (12, 3.1, 8.3)
    ]

    for litres, fat, snf in test_entries:
        rate = rate_per_litre(fat, snf)
        amount = payout(litres, fat, snf)

        print(
            f"{litres:5} L | Fat: {fat} | SNF: {snf} "
            f"| Rate: {rate:.2f} | Payment: {amount:.2f}"
        )