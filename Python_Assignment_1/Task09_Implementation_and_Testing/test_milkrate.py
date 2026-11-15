from milkrate import rate_per_litre, payout

def test_milk_payment():
    assert rate_per_litre(3.5, 8.5) == 30.00
    assert payout(10, 3.5, 8.5) == 300.00
    assert rate_per_litre(4.2, 8.7) == 33.40
    assert payout(8.5, 4.2, 8.7) == 283.90
    assert rate_per_litre(3.1, 8.3) == 27.80
    assert payout(12, 3.1, 8.3) == 333.60
    assert round(payout(10, 3.5, 8.5) + payout(8.5, 4.2, 8.7) + payout(12, 3.1, 8.3), 2) == 917.50

if __name__ == "__main__":
    test_milk_payment()
    print("All tests passed!")
