with open("day6.txt") as file:
    lines = file.readlines()

ages = lines[0].split(",")
ages = list(map(lambda x: int(x), ages))


def simulate(ages, days):
    val_counts = [ages.count(val) for val in range(9)]
    for day in range(days):
        newborn = val_counts[0]
        for i in range(len(val_counts) - 1):
            val_counts[i] = val_counts[i + 1]
        val_counts[-1] = newborn
        val_counts[6] += newborn  # add no. parents
    return sum(val_counts)


result = simulate(ages, 80)
print(result)  # 350149

result2 = simulate(ages, 256)
print(result2)  # 1590327954513
