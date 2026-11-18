import collections, random, time, string

calls = ["seeds not received seeds delayed", "fertiliser price high",
         "seeds price high subsidy not received"]
STOP = {"not", "high"}

def frequencies(texts, stop):
    counts = {}
    for text in texts:
        for word in text.lower().translate(str.maketrans("", "", string.punctuation)).split():
            if word not in stop:
                counts[word] = counts.get(word, 0) + 1
    return counts

def top(counts, k):
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:k]

if __name__ == "__main__":
    counts = frequencies(calls, STOP)
    print(top(counts, 3))
    districts = {"Cuddalore": ["seeds delayed", "water shortage"],
                 "Villupuram": ["fertiliser price high"]}
    print("Complaints per district:", {d: len(v) for d,v in districts.items()})
    print("Counter check:", collections.Counter(counts))
