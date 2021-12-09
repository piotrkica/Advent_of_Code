with open("day3.txt") as file:
    lines = file.readlines()
    lines = [(line.rstrip()) for line in lines]

number_len = len(lines[0])
list_len = len(lines)

gamma = ""
epsilon = ""
for bit in range(number_len):
    zeros_counter = sum([lines[i][bit] == "0" for i in range(list_len)])
    ones_counter = sum([lines[i][bit] == "1" for i in range(list_len)])
    if zeros_counter >= ones_counter:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

result = int(gamma, 2) * int(epsilon, 2)
print(result)  # 741950


most_common = lines.copy()  # for oxygen generator rating
least_common = lines.copy()  # for CO2 scrubber rating

for bit in range(number_len):
    zeros_counter = sum([most_common[i][bit] == "0" for i in range(len(most_common))])
    ones_counter = sum([most_common[i][bit] == "1" for i in range(len(most_common))])
    if len(most_common) > 1:
        most_common = [num for num in most_common if int(num[bit]) == (ones_counter >= zeros_counter)]

    zeros_counter = sum([least_common[i][bit] == "0" for i in range(len(least_common))])
    ones_counter = sum([least_common[i][bit] == "1" for i in range(len(least_common))])
    if len(least_common) > 1:
        least_common = [num for num in least_common if int(num[bit]) == (ones_counter < zeros_counter)]

result2 = int(most_common[0], 2) * int(least_common[0], 2)
print(result2)  # 903810
