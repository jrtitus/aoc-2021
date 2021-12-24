scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}


def isOpeningSymbol(s):
    return s == "[" or s == "<" or s == "{" or s == "("


def isMatching(s1, s2):
    return (s1 == "[" and s2 == "]") or (s1 == "<" and s2 == ">") or (s1 == "{" and s2 == "}") or (s1 == "(" and s2 == ")")


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()

    validLines = []
    errorScore = 0

    for line in lines:
        symbols = list(line.splitlines()[0])
        openingStack = []
        corrupted = False
        corruptSymbol = ""
        for s in symbols:
            if isOpeningSymbol(s):
                openingStack.append(s)
            elif isMatching(openingStack[len(openingStack) - 1], s):
                openingStack.pop()
            else:  # line is corrupted
                corrupted = True
                corruptSymbol = s
                break
        if not corrupted:
            validLines.append(symbols)
        else:
            errorScore += scores[corruptSymbol]

    print(f"Final score is {errorScore}")
