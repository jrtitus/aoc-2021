def getMaxXY(pairs):
    maxX = 0
    maxY = 0
    for xyset in pairs:
        [x1, y1, x2, y2] = xyset
        if x1 > maxX:
            maxX = x1
        if x2 > maxX:
            maxX = x2
        if y1 > maxY:
            maxY = y1
        if y2 > maxY:
            maxY = y2

    return [maxX, maxY]


def getRange(a, b):
    return a > b and range(a, b - 1, -1) or range(a, b + 1)


with open("input.txt") as f:
    allLines = f.readlines()

# get all the pairs we actually want
filteredPairs = []
for line in allLines:
    pairs = line.splitlines()[0].split(" -> ")
    [x1, y1] = pairs[0].split(",")
    [x2, y2] = pairs[1].split(",")

    filteredPairs.append([int(x1), int(y1), int(x2), int(y2)])

# find the max X and Y values for those pairs
[maxX, maxY] = getMaxXY(filteredPairs)

# construct the matrix from (0,0) to (maxX, maxY)
matrix = []
for y in range(0, maxY + 1):
    matrix.append([])
    for x in range(0, maxX + 1):
        matrix[y].append(0)

# fill in the matrix
for xyset in filteredPairs:
    [x1, y1, x2, y2] = xyset
    if y1 == y2:
        # horizontal line
        hl = getRange(x1, x2)
        for x in hl:
            matrix[y1][x] += 1
    elif x1 == x2:
        # vertical line
        vl = getRange(y1, y2)
        for y in vl:
            matrix[y][x1] += 1
    else:
        # diagonal line
        dlx = getRange(x1, x2)
        dly = getRange(y1, y2)
        for idx in range(0, len(dlx)):
            matrix[dly[idx]][dlx[idx]] += 1

# count the numbers > 1 in the matrix
sum = 0
for y in range(0, len(matrix)):
    # print(matrix[y])  # uncomment to print the matrix
    for x in range(0, len(matrix[y])):
        if matrix[y][x] > 1:
            sum += 1

print(f"Total: {sum}")
