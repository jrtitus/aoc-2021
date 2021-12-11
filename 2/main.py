position = 0
depth = 0
aim = 0

with open("input.txt") as f:
    lines = f.readlines()

for l in lines:
    [cmd, value] = l.split(" ")

    if cmd == "forward":
        position += int(value)
        depth += (aim * int(value))

    elif cmd == "down":
        aim += int(value)

    elif cmd == "up":
        aim -= int(value)

print(f"Final result is {position * depth}")