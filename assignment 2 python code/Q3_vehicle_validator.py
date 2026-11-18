def normalise(text):
    return text.strip().upper().replace(" ", "").replace("-", "")

def is_valid(reg):
    if len(reg) not in (9, 10):
        return False
    return (reg[:2].isalpha() and reg[2:4].isdigit()
            and reg[4:-4].isalpha() and len(reg[4:-4]) in (1, 2)
            and reg[-4:].isdigit())

def format_receipt(reg):
    if not is_valid(reg):
        raise ValueError("Invalid registration number")
    return f"{reg[:2]} {reg[2:4]} {reg[4:-4]} {reg[-4:]}"

if __name__ == "__main__":
    samples = ["tn 09 ab 1234", "KA-01-M-0007", "TN9AB1234",
               "TN 22 1234 AB", "MH 12 DE 1433", "TN-9-AB-1234"]
    for raw in samples:
        reg = normalise(raw)
        status = "valid" if is_valid(reg) else "INVALID"
        receipt = format_receipt(reg) if is_valid(reg) else "-"
        print(f"{raw:18} -> {reg:11} {status:7} {receipt}")
