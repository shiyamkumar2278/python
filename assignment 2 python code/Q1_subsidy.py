def separate_if(units, ration, senior):
    result = []
    if units <= 100: result.append("Full subsidy")
    if 101 <= units <= 200 and ration: result.append("Partial subsidy")
    if units > 200 and senior: result.append("Senior citizen subsidy")
    if not result: result.append("No subsidy")
    return result

def decide(units, ration, senior):
    if units < 0: return "Invalid consumption"
    elif units <= 100: return "Full subsidy"
    elif 101 <= units <= 200 and ration: return "Partial subsidy"
    elif units > 200 and senior: return "Senior citizen subsidy"
    else: return "No subsidy"

if __name__ == "__main__":
    cases = [(100,False,False),(101,True,False),(200,True,False),(201,False,True),
             (101,False,False),(200,False,True),(250,False,False),(80,True,True)]
    for u,r,s in cases:
        print(u, r, s, "=>", decide(u,r,s), "| separate if:", separate_if(u,r,s))
