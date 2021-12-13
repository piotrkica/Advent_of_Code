with open("day13.txt") as file:
    lines = file.readlines()
    lines = [(line.rstrip()) for line in lines]

folds = lines[lines.index("") + 1:]
coords = [line.split(",") for line in lines[:lines.index("")]]
coords = set((int(x), int(y)) for x, y in coords)

for fold in folds:
    fold_idx = int(fold[fold.index("=")+1:])
    if "x" in fold:
        for x, y in coords.copy():
            if x >= fold_idx:
                coords.add((x-2*(x-fold_idx), y))
                coords.remove((x, y))
    if "y" in fold:
        for x, y in coords.copy():
            if y >= fold_idx:
                coords.add((x, (y - 2 * (y - fold_idx))))
                coords.remove((x, y))

    if fold == folds[0]:
        result = len(coords)
        print(result)  # 755


size_x = max(coords, key=lambda x: x[0])[0] + 1
size_y = max(coords, key=lambda x: x[1])[1] + 1

result2 = [['#' if (x,y) in coords else '.' for x in range(size_x)] for y in range(size_y)]
for row in result2:
    print(row)  # BLKJRBAG
