def chess_pawn(index_position_x, index_position_y, index_move_x, index_move_y):
    if index_position_y == index_move_y and index_move_x - index_position_x == 1:
        print(f'Pawn has a move!')
        return True
    elif index_position_x == 2 and index_position_y in range(1, 9):
        if index_position_y == index_move_y and index_move_x - index_position_x == (2 or 1):
            print(f'Pawn has a move!')
            return True
        else:
            print(f'Pawn cannot move!')
            return False
    else:
        print(f'Pawn cannot move!')
        return False


def chess_rook(index_position_x, index_position_y, index_move_x, index_move_y):
    if index_position_y == index_move_y and abs(index_move_x - index_position_x) in range(1, 8):
        print(f'Rook has a move!')
        return True
    elif index_move_x == index_position_x and abs(index_move_y - index_position_y) in range(1, 8):
        print(f'Rook has a move!')
        return True
    else:
        print(f'Rook cannot move!')
        return False


def chess_bishop(index_position_x, index_position_y, index_move_x, index_move_y):
    if abs(index_move_y - index_position_y) in range(1, 8) and abs(index_move_x - index_position_x) in range(1, 8):
        if abs(index_move_y - index_position_y) == abs(index_move_x - index_position_x):
            print(f'Bishop has a move!')
            return True
        else:
            print(f'Bishop cannot move!')
            return False
    else:
        print(f'Bishop cannot move!')
        return False


def chess_knight(index_position_x, index_position_y, index_move_x, index_move_y):
    if abs(index_position_x - index_move_x) == 2 and abs(index_position_y - index_move_y) == 1:
        print(f'Knight has a move!')
        return True
    elif abs(index_position_x - index_move_x) == 1 and abs(index_position_y - index_move_y) == 2:
        print(f'Knight has a move')
        return True
    else:
        print(f'Knight cannot move!')
        return False


def chess_queen(index_position_x, index_position_y, index_move_x, index_move_y):
    if index_position_y == index_move_y and abs(index_move_x - index_position_x) in range(1, 8):
        print(f'Queen has a move!')
        return True
    elif index_move_x == index_position_x and abs(index_move_y - index_position_y) in range(1, 8):
        print(f'Queen has a move!')
        return True
    elif abs(index_move_y - index_position_y) in range(1, 8) and abs(index_move_x - index_position_x) in range(1, 8):
        if abs(index_move_y - index_position_y) == abs(index_move_x - index_position_x):
            print(f'Queen has a move!')
            return True
        else:
            print(f'Queen cannot move!')
            return False
    else:
        print(f'Queen cannot move!')
        return False


def chess_king(index_position_x, index_position_y, index_move_x, index_move_y):
    if abs(index_move_x - index_position_x) == 1 and index_move_y == index_position_y:
        print(f'King has a move!')
        return True
    elif abs(index_move_x - index_position_x) == 1 and abs(index_move_y - index_position_y) == 1:
        print(f'King has a move!')
        return True
    elif index_move_x == index_position_x and abs(index_move_y - index_position_y) == 1:
        print(f'King has a move')
        return True
    else:
        print(f'King cannot move!')
        return False
