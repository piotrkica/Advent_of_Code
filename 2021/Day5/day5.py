with open("day5.txt") as file:
    lines = file.readlines()
    lines = [(line.rstrip()) for line in lines]

size_x = 1000
size_y = 1000

map_2d = [[0 for _ in range(size_x + 2)] for _1 in range(size_y + 1)]
for line in lines:
    x, y = line.split("->")
    x1, y1 = x.split(",")
    x2, y2 = y.split(",")
    x1, x2, y1, y2 = list(map(lambda x: int(x), [x1, x2, y1, y2]))

    if x1 == x2:
        for i in range(min(y1, y2), max(y2, y1) + 1):
            map_2d[x1][i] += 1
    elif y1 == y2:
        for i in range(min(x1, x2), max(x2, x1) + 1):
            map_2d[i][y1] += 1

result = sum([sum([x > 1 for x in row]) for row in map_2d])
print(result)  # 167165280


map_2d = [[0 for _ in range(size_x + 2)] for _1 in range(size_y + 1)]
for line in lines:
    x, y = line.split("->")
    x1, y1 = x.split(",")
    x2, y2 = y.split(",")
    x1, x2, y1, y2 = list(map(lambda x: int(x), [x1, x2, y1, y2]))

    if x1 == x2:
        for i in range(min(y1, y2), max(y2, y1) + 1):
            map_2d[x1][i] += 1
    elif y1 == y2:
        for i in range(min(x1, x2), max(x2, x1) + 1):
            map_2d[i][y1] += 1
    elif abs(x1 - x2) == abs(y1 - y2):
        for i in range(abs(x1 - x2) + 1):
            if x1 < x2:
                if y1 < y2:
                    map_2d[x1 + i][y1 + i] += 1
                else:
                    map_2d[x1 + i][y1 - i] += 1
            else:
                if y1 < y2:
                    map_2d[x1 - i][y1 + i] += 1
                else:
                    map_2d[x1 - i][y1 - i] += 1

result2 = sum([sum([x > 1 for x in row]) for row in map_2d])
print(result2)  # 16716
