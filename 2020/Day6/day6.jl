lines = readlines("2020/Day6/day6.txt")

function count_answers_anyone(answers)
    counter = 0
    uniq = Set()
    for ans in answers
        if ans == ""
            counter += length(uniq)
            uniq = Set()
        else
            uniq = union(uniq, Set(ans))
        end
    end
    counter += length(uniq)

    return counter
end

function count_answers_everyone(answers)
    counter = 0
    uniq = Set(answers[1])
    for (i, ans) in enumerate(answers)
        if ans == ""
            counter += length(uniq) 
            uniq = Set(answers[i+1])
        else
            uniq = intersect(uniq, Set(ans))
        end
    end
    counter += length(uniq)

    return counter
end

println(count_answers_anyone(lines))  # 6775
println(count_answers_everyone(lines))  # 3356