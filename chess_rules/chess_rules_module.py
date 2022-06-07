import re
from chess_rules.rules import chess_pawn, chess_rook, chess_bishop, chess_knight, chess_queen, chess_king


def is_figure_movable(figure_name, position_input, move_input):
    if not position_input[1].isdigit():
        print('Invalid [1] of "position": must be digit [1-8] ')
        return False
    elif not position_input[0].isalpha():
        print('Invalid [0] of "position: must be letter [A-H]"')
        return False
    if not move_input[1].isdigit():
        print('Invalid [1] of ''move'': must be digit [1-8]')
        return False
    elif not move_input[0].isalpha():
        print('Invalid [0] of "move": must be letter [A-H]')
        return False
    if not re.match(r'([A-Ha-h])', position_input):
        print(f'The figure is not on the board')
        return False
    if not re.match(r'([A-Ha-h])', move_input):
        print(f'Move is out of the board')
        return False
    board = [
        ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1'],
        ['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2'],
        ['A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3'],
        ['A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4'],
        ['A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5'],
        ['A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6'],
        ['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7'],
        ['A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8'],
    ]
    pos_x = 0
    pos_y = 0
    move_x = 0
    move_y = 0
    for i in board:
        try:
            pos_y = i.index(position_input)
        except ValueError:
            pos_y = -1
        if pos_y != -1:
            break
        pos_x += 1
    for i in board:
        try:
            move_y = i.index(move_input)
        except ValueError:
            move_y = -1
        if move_y != -1:
            break
        move_x += 1
    index_position_x = pos_x + 1
    index_position_y = pos_y + 1
    index_move_x = move_x + 1
    index_move_y = move_y + 1
    if index_position_x > 8 or index_position_x == 0 or index_position_y > 8 or index_position_y == 0:
        print(f'The figure is not on the board')
        return False
    if index_move_x > 8 or index_move_x == 0 or index_move_y > 8 or index_move_y == 0:
        print(f'Move is out of board')
        return False

    if figure_name == 'PAWN':
        return chess_pawn(index_position_x, index_position_y, index_move_x, index_move_y)
    elif figure_name == 'ROOK':
        return chess_rook(index_position_x, index_position_y, index_move_x, index_move_y)
    elif figure_name == 'BISHOP':
        return chess_bishop(index_position_x, index_position_y, index_move_x, index_move_y)
    elif figure_name == 'KNIGHT':
        return chess_knight(index_position_x, index_position_y, index_move_x, index_move_y)
    elif figure_name == 'QUEEN':
        return chess_queen(index_position_x, index_position_y, index_move_x, index_move_y)
    elif figure_name == 'KING':
        return chess_king(index_position_x, index_position_y, index_move_x, index_move_y)
    else:
        print(f' No such figure exists')
        return False
