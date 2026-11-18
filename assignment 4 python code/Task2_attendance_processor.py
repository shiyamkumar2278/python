from pathlib import Path
from collections import defaultdict
import csv

def process_files(folder, output_folder="reports"):
    folder=Path(folder); out=Path(output_folder); out.mkdir(exist_ok=True)
    counts=defaultdict(lambda:[0,0])  # reg -> [present, total]
    errors=[]
    for file in sorted(folder.glob("*.csv")):
        with file.open(encoding="utf-8", newline="") as f:
            for line_no, row in enumerate(csv.reader(f), 1):
                if not row: continue
                try:
                    if len(row)!=3: raise ValueError("expected 3 fields")
                    reg, date, status=row
                    if status not in {"P","A"}: raise ValueError("status must be P or A")
                    counts[reg][1]+=1
                    if status=="P": counts[reg][0]+=1
                except ValueError as exc:
                    errors.append(f"{file.name},{line_no},{exc}")
    with (out/"attendance_report.csv").open("w", newline="", encoding="utf-8") as f:
        w=csv.writer(f); w.writerow(["register","present","total","percentage"])
        for reg,(present,total) in sorted(counts.items()):
            w.writerow([reg,present,total,round(present/total*100,2)])
    (out/"errors.log").write_text("\\n".join(errors), encoding="utf-8")
    return counts, errors

if __name__ == "__main__":
    folder=Path("attendance_data"); folder.mkdir(exist_ok=True)
    sample=folder/"day1.csv"
    if not sample.exists():
        sample.write_text("192311001,2026-10-08,P\\n192311002,2026-10-08,A\\nbad,line\\n", encoding="utf-8")
    print(process_files(folder))
