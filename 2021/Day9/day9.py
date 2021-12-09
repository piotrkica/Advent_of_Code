with open("day9.txt") as file:
    lines = file.readlines()
    lines = [(line.rstrip()) for line in lines]

size_x = len(lines)
size_y = len(lines[0])
arr = [[0 for _ in range(size_y)] for __ in range(size_x)]

for i, line in enumerate(lines):
    for j, number in enumerate(line):
        arr[i][j] = int(number)

sum_val = 0
for i in range(size_x):
    for j in range(size_y):
        if (i - 1 >= 0 and arr[i - 1][j] <= arr[i][j]) \
                or (j - 1 >= 0 and arr[i][j - 1] <= arr[i][j]) \
                or (i + 1 < size_x and arr[i + 1][j] <= arr[i][j]) \
                or (j + 1 < size_y and arr[i][j + 1] <= arr[i][j]):
            continue
        sum_val += arr[i][j] + 1

result = sum_val
print(result)  # 417


def calc_basin_size(i, j):
    if arr[i][j] == -1 or arr[i][j] == 9:
        return 0
    basin_size = 1
    arr[i][j] = -1
    if not i - 1 < 0 and arr[i - 1][j] != 9:
        basin_size += calc_basin_size(i - 1, j)
    if not j - 1 < 0 and arr[i][j - 1] != 9:
        basin_size += calc_basin_size(i, j - 1)
    if not i + 1 >= size_x and arr[i + 1][j] != 9:
        basin_size += calc_basin_size(i + 1, j)
    if not j + 1 >= size_y and arr[i][j + 1] != 9:
        basin_size += calc_basin_size(i, j + 1)
    return basin_size


basins = []
for i in range(size_x):
    for j in range(size_y):
        curr_basin = 0
        basin_size = calc_basin_size(i, j)
        if basin_size != 0:
            basins.append(basin_size)

basins = sorted(basins, reverse=True)
result2 = basins[0] * basins[1] * basins[2]
print(result2)  # 1148965
