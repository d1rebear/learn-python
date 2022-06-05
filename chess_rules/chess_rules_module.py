import re
from chess_rules.rules_moves import chess_pawn, chess_rook, chess_bishop, chess_knight, chess_queen, chess_king


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
    regular_letter_search = r'([A-Za-z])'
    search_position_letter = re.search(regular_letter_search, position_input)
    if not re.match(r'([A-Ha-h])', position_input):
        print(f'The figure is not on the board')
        return False
    ord_position_letter = ord(search_position_letter[0])
    search_position_digit = re.search(r'\d', position_input)
    ord_position_digit = ord(search_position_digit[0])
    if 48 < ord_position_digit < 57:
        pass
    else:
        print(f'The figure is not on the board')
        return False
    position = ord_position_letter + ord_position_digit * 10
    if 555 <= position <= 632:
        pass
    else:
        print(f'The figure is not on the board')
        return False
    # handling move
    search_move_letter = re.search(regular_letter_search, move_input)
    if not re.match(r'([A-Ha-h])', move_input):
        print(f'Move is out of the board')
        return False
    ord_move_letter = ord(search_move_letter[0])
    search_move_digit = re.search(r'\d', move_input)
    ord_move_digit = ord(search_move_digit[0])
    if 48 < ord_move_digit < 57:
        pass
    else:
        print(f'Move is out of the board')
        return False
    move = ord_move_letter + ord_move_digit * 10
    move_position_diff = move - position
    if 555 <= move <= 632:
        pass
    else:
        print(f'Move is out of the board')
        return False
    if figure_name == 'PAWN':
        return chess_pawn(position, move_position_diff)
    elif figure_name == 'ROOK':
        return chess_rook(move_position_diff)
    elif figure_name == 'BISHOP':
        return chess_bishop(move, position, move_position_diff)
    elif figure_name == 'KNIGHT':
        return chess_knight(move_position_diff)
    elif figure_name == 'QUEEN':
        return chess_queen(move, position, move_position_diff)
    elif figure_name == 'KING':
        return chess_king(move_position_diff)
    else:
        print(f' No such figure exists')
        return False

