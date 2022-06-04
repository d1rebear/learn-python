import pytest
from chess_rules.chess_rules_module import is_figure_movable

testdata_valid = [
    ('ROOK', 'A1', 'A8'),
    ('ROOK', 'A1', 'H1'),
    ('ROOK', 'H1', 'A1'),
    ('ROOK', 'C2', 'C7'),
    ('ROOK', 'B6', 'D6'),
    ('ROOK', 'F7', 'B7'),
    ('ROOK', 'G8', 'H8'),
    ('ROOK', 'E3', 'F3'),
    ('ROOK', 'D1', 'E1'),
    ('ROOK', 'H5', 'A5')
]

testdata_invalid = [
    ('ROOK', 'A1', 'H8'),
    ('ROOK', 'D1', 'A3'),
    ('RO0K', 'E1', 'E3'),
    ('ROOK', 'M1', 'A8'),
    ('RrOOK', 'A2', 'A8'),
    ('ROOK', 'D6', 'J6'),
    ('ROOK', 'V1', 'V8'),
    ('ROOK', 'B8', 'F3'),
    ('RoOk', 'E1', 'E4'),
    ('rOoK', 'G5', 'G6'),
]


class TestRook:
    @staticmethod
    @pytest.mark.parametrize("figure_name, start_position, end_position",
                             testdata_valid)
    def test_valid_move(figure_name, start_position, end_position):
        assert is_figure_movable(figure_name,
                                 position_input=start_position,
                                 move_input=end_position)

    @staticmethod
    @pytest.mark.parametrize("figure_name, start_position, end_position",
                             testdata_invalid)
    def test_invalid_move(figure_name, start_position, end_position):
        assert not is_figure_movable(figure_name,
                                 position_input=start_position,
                                 move_input=end_position)
