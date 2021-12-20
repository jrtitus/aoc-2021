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


with open("input.txt") as f:
    allLines = f.readlines()

# get all the pairs we actually want
filteredPairs = []
for line in allLines:
    pairs = line.splitlines()[0].split(" -> ")
    [x1, y1] = pairs[0].split(",")
    [x2, y2] = pairs[1].split(",")

    if (x1 == x2) or (y1 == y2):
        filteredPairs.append([int(x1), int(y1), int(x2), int(y2)])

# find the max X and Y values for those pairs
[maxX, maxY] = getMaxXY(filteredPairs)

# construct the matrix from (0,0) to (maxX, maxY)
matrix = []
for x in range(0, maxX + 1):
    matrix.append([])
    for y in range(0, maxY + 1):
        matrix[x].append(0)

# fill in the matrix
for xyset in filteredPairs:
    [x1, y1, x2, y2] = xyset
    if y1 == y2:
        # horizontal line
        hl = x1 > x2 and range(x2, x1 + 1) or range(x1, x2 + 1)
        for x in hl:
            matrix[x][y1] += 1
    else:
        # vertical line
        vl = y1 > y2 and range(y2, y1 + 1) or range(y1, y2 + 1)
        for y in vl:
            matrix[x1][y] += 1

# count the numbers >1 in the matrix
sum = 0
for x in range(0, len(matrix)):
    for y in range(0, len(matrix[x])):
        if matrix[x][y] > 1:
            sum += 1

print(f"Total: {sum}")
