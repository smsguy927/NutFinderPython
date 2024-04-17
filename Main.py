from typing import Final
import itertools

def is_different(arr1, arr2):
    for x, y in zip(arr1, arr2):
        if x != y:
            return True
    return False


def calc_gap(left, right):
    return abs(left - right) - 1


def calc_gaps(arr):
    total_gaps = 0
    for i in range(len(arr) - 1):
        total_gaps += calc_gap(arr[i], arr[i + 1])
    print(f"Arr: {arr} Total gaps: {total_gaps}")
    return total_gaps


def calc_gap_sizes(arr):
    gap_sizes = []
    for i in range(len(arr) - 1):
        gap_sizes.append(calc_gap(arr[i], arr[i + 1]))
    return gap_sizes


def find_nut_straight(min_rank, max_rank, board):
    straights = []
    if min_rank > max_rank:
        raise ValueError(f"{min_rank} cannot be greater than {max_rank}")
    if max_rank < min_rank:
        raise ValueError(f"{max_rank} cannot be less than {min_rank}")
    if abs(max_rank - min_rank) < 3:
        return straights
    any_rank: Final[int] = 0
    board.sort(reverse=True)
    board_gaps = calc_gap_sizes(board)
    print(board_gaps)
    result = []

    if max(board_gaps) == 0:
        if board[0] == max_rank:
            result.append(any_rank)
        else:
            result.append(board[0] + 1)
        result.append(any_rank)
    elif board_gaps.count(0) == 3 and (board_gaps[0] != 0 or board_gaps[3] != 0):
        if board_gaps[0] == 0 and board[0] == max_rank:
            result.append(board[3] - 1)
        else:
            result.append(board[0] + 1)
        result.append(any_rank)
    elif board_gaps[0] == 0 and board_gaps[1] == 0:
        pass

    return result


def generate_combos(arr, length):
    return list(itertools.combinations(arr, 5))


def main():
    print("Starting program...")
    all_ranks = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    all_cases = generate_combos(all_ranks, 5)
    for case in all_cases:
        print(case)
        print(find_nut_straight(2, 14, list(case)))


main()
