"""TASK 3 – Engineer a Vehicle Registration Number Validator
Problem Context: Toll Plaza Number-Plate Records
"""

def normalise(text):
    """Remove spaces and hyphens and convert to uppercase."""
    text = text.strip()
    text = text.replace(" ", "")
    text = text.replace("-", "")
    return text.upper()


def is_valid(reg):
    """Check the structure of a vehicle registration number."""
    if len(reg) not in (9, 10):
        return False

    state = reg[:2]
    district = reg[2:4]
    series = reg[4:-4]
    number = reg[-4:]

    return (
        state.isalpha()
        and district.isdigit()
        and series.isalpha()
        and len(series) in (1, 2)
        and number.isdigit()
    )


def format_registration(reg):
    """Format the registration number for printing."""
    if not is_valid(reg):
        return "Invalid registration number"

    return " ".join([
        reg[:2],
        reg[2:4],
        reg[4:-4],
        reg[-4:]
    ])


# Alternative concept – regular expressions
import re

def is_valid_regex(reg):
    pattern = r"[A-Z]{2}[0-9]{2}[A-Z]{1,2}[0-9]{4}"
    return re.fullmatch(pattern, reg) is not None


if __name__ == "__main__":
    registration = "tn 09 ab 1234"
    reg = normalise(registration)

    print("Normalised:", reg)
    print("Valid:", is_valid(reg))
    print("Receipt Format:", format_registration(reg))

    print("\\nComplete Program Test Cases")
    samples = [
        "tn 09 ab 1234",
        "KA-01-M-0007",
        "TN09AB1234",
        "TN9AB1234",
        "TN 22 1234 AB",
        "AP 05 XY 9876"
    ]

    for value in samples:
        normalised = normalise(value)
        status = "valid" if is_valid(normalised) else "INVALID"
        print(f"{value:<18} -> {normalised:<10} {status}")

    print("\\nRegular Expression Tests")
    print(is_valid_regex("TN09AB1234"))
    print(is_valid_regex("TN9AB1234"))

    print("\\nString Immutability")
    text = "tn09ab1234"
    text.upper()
    print(text)
    text = text.upper()
    print(text)

    print("\\nString Slicing")
    s1 = "TN09M1234"
    s2 = "TN09AB1234"
    print("s1[-4:]:", s1[-4:])
    print("s2[-4:]:", s2[-4:])
    print("s1[4:-4]:", s1[4:-4])
    print("s2[4:-4]:", s2[4:-4])
    print("s1[:2]:", s1[:2])
    print("s1[2:4]:", s1[2:4])
