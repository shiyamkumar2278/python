from pathlib import Path
from decimal import Decimal, InvalidOperation

def process_bill(filename):
    total=Decimal("0.00")
    report=[]
    rejected=[]
    with open(filename, "r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            if not line.strip(): continue
            try:
                parts=line.strip().split(",")
                if len(parts) != 3: raise ValueError("expected 3 fields")
                reg, name, amount=parts
                value=Decimal(amount)
                report.append(f"{name} {value:.2f}")
                total += value
            except (ValueError, InvalidOperation) as exc:
                rejected.append((line_no, line.strip(), str(exc)))
    return report, total, rejected

if __name__ == "__main__":
    p=Path("mess_oct.txt")
    if not p.exists():
        p.write_text("192311001,Ravi,1250.50\\n192311002,Anu,900\\nbad,line\\n", encoding="utf-8")
    report,total,rejected=process_bill(p)
    print("\\n".join(report)); print("Total", total); print("Rejected", rejected)
