lines = readlines("2020/Day4/day4.txt")


function count_valid(lines)
    delims = findall(x->x=="", lines)
    start = 1
    push!(delims, length(lines) +1 )

    total = 0
    invalid_counter = 0
    required = ["byr", "ecl", "eyr", "hcl", "hgt", "iyr", "pid"]
    
    for delim in delims
        total += 1
        passport = lines[start:delim-1]
        start = delim + 1
        passport = join(sort(split(join(passport, " "), " ")), " ")

        for field in required
            if !occursin(field, passport)
                invalid_counter += 1
                break
            end
        end
    end
    return total - invalid_counter
end

result = count_valid(lines)
println(result)  # 233


function verify_field(field, passport)
    if field == "byr"
        reg = r".*byr:(\d+).*"
        m = match(reg, passport)
        val = parse(Int64, m.captures[1])
        return 1920 <= val <= 2002
    end

    if field == "iyr"
        reg = r".*iyr:(\d+).*"
        m = match(reg, passport)
        val = parse(Int64, m.captures[1])
        return 2010 <= val <= 2020
    end

    if field == "eyr"
        reg = r".*eyr:(\d+).*"
        m = match(reg, passport)
        val = parse(Int64, m.captures[1])
        return 2020 <= val <= 2030
    end

    if field == "hgt"
        reg1 = r".*hgt:(\d+)cm.*"
        reg2 = r".*hgt:(\d+)in.*"
        m1 = match(reg1, passport)
        m2 = match(reg2, passport)
        if m1 != nothing
            val = parse(Int64, m1.captures[1])
            return 150 <= val <= 193
        elseif m2 != nothing
            val = parse(Int64, m2.captures[1])
            return 59 <= val <= 76
        else
            return false
        end
    end

    if field == "hcl"
        reg = r".*hcl:#([\da-f]{6}).*"
        m = match(reg, passport)
        return m != nothing
    end

    if field == "ecl"
        reg = r".*ecl:([a-z]{3}).*"
        m = match(reg, passport)
        if m != nothing
            val = String(m.captures[1])
            colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            return val in colors
        end 
        return false
    end

    if field == "pid"
        reg = r".*pid:(\d{9})" 
        m = match(reg, passport)
        return m != nothing
    end

    return false
end

function count_valid2(lines)
    delims = findall(x->x=="", lines)
    start = 1
    push!(delims, length(lines) + 1)

    total = length(delims)
    invalid_counter = 0
    required = ["byr", "ecl", "eyr", "hcl", "hgt", "iyr", "pid"]
    
    for delim in delims
        passport = lines[start:delim-1]
        start = delim + 1
        passport = join(sort(split(join(passport, " "), " ")), " ")

        for field in required
            if !occursin(field, passport) || !verify_field(field, passport)
                invalid_counter += 1
                break
            end
        end
    end
    return total - invalid_counter
end

result2 = count_valid2(lines)
println(result2)  # 111