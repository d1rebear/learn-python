import pytest
from chess_rules.chess_rules_module import is_figure_movable

testdata_valid = [
    ('KING', 'A1', 'B1'),
    ('KING', 'D5', 'C4'),
    ('KING', 'H1', 'H2'),
    ('KING', 'B4', 'A3'),
    ('KING', 'C5', 'D5'),
    ('KING', 'G7', 'G8'),
    ('KING', 'A8', 'B8'),
    ('KING', 'E2', 'D3'),
    ('KING', 'D6', 'E7'),
    ('KING', 'D6', 'E6'),
]
testdata_invalid = [
    ('KING', 'A1', 'A3'),
    ('KING', 'H1', 'E1'),
    ('KING', 'H1', 'A8'),
    ('KING', 'H1', 'H8'),
    ('KiNG', 'C5', 'D5'),
    ('kiNG', 'G7', 'B7'),
    ('KING', '22', 'D4'),
    ('KING', 'E4', '66'),
    ('KING', 'DD', 'A4'),
    ('KING', 'G2', 'CE'),
]


class TestKing:
    @staticmethod
    @pytest.mark.parametrize("figure_name, start_position, end_position", testdata_valid)
    def test_valid_move(figure_name, start_position, end_position):
        assert is_figure_movable(figure_name,
                                 position_input=start_position,
                                 move_input=end_position)

    @staticmethod
    @pytest.mark.parametrize("figure_name, start_position, end_position", testdata_invalid)
    def test_invalid_move(figure_name, start_position, end_position):
        assert not is_figure_movable(figure_name,
                                     position_input=start_position,
                                     move_input=end_position)
