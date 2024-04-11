from typing import Final


def is_different(arr1, arr2):
    for x, y in zip(arr1, arr2):
        if x != y:
            return True
    return False


def calc_gaps(arr):
    total_gaps = 0
    for i in range(len(arr) - 1):
        total_gaps += abs(arr[i] - arr[i + 1]) - 1
    print(f"Arr: {arr} Total gaps: {total_gaps}")
    return total_gaps


def find_straights(min_rank, max_rank, board):
    straights = []
    if min_rank > max_rank:
        raise ValueError(f"{min_rank} cannot be greater than {max_rank}")
    if max_rank < min_rank:
        raise ValueError(f"{max_rank} cannot be less than {min_rank}")
    if abs(max_rank - min_rank) < 3:
        return straights

    board.sort(reverse=True)
    straight_groups = []
    max_gaps: Final[int] = 2
    max_index: Final[int] = len(board) - 1
    straight_size: Final[int] = 3
    i = 0
    current_start = 0
    potential_straight = []
    while i < len(board):
        if len(potential_straight) == 0 or potential_straight[-1] != board[i]:
            potential_straight.append(board[i])
            if (len(potential_straight) == straight_size and calc_gaps(potential_straight) <= max_gaps and
                    (len(straight_groups) == 0 or is_different(potential_straight, straight_groups[-1]))):
                straight_groups.append(potential_straight)
            if len(potential_straight) == straight_size:
                potential_straight = []
                current_start += 1
                i = current_start - 1
        i += 1
    print(straight_groups)


def main():
    print("Starting program...")
    try:
        find_straights(0, 50, [35, 33, 31, 27, 21, 20, 19, 17, 13, 10, 9, 8, 7, 6, 2, 1, 0])
    except ValueError as e:
        print(e)


main()
