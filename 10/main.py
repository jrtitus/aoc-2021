from math import floor
from typing import List

scores = {
    "(": 1,
    ")": 3,
    "[": 2,
    "]": 57,
    "{": 3,
    "}": 1197,
    "<": 4,
    ">": 25137
}


def isOpeningSymbol(s):
    return s == "[" or s == "<" or s == "{" or s == "("


def isMatching(s1, s2):
    return (s1 == "[" and s2 == "]") or (s1 == "<" and s2 == ">") or (s1 == "{" and s2 == "}") or (s1 == "(" and s2 == ")")


def calculateCompletionScore(stack: List):
    score = 0
    stack.reverse()
    for symbol in stack:
        score *= 5
        score += scores[symbol]

    return score


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()

    errorScore = 0
    completionScore = 0
    completionScores = []

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
            completionScores.append(
                calculateCompletionScore(openingStack))
        else:
            errorScore += scores[corruptSymbol]

    completionScores.sort()

    print(f"Final corruption score is {errorScore}")
    print(
        f"Median completion score is {completionScores[floor(len(completionScores) / 2)]}")
