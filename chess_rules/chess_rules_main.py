from chess_rules import chess_rules_module

# pawn, rook, knight, bishop, queen, king

figure_name = str(input()).upper().strip()
# figure_name = figure_input.upper()
position_input = str(input()).upper()
move_input = str(input()).upper()
print(chess_rules_module.is_figure_movable(figure_name, position_input, move_input))
print(f' {figure_name}, {position_input},{move_input}')

