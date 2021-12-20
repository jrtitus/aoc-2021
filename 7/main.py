from math import floor


def sumOf(val):
    sum = 0
    for x in range(0, val + 1):
        sum += x

    return sum


def getFuelCostForPosition(pos, positions):
    sum = 0
    for crab in positions:
        sum += sumOf(abs(crab - pos))

    return sum


def searchForMinCost(positions, minPos, maxPos):
    currentPos = floor((maxPos + minPos) / 2)
    cost = getFuelCostForPosition(currentPos, positions)
    # lowest cost found
    if maxPos - minPos == 2:
        return cost, currentPos
    # check upper; go lower
    if cost < getFuelCostForPosition(currentPos + 1, positions):
        return searchForMinCost(positions, minPos, currentPos)
    # otherwise, go higher
    else:
        return searchForMinCost(positions, currentPos, maxPos)


if __name__ == "__main__":
    with open("input.txt") as f:
        content = f.read()

    # get the list of positions
    positions = content.splitlines()[0].split(",")

    # convert strings to numbers and get the max position
    maxPos = 0
    for crab in range(0, len(positions)):
        positions[crab] = int(positions[crab])
        if positions[crab] > maxPos:
            maxPos = positions[crab]

    # find the minimum cost and position
    minCost, costPosition = searchForMinCost(positions, 0, maxPos)

    print(f"Minimum fuel cost {minCost} found at position {costPosition}")
