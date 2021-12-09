with open("day2.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

horiz_pos, depth = 0, 0

for line in lines:
    direction, number = line.split(" ")
    number = int(number)
    if direction == "forward":
        horiz_pos += number
    elif direction == "up":
        depth -= number
    else:
        depth += number

result = (horiz_pos * depth)
print(result)  # 2150351


horiz_pos, depth, aim = 0, 0, 0

for line in lines:
    direction, number = line.split(" ")
    number = int(number)
    if direction == "forward":
        horiz_pos += number
        depth += number * aim
    elif direction == "up":
        aim -= number
    else:
        aim += number

result2 = (horiz_pos * depth)
print(result2)  # 1842742223
