import os, tempfile

class InvalidRecord(Exception):
    """Attendance record is not in the required format."""

def parse_line(line):
    parts=line.strip().split(",")
    if len(parts)!=3:
        raise InvalidRecord(f"expected 3 fields, found {len(parts)}")
    reg, date, status=parts
    if status not in {"P","A"}:
        raise InvalidRecord(f"invalid status '{status}'")
    return reg,date,status

def summarise(path):
    present=absent=0
    errors=[]
    try:
        with open(path, encoding="utf-8") as f:
            for line_no,line in enumerate(f,1):
                try:
                    _,_,status=parse_line(line)
                    if status=="P": present+=1
                    else: absent+=1
                except InvalidRecord as exc:
                    errors.append((line_no,str(exc)))
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"Attendance file not found: {path}") from exc
    return present,absent,errors

if __name__ == "__main__":
    data=("192311001,2026-10-08,P\\n192311002,2026-10-08,A\\n"
          "192311003,2026-10-08\\n192311004,2026-10-08,L\\n")
    with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False, encoding="utf-8") as tmp:
        tmp.write(data); name=tmp.name
    try: print(summarise(name))
    finally: os.remove(name)
