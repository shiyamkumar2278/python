from decimal import Decimal
from milkrate import rate_per_litre, payout, bonus, ten_day_total

def test_all():
    assert rate_per_litre("4.26", "8.67", 4) == Decimal("36.20")
    assert rate_per_litre("4.26", "8.67", 7) == Decimal("33.80")
    assert payout(10, "4.26", "8.67", 4) == Decimal("362.00")
    assert payout(10, "4.26", "8.67", 7) == Decimal("338.00")
    assert bonus(500) == Decimal("0.00")
    assert bonus(501) == Decimal("250.50")
    assert bonus(600) == Decimal("300.00")

    entries = [("10", "4.26", "8.67"),
               ("200", "4.26", "8.67"),
               ("291", "4.26", "8.67")]
    result = ten_day_total(entries, 4)
    assert result["total_litres"] == Decimal("501")
    assert result["milk_payment"] == Decimal("18136.20")
    assert result["bonus"] == Decimal("250.50")
    assert result["final_payment"] == Decimal("18386.70")

if __name__ == "__main__":
    test_all()
    print("All tests passed!")
