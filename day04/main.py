import numpy
from utils import utils


def create_boards(data):
    boards = []
    board_line = 0
    board = numpy.empty([5, 5], dtype=int)

    for line in data:
        if not line:
            boards.append(board)
            board = numpy.empty([5, 5], dtype=int)
            board_line = 0
        else:
            board[board_line] = line.split()
            board_line += 1

    boards.append(board)
    marked = [numpy.full([5, 5], False, dtype=bool) for _ in boards]

    return boards, marked


def check_board(board, marked, value):
    indexes = numpy.concatenate(numpy.where(board == value))

    if len(indexes):
        marked[indexes[0]][indexes[1]] = True


def is_board_win(marked):
    return len(numpy.where(marked.all(axis=1))[0]) or len(numpy.where(marked.all(axis=0))[0])


def play_bingo(boards, marked, draws):
    boards_finished = []
    numbers_drawn_after_win = []
    number_boards = len(boards)

    for draw in draws:
        for b in range(0, number_boards):
            if b in boards_finished:
                continue

            if not is_board_win(marked[b]):
                check_board(boards[b], marked[b], draw)

            if is_board_win(marked[b]):
                boards_finished.append(b)

        if len(boards_finished):
            numbers_drawn_after_win.append(draw)

        if len(boards_finished) == number_boards:
            break

    return boards_finished[0], numbers_drawn_after_win[0], boards_finished[-1], numbers_drawn_after_win[-1]


def calc_score(winning_board, winning_marked, last_draw):
    index_where = numpy.where(~winning_marked)
    indexes = list(zip(index_where[0], index_where[1]))
    win_sum = 0

    for index_tuple in indexes:
        win_sum += winning_board[index_tuple[0]][index_tuple[1]]

    return win_sum * last_draw


def play(data):
    draws = list(map(int, data[0].split(',')))
    data = numpy.delete(data, [0, 1])
    boards, marked = create_boards(data)

    winning, winning_draw, last_winning, last_draw = play_bingo(boards, marked, draws)

    score = calc_score(boards[winning], marked[winning], winning_draw)
    last_score = calc_score(boards[last_winning], marked[last_winning], last_draw)

    return score, last_score


example_data, input_data = utils.get_data("04")

example_score, example_last_score = play(example_data)
input_score, input_last_score = play(input_data)

print("## Part 1 ##")
print(f"Answer: {example_score}")
print(f"Answer: {input_score}\n")

print("## Part 2 ##")
print(f"Answer: {example_last_score}")
print(f"Answer: {input_last_score}\n")
