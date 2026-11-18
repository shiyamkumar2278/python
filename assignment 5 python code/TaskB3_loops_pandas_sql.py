import csv, io, sqlite3, time, cProfile, random
from collections import defaultdict
try:
    import pandas as pd
except ImportError:
    pd=None

def generate_rows(stations=3, days=30):
    rows=[]
    for s in range(stations):
        for d in range(days):
            rows.append((f"Station{s+1}",f"2026-10-{d+1:02d}",round(random.uniform(5,150),2)))
    return rows

def loops_mean(rows):
    totals=defaultdict(lambda:[0.0,0])
    for station,day,value in rows:
        key=(station,day); totals[key][0]+=value; totals[key][1]+=1
    return {k:v[0]/v[1] for k,v in totals.items()}

def sql_mean(rows):
    con=sqlite3.connect(":memory:")
    con.execute("CREATE TABLE aq(station TEXT,day TEXT,pm25 REAL)")
    con.executemany("INSERT INTO aq VALUES(?,?,?)",rows)
    result=dict(((s,d),avg) for s,d,avg in con.execute("SELECT station,day,AVG(pm25) FROM aq GROUP BY station,day"))
    con.close(); return result

def pandas_mean(rows):
    if pd is None: return None
    df=pd.DataFrame(rows,columns=["station","day","pm25"])
    return df.groupby(["station","day"])["pm25"].mean().to_dict()

if __name__=="__main__":
    data=generate_rows(3,30)
    expected=loops_mean(data); print("Loop result count:",len(expected))
    print("SQL matches:",expected==sql_mean(data))
    p=pandas_mean(data)
    if p is not None: print("Pandas matches:",all(abs(expected[k]-p[k])<1e-9 for k in expected))
    cProfile.run("loops_mean(data)")
    for n in (1,12,120):
        rows=generate_rows(n,365)
        for fn in (loops_mean,sql_mean):
            start=time.perf_counter(); fn(rows)
            print(n,fn.__name__,round(time.perf_counter()-start,4),"sec")
