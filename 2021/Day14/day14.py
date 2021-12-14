from collections import defaultdict, Counter

with open("day14.txt") as file:
    lines = file.readlines()
    lines = [(line.rstrip()) for line in lines]

polymer = lines[0]
rules = lines[2:]
rules_map = dict()

for rule in rules:
    left, right = rule.split(" -> ")
    rules_map[left] = right

pair_counter = Counter([polymer[i:i + 2] for i in range(len(polymer) - 1)])

for step in range(40):  # part1: 10 -> result = 3213
    new_pair_counter = defaultdict(int)
    for rule, counter in pair_counter.items():
        new_element = rules_map[rule]
        new_pair_counter[rule[0]+new_element] += pair_counter[rule]
        new_pair_counter[new_element+rule[1]] += pair_counter[rule]
    pair_counter = new_pair_counter

element_counter = defaultdict(int)
for rule, counter in pair_counter.items():
    element_counter[rule[1]] += counter

result2 = max(element_counter.values()) - min(element_counter.values())
print(result2)  # 3711743744429
