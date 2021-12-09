with open("day7.txt") as file:
    lines = file.readlines()

positions = list(map(lambda x: int(x), lines[0].split(",")))

result = float("inf")
for i in range(max(positions) + 1):
    move_costs = [abs(position - i) for position in positions]
    result = int(min(result, sum(move_costs)))

print(result)  # 342534


result2 = float("inf")
for i in range(max(positions) + 1):
    move_costs = [(abs(position - i)) * (abs(position - i) + 1) / 2 for position in positions]
    result2 = int(min(result2, sum(move_costs)))

print(result2)  # 94004208
