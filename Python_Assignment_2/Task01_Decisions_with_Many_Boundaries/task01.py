"""TASK 1 – Decisions with Many Boundaries
Problem Context: State Electricity Subsidy Eligibility
"""

def subsidy_separate(units, ration_card, elderly):
    """Determine subsidy using separate if statements."""
    results = []

    if units <= 100:
        results.append("Full subsidy")

    if 101 <= units <= 200 and ration_card:
        results.append("Partial subsidy")

    if units > 200 and elderly:
        results.append("Elderly-member subsidy")

    if not results:
        results.append("No subsidy")

    return results


def subsidy(units, ration_card, elderly):
    """Determine household subsidy eligibility."""
    if units <= 100:
        return "Full subsidy"
    elif 101 <= units <= 200:
        if ration_card:
            return "Partial subsidy"
        else:
            return "No subsidy"
    elif units > 200:
        if elderly:
            return "Elderly-member subsidy"
        else:
            return "No subsidy"


def subsidy_match(units, ration_card, elderly):
    """Determine subsidy using match-case (Python 3.10+)."""
    match True:
        case _ if units <= 100:
            return "Full subsidy"
        case _ if 101 <= units <= 200 and ration_card:
            return "Partial subsidy"
        case _ if units > 200 and elderly:
            return "Elderly-member subsidy"
        case _:
            return "No subsidy"


households = [
    (80, True, False),
    (100, False, False),
    (101, True, False),
    (101, False, False),
    (150, True, False),
    (200, True, False),
    (201, True, False),
    (250, False, True)
]

print("Implementation Using Separate If Statements")
print(subsidy_separate(100, True, True))
print(subsidy_separate(150, True, False))
print(subsidy_separate(250, False, True))

print("\\nImplementation Using If-Elif-Else")
for i, household in enumerate(households, 1):
    result = subsidy(*household)
    print(f"Household {i}: {result}")

print("\\nAlternative Concept – Match-Case")
print(subsidy_match(100, False, False))
print(subsidy_match(150, True, False))
print(subsidy_match(250, False, True))
