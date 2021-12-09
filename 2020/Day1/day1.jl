numbers = readlines("2020/Day1/day1.txt")
numbers = sort(map(x -> parse(Int64, x), numbers))

function find1(numbers)
    i = 1
    j = length(numbers)
    while i != j
        if numbers[i] + numbers[j] == 2020
            return numbers[i] * numbers[j]
        elseif numbers[i] + numbers[j] < 2020
            i += 1
        else
            j -= 1
        end
    end
end

result = find1(numbers)
println(result)  # 326211



function find2(numbers)
    for k in 1:length(numbers)
        i = k + 1
        j = length(numbers)
        while i != j
            if numbers[i] + numbers[j] == 2020 - numbers[k]
                return numbers[i] * numbers[j] * numbers[k]
            elseif numbers[i] + numbers[j] < 2020 - numbers[k]
                i += 1
            else
                j -= 1
            end
        end
    end
end

result2 = find2(numbers)
println(result2)  # 131347190
