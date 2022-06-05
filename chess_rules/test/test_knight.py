import pytest
from chess_rules.chess_rules_module import is_figure_movable

testdata_valid = [
    ('KNIGHT', 'A1', 'C2'),
    ('KNIGHT', 'D1', 'C3'),
    ('KNIGHT', 'E7', 'C6'),
    ('KNIGHT', 'F5', 'H6'),
    ('KNIGHT', 'A4', 'B6'),
    ('KNIGHT', 'D2', 'F1'),
    ('KNIGHT', 'B7', 'D6'),
    ('KNIGHT', 'E2', 'F4'),
    ('KNIGHT', 'G6', 'H8'),
    ('KNIGHT', 'B5', 'D4'),
]
testdata_invalid = [
    ('KNIGHT', 'A1', 'H8'),
    ('KNIGHT', 'H1', 'F1'),
    ('KNIGHT', 'C3', 'M1'),
    ('KNIGHT', 'V3', 'G6'),
    ('KNiGHT', 'A4', 'C2'),
    ('KnIgHt', 'B2', 'C3'),
    ('KNIGHT', 'EE', 'F8'),
    ('KNIGHT', '44', 'F7'),
    ('KNIGHT', 'D1', '33'),
    ('KNIGHT', 'G2', 'BB'),
]


class TestKnight:
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