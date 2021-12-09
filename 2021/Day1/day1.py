with open("day1.txt") as file:
    lines = file.readlines()
    lines = [int(line.rstrip()) for line in lines]

result1 = sum([lines[i] < lines[i + 1] for i in range(len(lines) - 1)])
print(result1)  # 1121


sum_list = [lines[i] + lines[i + 1] + lines[i + 2] for i in range(len(lines) - 2)]
result2 = sum([sum_list[i] < sum_list[i + 1] for i in range(len(sum_list) - 1)])
print(result2)  # 1065
