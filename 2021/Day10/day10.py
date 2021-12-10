with open("day10.txt") as file:
    lines = file.readlines()
    lines = [(line.rstrip()) for line in lines]

bracket_map = {')': '(', '}': '{', ']': '[', '>': '<', }

score_map = {')': 3, "]": 57, "}": 1197, ">": 25137}
total_score = 0

for line in lines.copy():
    stack = []
    for bracket in line:
        if bracket not in bracket_map:
            stack.append(bracket)
        elif len(stack) != 0 and stack[-1] == bracket_map[bracket]:
            stack.pop()
        elif len(stack) == 0 or stack[-1] != bracket_map[bracket]:
            lines.remove(line)  # must be run before next part to delete incorrect lines
            total_score += score_map[bracket]
            break

result = total_score
print(result)  # 392139


score_map = {'(': 1, "[": 2, "{": 3, "<": 4}
score_array = []

for line in lines.copy():
    stack = []
    score = 0

    for bracket in line:
        if bracket not in bracket_map:
            stack.append(bracket)
        elif len(stack) != 0 and stack[-1] == bracket_map[bracket]:
            stack.pop()
        elif len(stack) == 0 or stack[-1] != bracket_map[bracket]:
            break
    if len(stack) != 0:
        for bracket in stack[::-1]:
            score *= 5
            score += score_map[bracket]
        score_array.append(score)

result2 = sorted(score_array)[len(score_array)//2]
print(result2)  # 4001832844


