import pytest
from chess_rules.chess_rules_module import is_figure_movable

testdata_valid = [
    ('QUEEN', 'A1', 'H8'),
    ('QUEEN', 'A1', 'A8'),
    ('QUEEN', 'H1', 'A8'),
    ('QUEEN', 'H1', 'H8'),
    ('QUEEN', 'C5', 'D5'),
    ('QUEEN', 'G7', 'B7'),
    ('QUEEN', 'B2', 'D4'),
    ('QUEEN', 'E4', 'G6'),
    ('QUEEN', 'D1', 'A4'),
    ('QUEEN', 'G2', 'C6'),
]
testdata_invalid = [
    ('QUEEN', 'A1', 'B6'),
    ('QUEEN', 'F3', 'A7'),
    ('QUeEN', 'C3', 'E1'),
    ('QuEeN', 'F5', 'G6'),
    ('QUEEN', 'AA', 'C2'),
    ('QUEEN', 'B2', 'CC'),
    ('QUEEN', '17', 'F8'),
    ('QUEEN', 'C4', '27'),
    ('QUEEN', 'S1', 'F3'),
    ('QUEEN', 'G2', 'X7'),
]


class TestQueen:
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