"""Task 5: Read input, convert types, validate and format values."""

def read_number(prompt):
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Invalid input. Please enter a number (use a decimal point).")

def main():
    try:
        litres = read_number("Enter milk quantity in litres: ")
        fat = read_number("Enter fat percentage: ")
        snf = read_number("Enter SNF percentage: ")

        if litres <= 0:
            print("Invalid quantity: litres must be greater than zero.")
        elif not 2.0 <= fat <= 7.0:
            print("Invalid fat: enter a value from 2.0 to 7.0.")
        elif not 5.0 <= snf <= 12.0:
            print("Invalid SNF: enter a value from 5.0 to 12.0.")
        else:
            print("\nVALID INPUT")
            print(f"{litres:8.2f} L")
            print(f"{fat:8.2f} % fat")
            print(f"{snf:8.2f} % SNF")
    except KeyboardInterrupt:
        print("\nInput cancelled.")

if __name__ == "__main__":
    main()
