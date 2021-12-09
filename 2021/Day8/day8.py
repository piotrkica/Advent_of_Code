with open("day8.txt") as file:
    lines = file.readlines()

digit_counter_map = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
total_sum = 0


def parse_line(line):
    input_, output = line.split('|')
    input_ = input_.split(' ')
    output = output.split(' ')
    input_.remove('')
    output.remove('')
    output[-1] = output[-1].replace("\n", "")
    return input_, output


for line in lines:
    codes, coded_number = parse_line(line)
    codes.sort(key=lambda x: len(x))

    digits_map = dict()
    digits_map[1] = set(codes[0])
    digits_map[7] = set(codes[1])
    digits_map[4] = set(codes[2])
    digits_map[8] = set(codes[9])

    codes_of_2_3_5 = [set(segment) for segment in codes if len(segment) == 5]
    digits_map[3] = [x for x in codes_of_2_3_5 if digits_map[1].issubset(x)][0]
    codes_of_2_3_5.remove(digits_map[3])
    digits_map[5] = [x for x in codes_of_2_3_5 if (digits_map[4] - digits_map[1]).issubset(x)][0]
    codes_of_2_3_5.remove(digits_map[5])
    digits_map[2] = codes_of_2_3_5[0]

    codes_of_0_6_9 = [set(segment) for segment in codes if len(segment) == 6]
    digits_map[0] = [x for x in codes_of_0_6_9 if not (digits_map[4] - digits_map[1]).issubset(x)][0]
    codes_of_0_6_9.remove(digits_map[0])
    digits_map[9] = [x for x in codes_of_0_6_9 if digits_map[1].issubset(x)][0]
    codes_of_0_6_9.remove(digits_map[9])
    digits_map[6] = codes_of_0_6_9[0]

    output_decoded = 0
    digit = coded_number[0]
    for i, digit in enumerate(coded_number[::-1]):
        for k, v in digits_map.items():
            if set(digit) == set(v):
                output_decoded += 10 ** i * k
                digit_counter_map[k] += 1

    total_sum += output_decoded

result = digit_counter_map[1] + digit_counter_map[4] + digit_counter_map[7] + digit_counter_map[8]
print(result)

result2 = total_sum
print(result2)
