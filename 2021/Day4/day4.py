import numpy as np

with open("day4.txt") as file:
    lines = file.readlines()
    lines = [(line.rstrip()) for line in lines]

size = 5
bingo_nums = list(map(lambda x: int(x), lines[0].split(",")))
lines = lines[1:]


def parse_bingo_lines(lines):
    bingo_boards = []
    for line in lines:
        if line == '':
            bingo_boards.append([])
        else:
            bingo_row = line.split(" ")
            bingo_row = list(filter(lambda x: x != "", bingo_row))
            bingo_row = list(map(lambda x: int(x), bingo_row))
            bingo_boards[-1].append(bingo_row)

    return bingo_boards


def play_bingo_winner_board(bingo_nums, bingo_boards):
    for num in bingo_nums:
        for board in bingo_boards:
            for row in board:
                if num in row:
                    row[row.index(num)] = -1

        for board in bingo_boards:
            for i in range(size):
                row = board[i]
                if row.count(-1) == size:
                    return num, board
                column = [board[row][i] for row in range(size)]
                if column.count(-1) == size:
                    return num, board


bingo_boards = parse_bingo_lines(lines)
last_num, winning_set = play_bingo_winner_board(bingo_nums, bingo_boards)
result = last_num * (np.sum(winning_set) + np.count_nonzero(np.array(winning_set) == -1))
print(result)  # 89001


def play_bingo_loser_board(bingo_nums, bingo_boards):
    for num in bingo_nums:
        for board in bingo_boards:
            for row in board:
                if num in row:
                    row[row.index(num)] = -1

        for board in bingo_boards:
            for i in range(size):
                row = board[i]
                if row.count(-1) == size:
                    if len(bingo_boards) == 1:
                        return num, board
                    else:
                        bingo_boards.remove(board)
                        break
                column = [board[row][i] for row in range(size)]
                if column.count(-1) == size:
                    if len(bingo_boards) == 1:
                        return num, board
                    else:
                        bingo_boards.remove(board)
                        break


last_num, winning_set = play_bingo_loser_board(bingo_nums, bingo_boards)
result2 = last_num * (np.sum(winning_set) + np.count_nonzero(np.array(winning_set) == -1))
print(result2)  # 7296
