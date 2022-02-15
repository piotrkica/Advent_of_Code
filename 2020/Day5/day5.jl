lines = readlines("2020/Day5/day5.txt")

function decode_seat(seat_code)
    row_code = seat_code[1:7]
    row_code = replace(row_code, 'F' => 0, 'B' => 1)
    row = parse(Int, row_code, base=2)

    col_code = seat_code[8:10]
    col_code = replace(col_code, 'L' => 0, 'R' => 1)
    col = parse(Int, col_code, base=2)

    return row, col
end

function find_seat_id(seat_code)
    seat_loc = decode_seat(seat_code)
    seat_id = seat_loc[1] * 8 + seat_loc[2]
    
    return seat_id
end

function find_highest_seat(seat_codes)
    highest_id = -1
    for seat_code in seat_codes
        seat_id = find_seat_id(seat_code)
        highest_id = max(highest_id, seat_id)
    end

    return highest_id
end 

function find_missing_seat(seat_codes)
    highest_id = find_highest_seat(seat_codes)
    seat_ids = Set(1:highest_id)
    for seat_code in seat_codes
        seat_id = find_seat_id(seat_code)
        delete!(seat_ids, seat_id)
    end

    seat_ids = sort(collect(seat_ids))
    
    return seat_ids[length(seat_ids)]
end

println(find_highest_seat(lines))
println(find_missing_seat(lines))