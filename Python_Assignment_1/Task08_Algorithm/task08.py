"""Task 8: Implement the planned algorithm and display its steps."""

BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

def calculate_one(litres, fat, snf):
    # Validate the values before calculating.
    if litres <= 0:
        raise ValueError("Invalid quantity")
    if not 2.0 <= fat <= 7.0:
        raise ValueError("Invalid fat percentage")
    if not 5.0 <= snf <= 12.0:
        raise ValueError("Invalid SNF percentage")

    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)
    rate = BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE
    payment = round(litres * rate, 2)
    return round(rate, 2), payment

def main():
    print("ALGORITHM: Read -> Validate -> Calculate steps -> Calculate rate -> Calculate payment")
    try:
        litres = float(input("Enter litres: "))
        fat = float(input("Enter fat percentage: "))
        snf = float(input("Enter SNF percentage: "))
        rate, payment = calculate_one(litres, fat, snf)
        print(f"Rate per litre: Rs.{rate:.2f}")
        print(f"Payment: Rs.{payment:.2f}")
    except ValueError as error:
        print("Error:", error)

if __name__ == "__main__":
    main()
