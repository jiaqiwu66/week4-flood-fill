from typing import List

directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]


def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    """Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str])
        old (str): Value to be replaced
        new (str): Value that replaces the old
        x (int): X-coordinate of the flood start point
        y (int): Y-coordinate of the flood start point
    Returns:
        List[str]: Modified board
    """

    # Implement your code here.
    row = len(input_board)
    col = len(input_board[0])

    board_arr = []
    for line in input_board:
        board_arr.append(list(line))

    if (not (0 <= x < row and 0 <= y < col)) or board_arr[x][y] != old:
        return input_board

    dfs(board_arr, x, y, row, col, old, new)

    res = []
    for line in board_arr:
        res.append("".join(line))

    return res


def dfs(board_arr: List[List[str]], x: int, y: int, row: int, col: int, old: str, new: str):
    board_arr[x][y] = new
    for direct in directions:
        x_ = x + direct[0]
        y_ = y + direct[1]
        if 0 <= x_ < row and 0 <= y_ < col and board_arr[x_][y_] == old:
            dfs(board_arr, x_, y_, row, col, old, new)


board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]

modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for a in modified_board:
    print(a)

# Expected output:
# ......................
# ......##########......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#####..
# ....###~~~~~~~~~~~~#..
# ....#~~~~~~~~~~~~###..
# ....##############....
