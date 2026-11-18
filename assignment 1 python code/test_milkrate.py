from milkrate import (
    rate_per_litre,
    payout,
    bonus_amount,
    ten_day_total
)

from decimal import Decimal


# Original rate tests
assert rate_per_litre(3.5, 8.5) == Decimal("30.00")
assert rate_per_litre(4.2, 8.7) == Decimal("33.40")
assert rate_per_litre(3.1, 8.3) == Decimal("27.80")

# Payment tests
assert payout(10, 3.5, 8.5) == Decimal("300.00")
assert payout(8.5, 4.2, 8.7) == Decimal("283.90")
assert payout(12, 3.1, 8.3) == Decimal("333.60")

# Seasonal rate tests
assert rate_per_litre(3.5, 8.5, "apr_jun") == Decimal("32.00")
assert rate_per_litre(4.2, 8.7, "apr_jun") == Decimal("35.75")

# Bonus tests
assert bonus_amount(400) == Decimal("0.00")
assert bonus_amount(500) == Decimal("0.00")
assert bonus_amount(600) == Decimal("300.00")

# Ten-day total test
payments = [
    Decimal("300.00"),
    Decimal("283.90"),
    Decimal("333.60")
]

assert ten_day_total(payments) == Decimal("917.50")


# Invalid input test
try:
    payout(-10, 3.5, 8.5)
    assert False, "Negative quantity should not be accepted"
except ValueError:
    pass

try:
    payout(10, 8.0, 8.5)
    assert False, "Invalid fat should not be accepted"
except ValueError:
    pass


print("All test cases passed successfully!")