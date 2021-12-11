position = 0
depth = 0

with open("input.txt") as f:
    lines = f.readlines()

for l in lines:
    [cmd, value] = l.split(" ")

    if cmd == "forward":
        position += int(value)

    elif cmd == "down":
        depth += int(value)

    elif cmd == "up":
        depth -= int(value)

print(f"Final result is {position * depth}")