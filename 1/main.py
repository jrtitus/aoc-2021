with open("input.txt") as f:
    lines = f.readlines()

sums = []
for l in range(2, len(lines)):
    sums.append(int(lines[l]) + int(lines[l-1]) + int(lines[l-2]))

count = 0
for s in range(1, len(sums)):
    if sums[s] > sums[s-1]:
        count += 1

print(count)