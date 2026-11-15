"""Task 11: Recommended Decimal rounding and rate-card configuration."""
from decimal import Decimal, ROUND_HALF_UP

# Rate-card values are kept in this Python file so the task folder contains
# only Python source files.
RATE_CARD = {
    "base_rate": Decimal("30.00"),
    "fat_step_value": Decimal("0.40"),
    "snf_step_value": Decimal("0.30"),
}

amount = Decimal("283.905")
rounded_amount = amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
print("Rounded payment:", rounded_amount)
print("Loaded rate card:", RATE_CARD)
print("\nDesign limitations:")
print("- No permanent farmer database")
print("- No authentication or audit history")
print("- No multi-centre transaction management")
print("Recommended extensions: database, access control, versioned rate cards and backups.")
