import pytest
from chess_rules.chess_rules_module import is_figure_movable


class TestPawn:
    @staticmethod
    @pytest.mark.parametrize("figure_name,start_position,end_position",
                             [('PAWN', 'A1', 'A2'),
                              ('PAWN', 'A1', 'A3')])
    def test_valid_move(figure_name, start_position, end_position):
        assert is_figure_movable(figure=figure_name,
                                 position_input=start_position,
                                 move_input=end_position)

    @staticmethod
    @pytest.mark.parametrize("figure_name,start_position,end_position",
                             [('PAWN', 'A1', 'A4'),
                              ('PAWN', 'A1', 'A5')])
    def test_invalid_move(figure_name, start_position, end_position):
        assert not is_figure_movable(figure=figure_name,
                                     position_input=start_position,
                                     move_input=end_position)
