from chess_rules import chess_rules_module

# pawn, rook, knight, bishop, queen, king

figure = str(input()).upper()
position_input = str(input()).upper()
move_input = str(input()).upper()
print(chess_rules_module.is_figure_movable(figure, position_input, move_input))
print(f' {figure}, {position_input},{move_input}')

