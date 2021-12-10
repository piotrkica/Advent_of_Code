lines = readlines("2020/Day2/day2.txt")

function parse_line(line)
    reg = r"(\d+)-(\d+) (\w): (\w+)"
    m = match(reg, line)
    min_ = parse(Int64, m.captures[1])
    max_ = parse(Int64, m.captures[2])
    chr  = m.captures[3]
    str  = m.captures[4]
    return min_, max_, chr, str
end

function count_valid_passwords(lines)
    valid_count = 0
    for line in lines
        min_, max_, chr, str = parse_line(line)
        if (min_ <= count(chr, str) <= max_)
            valid_count += 1
        end
    end
    return valid_count
end

result = count_valid_passwords(lines)
println(result)  # 524


function count_valid_passwords2(lines)
    valid_count = 0
    for line in lines
        i, j, chr, str = parse_line(line)
        chr = chr[1]  # [1] means substring to char conversion
        if str[i] == chr && str[j] != chr || str[i] != chr && str[j] == chr 
            valid_count += 1
        end
    end
    return valid_count
end

result = count_valid_passwords2(lines)
println(result)  # 485