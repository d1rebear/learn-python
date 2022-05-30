import re
from chess_rules.rules_moves import chess_pawn, chess_rook, chess_bishop, chess_knight, chess_queen, chess_king


def is_figure_movable(figure, position_input, move_input):
    regular_letter_search = r'([A-Za-z])'
    search_position_letter = re.search(regular_letter_search, position_input)
    ord_position_letter = ord(search_position_letter[0])
    search_position_digit = re.search(r'\d', position_input)
    ord_position_digit = ord(search_position_digit[0])
    position = ord_position_letter + ord_position_digit * 10
    if 555 <= position <= 632:
        pass
    else:
        print(f'The figure is not on the board')
        return False
    # handling move
    search_move_letter = re.search(regular_letter_search, move_input)
    ord_move_letter = ord(search_move_letter[0])
    search_move_digit = re.search(r'\d', move_input)
    ord_move_digit = ord(search_move_digit[0])
    move = ord_move_letter + ord_move_digit * 10
    move_position_diff = move - position
    if 555 <= move <= 632:
        pass
    else:
        print(f'Move is out of the board')
        return False
    if figure == 'PAWN':
        return chess_pawn(position, move_position_diff)
    elif figure == 'ROOK':
        return chess_rook(move_position_diff)
    elif figure == 'BISHOP':
        return chess_bishop(move, position, move_position_diff)
    elif figure == 'KNIGHT':
        return chess_knight(move_position_diff)
    elif figure == 'QUEEN':
        return chess_queen(move, position, move_position_diff)
    elif figure == 'KING':
        return chess_king(move_position_diff)
    else:
        exit(f'No such figure exists')
