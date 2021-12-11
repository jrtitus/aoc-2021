with open("input.txt") as f:
    lines = f.readlines()

count = 0
for l in range(1, len(lines)):
    if int(lines[l]) > int(lines[l - 1]):
        count += 1

print(count)