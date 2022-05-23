import re
from rules_moves import chess_pawn, chess_rook, chess_bishop, chess_knight, chess_queen, chess_king

# pawn, rook, knight, bishop, queen, king

figure = str(input()).capitalize()
position_input = str(input()).upper()
move_input = str(input()).upper()

# handling position
regular_letter_search = r'([A-Za-z])'
search_position_letter = re.search(regular_letter_search, position_input)
ord_position_letter = ord(search_position_letter[0])
search_position_digit = re.search('\d', position_input)
ord_position_digit = ord(search_position_digit[0])
position = ord_position_letter + ord_position_digit * 10

if 555 <= position <= 632:
    pass
else:
    exit(f'The figure is not on the board')

# handling move
search_move_letter = re.search(regular_letter_search, move_input)
ord_move_letter = ord(search_move_letter[0])
search_move_digit = re.search('\d', move_input)
ord_move_digit = ord(search_move_digit[0])
move = ord_move_letter + ord_move_digit * 10

if 555 <= move <= 632:
    pass
else:
    exit(f'Move is out of the board')

move_position_diff = move - position
print(f'Moving "{figure}" from "{position_input}" to "{move_input}"')

if figure == 'Pawn':
    chess_pawn(position, move_position_diff)
elif figure == 'Rook':
    chess_rook(move_position_diff)
elif figure == 'Bishop':
    chess_bishop(move_position_diff)
elif figure == 'Knight':
    chess_knight(move_position_diff)
elif figure == 'Queen':
    chess_queen(move, position, move_position_diff)
elif figure == 'King':
    chess_king(move_position_diff)
else:
    exit(f'No such figure exists')

