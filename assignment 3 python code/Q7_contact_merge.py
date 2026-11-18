import re, time

contacts_a = [
 {"name":"Dr. Ravi","phone":"+91 98400 12345","email":"ravi@example.com"},
 {"name":"Anu","phone":"9876543210","email":"anu@example.com"}
]
contacts_b = [
 {"name":"ravi kumar","phone":"9840012345","email":"rk@example.com"},
 {"name":"Anu S","phone":"98765-43210","email":"anu@example.com"}
]

def normalise_phone(phone):
    digits = "".join(ch for ch in phone if ch.isdigit())
    if digits.startswith("91") and len(digits) == 12: digits = digits[2:]
    return digits

def merge_contacts(*groups):
    merged={}
    for group in groups:
        for contact in group:
            key=normalise_phone(contact.get("phone",""))
            if not key: continue
            if key not in merged:
                merged[key]={"names":set(),"phones":set(),"emails":set()}
            if contact.get("name"): merged[key]["names"].add(contact["name"].strip())
            if contact.get("phone"): merged[key]["phones"].add(contact["phone"])
            if contact.get("email"): merged[key]["emails"].add(contact["email"].lower())
    return merged

if __name__ == "__main__":
    result=merge_contacts(contacts_a, contacts_b)
    for phone, info in result.items():
        print(phone, {k: sorted(v) for k,v in info.items()})
