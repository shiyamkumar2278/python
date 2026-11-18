from pathlib import Path
import re, csv

def valid_email(email):
    return bool(re.fullmatch(r"[^\\s@]+@[^\\s@]+\\.[^\\s@]+", email))

def process_folder(folder, output="fest_output"):
    folder=Path(folder); out=Path(output); out.mkdir(exist_ok=True)
    master={}; seen=set(); errors=[]
    for file in sorted(folder.glob("*.txt")):
        try:
            with file.open(encoding="utf-8") as f:
                for line_no,line in enumerate(f,1):
                    try:
                        parts=line.strip().split(",")
                        if len(parts)!=5: raise ValueError("expected 5 fields")
                        reg,name,dept,email,events=parts
                        if not valid_email(email): raise ValueError("invalid email")
                        if reg in seen:
                            master[reg]["events"].update(events.split(";"))
                            master[reg]["emails"].add(email.lower())
                        else:
                            seen.add(reg)
                            master[reg]={"name":name,"department":dept,
                                         "emails":{email.lower()},"events":set(events.split(";"))}
                    except ValueError as exc:
                        errors.append(f"{file.name}:{line_no}: {exc}")
        except (FileNotFoundError, UnicodeDecodeError, PermissionError) as exc:
            errors.append(f"{file.name}: {exc}")
    with (out/"master.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.writer(f); w.writerow(["reg","name","department","emails","events"])
        for reg,item in sorted(master.items()):
            w.writerow([reg,item["name"],item["department"],";".join(sorted(item["emails"])),";".join(sorted(item["events"]))])
    all_events={}
    for reg,item in master.items():
        for event in item["events"]: all_events.setdefault(event,[]).append(reg)
    for event,regs in all_events.items():
        (out/f"{event}.txt").write_text("\\n".join(sorted(regs)),encoding="utf-8")
    (out/"errors.log").write_text("\\n".join(errors),encoding="utf-8")
    return master,errors

if __name__ == "__main__":
    sample=Path("fest_data"); sample.mkdir(exist_ok=True)
    (sample/"dept1.txt").write_text("192311001,Ravi,ECE,ravi@mail.com,Singing;Dance\\n192311001,Ravi,ECE,ravi@mail.com,Drama\\n192311002,Anu,CSE,bad-email,Quiz\\n",encoding="utf-8")
    print(process_folder(sample))
