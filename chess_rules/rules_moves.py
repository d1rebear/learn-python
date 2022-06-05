def chess_pawn(position, move_position_diff):
    if move_position_diff == 10:
        print(f'The "Pawn" has a move')
        return True
    elif 555 <= position <= 572:
        if move_position_diff == 20 or move_position_diff == 10:
            print(f'The "Pawn" has a move')
            return True
        else:
            print(f'The "Pawn" cannot move!')
            return False
    else:
        print(f'The "Pawn" cannot move!')
        return False


def chess_rook(move_position_diff):
    if move_position_diff % 10 == 0:
        print(f'The "Rook" has a move')
        return True
    elif -7 <= move_position_diff <= 7:
        print(f'The "Rook" has a move')
        return True
    else:
        print(f'The "Rook" cannot move!')
        return False


def chess_bishop(move, position, move_position_diff):
    if move_position_diff % 9 == 0 or move_position_diff % 11 == 0:
        if (position == 555 and move == 591) or (position == 565 and move == 601) or (
                position == 575 and move == 611):
            print(f'The "Bishop" cannot move!')
            return False
        elif (position == 585 and move == 621) or (position == 595 and move == 631) or (
                position == 556 and move == 592):
            print(f'The "Bishop" cannot move!')
            return False
        elif (position == 566 and move == 602) or (position == 576 and move == 612) or (
                position == 586 and move == 622):
            print(f'The "Bishop" cannot move!')
            return False
        elif position == 596 and move == 632:
            print(f'The "Bishop" cannot move!')
            return False
        else:
            print(f'The "Bishop" has a move')
            return True
    else:
        print(f'The "Bishop" cannot move!')
        return False


def chess_knight(move_position_diff):
    if move_position_diff == 21 or move_position_diff == -21 or move_position_diff == 12 or move_position_diff == -12:
        print(f'The "Knight" has a move')
        return True
    elif move_position_diff == 19 or move_position_diff == -19 or move_position_diff == 8 or move_position_diff == -8:
        print(f'The "Knight" has a move')
        return True
    else:
        print(f'The "Knight" cannot move!')
        return False


def chess_queen(move, position, move_position_diff):
    if move_position_diff % 10 == 0:
        print(f'The "Queen" has a move')
        return True
    elif -7 <= move_position_diff <= 7:
        print(f'The "Queen" has a move')
        return True
    elif move_position_diff % 9 == 0 or move_position_diff % 11 == 0:
        if (position == 555 and move == 591) or (position == 565 and move == 601) or (
                position == 575 and move == 611):
            print(f'The "Queen" cannot move!')
            return False
        elif (position == 585 and move == 621) or (position == 595 and move == 631) or (
                position == 556 and move == 592):
            print(f'The "Queen" cannot move!')
            return False
        elif (position == 566 and move == 602) or (position == 576 and move == 612) or (
                position == 586 and move == 622):
            print(f'The "Queen" cannot move!')
            return False
        elif position == 596 and move == 632:
            print(f'The "Queen" cannot move!')
            return False
        else:
            print(f'The "Queen" has a move')
            return True
    else:
        print(f'The "Queen" cannot move!')
        return False


def chess_king(move_position_diff):
    if move_position_diff == 10 or move_position_diff == -10 or \
            move_position_diff == 1 or move_position_diff == -1:
        print(f'The "King" has a move')
        return True
    elif move_position_diff == 9 or move_position_diff == -9 or \
            move_position_diff == 11 or move_position_diff == -11:
        print(f'The "King" has a move')
        return True
    else:
        print(f'The "King" cannot move!')
        return False
