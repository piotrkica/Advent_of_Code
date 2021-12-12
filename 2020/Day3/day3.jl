lines = readlines("2020/Day3/day3.txt")

function count_trees(lines)
    size_x = length(lines[1])
    counter = 0
    x_pos = 1
    for line in lines
        counter += line[x_pos] == '#'
        x_pos = (x_pos + 2) % size_x + 1 
    end
    return counter
end

result = count_trees(lines)
println(result)  # 205

function count_trees2(lines)
    size_x = length(lines[1])
    counter_r1, counter_r3, counter_r5, counter_r7, counter_d2 = 0, 0, 0, 0, 0
    x_pos1, x_pos3, x_pos5, x_pos7, x_pos1_d2 = 1, 1, 1, 1, 1
    
    for line in lines
        counter_r1 += line[x_pos1] == '#'
        x_pos1 = x_pos1 % size_x + 1 

        counter_r3 += line[x_pos3] == '#'
        x_pos3 = (x_pos3 + 2) % size_x + 1 

        counter_r5 += line[x_pos5] == '#'
        x_pos5 = (x_pos5 + 4) % size_x + 1 

        counter_r7 += line[x_pos7] == '#'
        x_pos7 = (x_pos7 + 6) % size_x + 1 
    end

    for i in 1:2:length(lines)
        line = lines[i]
        counter_d2 += line[x_pos1_d2] == '#'
        x_pos1_d2 = x_pos1_d2 % size_x + 1 
    end
    
    return counter_r1 * counter_r3 * counter_r5 * counter_r7 * counter_d2
end

result2 = count_trees2(lines)
println(result2)  # 3952146825