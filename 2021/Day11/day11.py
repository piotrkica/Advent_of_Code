with open("day11.txt") as file:
    lines = file.readlines()
    lines = [(line.rstrip()) for line in lines]

size_x = len(lines)
size_y = len(lines[0])
arr = [[int(number) for number in line] for line in lines]

result = 0
for day in range(1, 1000):
    stack = []
    has_flashed = set()
    for i in range(size_x):
        for j in range(size_y):
            arr[i][j] += 1
            if arr[i][j] >= 10:
                stack.append((i, j))
                has_flashed.add((i, j))

    while len(stack) != 0:
        i, j = stack.pop()
        result += 1

        for x in range(-1, 2):
            for y in range(-1, 2):
                if 0 <= i + x < size_x and 0 <= j + y < size_y:
                    arr[i + x][j + y] += 1
                    if arr[i + x][j + y] >= 10 and (i + x, j + y) not in has_flashed:
                        stack.append((i + x, j + y))
                        has_flashed.add((i + x, j + y))

    for i, j in has_flashed:
        arr[i][j] = 0

    if day == 100:
        print(result)  # 1741

    if len(has_flashed) == size_x * size_y:
        result2 = day
        print(result2)  # 440
        break
