from milkrate import (
    rate_per_litre,
    payout,
    ten_day_total,
    bonus_amount
)

from decimal import Decimal


def main():

    farmers = {}

    print("=" * 55)
    print("       KSHEERA MILK PAYMENT CALCULATOR")
    print("=" * 55)

    season = input(
        "Enter season (normal / apr_jun): "
    ).strip().lower()

    if season not in ["normal", "apr_jun"]:
        print("Invalid season. Using normal rate.")
        season = "normal"

    while True:

        print("\nEnter Farmer Details")

        farmer_id = input("Farmer ID (or 'exit' to finish): ").strip()

        if farmer_id.lower() == "exit":
            break

        try:
            litres = Decimal(input("Milk quantity (litres): "))
            fat = Decimal(input("Fat percentage: "))
            snf = Decimal(input("SNF percentage: "))
            shift = input("Shift (Morning/Evening): ").strip()

            if litres < 0:
                print("Error: Quantity cannot be negative.")
                continue

            if not Decimal("2.0") <= fat <= Decimal("7.0"):
                print("Error: Fat must be between 2.0 and 7.0.")
                continue

            if snf < 0:
                print("Error: SNF cannot be negative.")
                continue

            rate = rate_per_litre(fat, snf, season)
            amount = payout(litres, fat, snf, season)

            if farmer_id not in farmers:
                farmers[farmer_id] = {
                    "litres": Decimal("0"),
                    "payments": [],
                    "entries": 0
                }

            farmers[farmer_id]["litres"] += litres
            farmers[farmer_id]["payments"].append(amount)
            farmers[farmer_id]["entries"] += 1

            print("\n----- PAYMENT DETAILS -----")
            print(f"Farmer ID : {farmer_id}")
            print(f"Shift     : {shift}")
            print(f"Rate      : Rs. {rate:.2f}")
            print(f"Payment   : Rs. {amount:.2f}")
            print("---------------------------")

        except ValueError as error:
            print("Invalid input:", error)

    print("\n" + "=" * 60)
    print("              TEN-DAY PAYMENT REPORT")
    print("=" * 60)

    for farmer_id, details in farmers.items():

        total_litres = details["litres"]

        total_payment = ten_day_total(details["payments"])

        bonus = bonus_amount(total_litres)

        final_payment = total_payment + bonus

        print(f"\nFarmer ID       : {farmer_id}")
        print(f"Total Entries   : {details['entries']}")
        print(f"Total Litres    : {total_litres:.2f}")
        print(f"Milk Payment    : Rs. {total_payment:.2f}")
        print(f"Bonus           : Rs. {bonus:.2f}")
        print(f"Final Payment   : Rs. {final_payment:.2f}")

    print("\nPayment calculation completed.")


if __name__ == "__main__":
    main()