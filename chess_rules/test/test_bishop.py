import pytest
from chess_rules.chess_rules_module import is_figure_movable

testdata_valid = [
    ('BISHOP', 'A1', 'H8'),
    ('BISHOP', 'H1', 'A8'),
    ('BISHOP', 'C3', 'E1'),
    ('BISHOP', 'F5', 'G6'),
    ('BISHOP', 'A4', 'C2'),
    ('BISHOP', 'B2', 'C3'),
    ('BISHOP', 'E7', 'F8'),
    ('BISHOP', 'C4', 'F7'),
    ('BISHOP', 'D1', 'F3'),
    ('BISHOP', 'G2', 'B7'),
]
testdata_invalid = [
    ('BISHOP', 'A1', 'A8'),
    ('BISHOP', 'A1', 'H7'),
    ('BISHOP', 'A1', 'C2'),
    ('BISHoP', 'A1', 'A8'),
    ('bishOp', 'E3', 'C5'),
    ('BISHOP', 'I7', 'K8'),
    ('BISHOP', 'H1', 'N8'),
    ('BiShOP', 'B4', 'C5'),
    ('BISHOp', 'D3', 'C4'),
    ('BISHOP', '11', 'AA'),
]

class TestBishop:
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