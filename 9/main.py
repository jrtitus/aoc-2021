from math import floor

with open("input.txt") as f:
    lines = f.readlines()

heights = []
lineLength = len(lines[0]) - 1


# determine if the neighbor is taller
def isLowestNeighbor(height, neighborPos):
    try:
        neighbor = heights[neighborPos]
        if height >= neighbor:
            return False
    except:
        pass

    return True


def getRiskLevel(pos):
    height = heights[pos]

    if isLowestNeighbor(height, pos - 1) and \
            isLowestNeighbor(height, pos + 1) and \
            isLowestNeighbor(height, pos - lineLength) and \
            isLowestNeighbor(height, pos + lineLength):
        print(
            f"Risk point found at ({pos % lineLength},{floor(pos / lineLength)}) with value of {height}")
        return 1 + height

    return 0


if __name__ == "__main__":
    for line in lines:
        heights.extend(list(line.splitlines()[0]))

    # convert heights to numbers
    for h in range(0, len(heights)):
        heights[h] = int(heights[h])

    sum = 0
    for h in range(len(heights)):
        sum += getRiskLevel(h)

    print(f"The sum of the risk levels is {sum}")
