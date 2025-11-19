def print_board(board):
    for r in range(9):
        if r % 3 == 0 and r != 0:
            print("- - - - - - - - - - -")
        for c in range(9):
            if c % 3 == 0 and c != 0:
                print(" | ", end="")
            print(board[r][c] if board[r][c] != 0 else ".", end=" ")
        print()


def is_valid(board, row, col, num):
    # Revisar fila
    for c in range(9):
        if board[row][c] == num and c != col:
            return False

    # Revisar columna
    for r in range(9):
        if board[r][col] == num and r != row:
            return False

    # Revisar subcuadrante 3x3
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num and (r, c) != (row, col):
                return False

    return True


def find_empty(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    return None


def solve(board):
    empty = find_empty(board)
    if not empty:
        return True  # Resuelto
    row, col = empty

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0  # Backtracking

    return False


#============================================================
#                   BOARDS DEL USUARIO
#============================================================

board1_original = [
    [5,0,0, 9,1,3, 7,2,0],
    [3,0,0, 0,8,0, 5,0,9],
    [0,9,0, 2,5,0, 0,8,0],

    [6,8,0, 4,7,0, 2,3,0],
    [0,0,9, 5,0,0, 4,6,0],
    [7,0,4, 0,0,0, 0,0,5],

    [0,2,0, 0,0,0, 0,0,0],
    [4,0,0, 8,9,1, 6,0,0],
    [8,5,0, 7,2,0, 0,0,3]
]


board2_original = [
    [6,9,0, 0,0,0, 7,0,0],
    [0,0,0, 0,9,6, 0,0,0],
    [0,8,0, 7,5,3, 0,9,0],

    [0,2,0, 3,7,4, 5,6,1],
    [3,6,0, 0,0,5, 0,2,0],
    [0,0,0, 9,6,0, 3,7,8],

    [0,0,6, 0,3,1, 0,8,4],
    [0,4,5, 8,0,7, 6,0,0],
    [0,0,0, 0,0,0, 0,5,7]
]



#============================================================
#                   EJECUCIÓN PARA AMBOS
#============================================================

import copy

for i, original in enumerate([board1_original, board2_original], start=1):
    board = copy.deepcopy(original)
    print(f"\n==========================")
    print(f"SUDOKU {i} ORIGINAL")
    print("==========================")
    print_board(board)

    if solve(board):
        print(f"\n✔ SUDOKU {i} RESUELTO:")
        print_board(board)
    else:
        print(f"\n❌ Sudoku {i} no tiene solución válida.")
