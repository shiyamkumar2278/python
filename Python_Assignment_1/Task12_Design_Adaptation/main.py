from milkrate import rate_per_litre, payout, ten_day_total

def main():
    print("SEASONAL MILK PAYMENT CALCULATOR")
    month = int(input("Enter month number (1-12): "))
    litres = input("Enter litres: ")
    fat = input("Enter fat percentage (up to 2 decimals): ")
    snf = input("Enter SNF percentage (up to 2 decimals): ")
    print("Rate per litre: Rs.", rate_per_litre(fat, snf, month))
    print("Payment: Rs.", payout(litres, fat, snf, month))

    print("\nTen-day example including volume bonus:")
    entries = [("10", "4.26", "8.67"),
               ("200", "4.26", "8.67"),
               ("291", "4.26", "8.67")]
    result = ten_day_total(entries, month)
    for key, value in result.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
