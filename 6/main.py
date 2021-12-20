with open("input.txt") as f:
    content = f.read()

# get the school of fish
school = content.splitlines()[0].split(",")

# convert strings to numbers
for fish in range(0, len(school)):
    school[fish] = int(school[fish])

# simulate
days = 80
for day in range(0, days):
    fishToAdd = []
    for fish in range(0, len(school)):
        if school[fish] == 0:
            school[fish] = 6
            fishToAdd.append(8)
            continue
        school[fish] -= 1

    school.extend(fishToAdd)

print(f"Number of fish: {len(school)}")
