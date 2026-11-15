"""Task 9: Interactive validated milk payment calculator."""
from milkrate import rate_per_litre, payout

def read_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def validate_entry(litres, fat, snf):
    return litres > 0 and 2.0 <= fat <= 7.0 and 5.0 <= snf <= 12.0

def main():
    total = 0.0
    try:
        count = int(input("Enter number of entries: "))
        if count <= 0:
            print("Enter at least one entry.")
            return
        for index in range(count):
            print(f"\nEntry {index + 1}")
            litres = read_number("Enter litres: ")
            fat = read_number("Enter fat percentage: ")
            snf = read_number("Enter SNF percentage: ")
            if validate_entry(litres, fat, snf):
                rate = rate_per_litre(fat, snf)
                amount = payout(litres, fat, snf)
                total += amount
                print(f"Rate per litre: Rs.{rate:.2f}")
                print(f"Payment: Rs.{amount:.2f}")
            else:
                print("Invalid entry. Check litres, fat and SNF ranges.")
        print(f"\nTotal payment: Rs.{total:.2f}")
    except ValueError:
        print("Number of entries must be a whole number.")

if __name__ == "__main__":
    main()
