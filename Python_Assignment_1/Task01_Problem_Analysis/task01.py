"""Task 1: Identify the milk calculator inputs, outputs and data types."""
from decimal import Decimal
from datetime import date

farmer_id = "F001"
litres = Decimal("12.75")
fat_percent = Decimal("4.2")
snf_percent = Decimal("8.7")
shift = "Morning"
collection_date = date(2026, 11, 15)

print("Ksheera Village Milk Co-operative")
print("INPUTS")
print("Farmer ID:", farmer_id, type(farmer_id).__name__)
print("Litres:", litres, type(litres).__name__)
print("Fat:", fat_percent, type(fat_percent).__name__)
print("SNF:", snf_percent, type(snf_percent).__name__)
print("Shift:", shift, type(shift).__name__)
print("Collection date:", collection_date, type(collection_date).__name__)

BASE_RATE = Decimal("30.00")
BASE_FAT = Decimal("3.5")
BASE_SNF = Decimal("8.5")
FAT_RATE = Decimal("0.40")
SNF_RATE = Decimal("0.30")
STEP = Decimal("0.1")

fat_steps = (fat_percent - BASE_FAT) / STEP
snf_steps = (snf_percent - BASE_SNF) / STEP
rate = BASE_RATE + fat_steps * FAT_RATE + snf_steps * SNF_RATE
payment = litres * rate

print("\nOUTPUT")
print("Rate per litre: Rs.", rate)
print("Payment: Rs.", payment.quantize(Decimal("0.01")))
