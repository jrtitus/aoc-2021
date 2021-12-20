def getDigit(segment):
    seglen = len(segment)
    if seglen == 2:
        return 1
    if seglen == 4:
        return 4
    if seglen == 3:
        return 7
    if seglen == 7:
        return 8
    return -1


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()

    uniqueDigits = 0
    for line in lines:
        [input, output] = line.split(" | ")
        output = output.splitlines()[0].split(" ")
        for o in output:
            digit = getDigit(o)
            if digit == 1 or digit == 4 or digit == 7 or digit == 8:
                uniqueDigits += 1

    print(f"1, 4, 7, or 8 appears {uniqueDigits} times in the output")
