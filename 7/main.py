def sumOf(val):
    sum = 0
    for x in range(0, val + 1):
        sum += x

    return sum


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

# get fuel calculations for each location
cost = []
for pos in range(0, maxPos):
    sum = 0
    for crab in positions:
        sum += sumOf(abs(crab - pos))

    cost.append(sum)

# find minimum cost
costPosition = 0
minCost = cost[costPosition]
for idx in range(1, len(cost)):
    if cost[idx] < minCost:
        minCost = cost[idx]
        costPosition = idx
    elif cost[idx] > minCost:
        break

print(f"Minimum fuel cost {minCost} found at position {costPosition}")
