import re
POSITIVE={"good","clean","fast","helpful","improved"}
NEGATIVE={"bad","dirty","slow","rude","smoke","broken"}
NEGATORS={"not","never","no"}

def score(text):
    words=re.findall(r"[a-z']+",text.lower())
    total=0
    for i,word in enumerate(words):
        value=1 if word in POSITIVE else -1 if word in NEGATIVE else 0
        if i>0 and words[i-1] in NEGATORS: value=-value
        total+=value
    return total

def label(text):
    s=score(text)
    return "positive" if s>0 else "negative" if s<0 else "neutral"

def summarise(text,k=2):
    sentences=[s.strip() for s in re.split(r"(?<=[.!?])\\s+",text) if s.strip()]
    freq={}
    for sentence in sentences:
        for word in re.findall(r"[a-z]+",sentence.lower()):
            if word not in {"the","and","is","are","a","of","to","in"}:
                freq[word]=freq.get(word,0)+1
    ranked=sorted(sentences,key=lambda s:sum(freq.get(w,0) for w in re.findall(r"[a-z]+",s.lower())),reverse=True)
    return " ".join(ranked[:k])

if __name__=="__main__":
    complaints=["Roads are clean and the bus was fast.",
                "Smoke from the factory, air is bad.",
                "The staff were not helpful.",
                "Not bad, service improved."]
    for c in complaints: print(f"{label(c):8} | {c}")
    print("Summary:",summarise("Air is dirty. Roads are clean. Air quality is bad. Roads need repair."))
