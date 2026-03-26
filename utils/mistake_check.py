def detect_mistakes(eq):

    mistakes = []

    if "--" in eq:
        mistakes.append("Possible sign error detected")

    if eq.count("(") != eq.count(")"):
        mistakes.append("Missing bracket detected")

    if "+-" in eq or "-+" in eq:
        mistakes.append("Possible arithmetic trap")

    if "=" not in eq:
        mistakes.append("Equation missing '=' sign")

    if len(mistakes) == 0:
        mistakes.append("No mistakes detected")

    return mistakes