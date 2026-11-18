import csv, io, sqlite3
import matplotlib.pyplot as plt

RAW = """station,date,pm25
Adyar,2026-10-01,48
Adyar,2026-10-02,NA
Adyar,2026-10-03,
Guindy,2026-10-01,95
Guindy,2026-10-02,-5
Guindy,2026-10-03,121
Guindy,2026-10-04,1200
"""

def load_clean(text):
    rows=[]
    for row in csv.DictReader(io.StringIO(text)):
        value=row["pm25"].strip()
        if value in {"","NA"}: continue
        try: pm=float(value)
        except ValueError: continue
        if 0 <= pm <= 999:
            rows.append((row["station"],row["date"],pm))
    return rows

def min_max(values):
    if not values: return []
    lo,hi=min(values),max(values)
    if lo==hi: return [0.0 for _ in values]
    return [round((v-lo)/(hi-lo),3) for v in values]

def main():
    clean=load_clean(RAW)
    print("Clean:",clean)
    print("Normalised:",min_max([x[2] for x in clean]))
    con=sqlite3.connect("air_quality.db")
    con.execute("CREATE TABLE IF NOT EXISTS aq(station TEXT, day TEXT, pm25 REAL)")
    con.execute("DELETE FROM aq")
    con.executemany("INSERT INTO aq VALUES(?,?,?)",clean); con.commit()
    result=con.execute("SELECT station, AVG(pm25) FROM aq GROUP BY station").fetchall()
    print("SQL averages:",result)
    if clean:
        names=[x[0] for x in clean]; values=[x[2] for x in clean]
        plt.bar(names,values); plt.xlabel("Station"); plt.ylabel("PM2.5")
        plt.title("Clean PM2.5 readings"); plt.tight_layout(); plt.savefig("pm25_chart.png"); plt.show()
    con.close()

if __name__=="__main__": main()
