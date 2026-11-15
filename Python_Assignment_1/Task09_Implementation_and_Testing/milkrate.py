"""Reusable rate and payout module for the village milk co-operative."""
BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

def rate_per_litre(fat, snf):
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)
    return round(BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE, 2)

def payout(litres, fat, snf):
    if litres <= 0:
        raise ValueError("Litres must be greater than zero.")
    return round(litres * rate_per_litre(fat, snf), 2)

if __name__ == "__main__":
    examples = [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.3)]
    for litres, fat, snf in examples:
        print(f"{litres:5} L fat {fat} snf {snf} rate {rate_per_litre(fat, snf):6.2f} pay {payout(litres, fat, snf):8.2f}")
