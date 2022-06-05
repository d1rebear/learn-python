import pytest
from chess_rules.chess_rules_module import is_figure_movable

testdata_valid = [
    ('PAWN', 'A1', 'A2'),
    ('PAWN', 'A1', 'A3'),
    ('PAWN', 'A2', 'A3'),
    ('PAWN', 'A2', 'A4'),
    ('PAWN', 'E2', 'E4'),
    ('PAWN', 'E2', 'E4'),
    ('PAWN', 'E2', 'E4'),
    ('PAWN', 'C6', 'C7'),
    ('PAWN', 'F5', 'F6'),
    ('PAWN', 'H2', 'H4'),
]
testdata_invalid = [
    ('Pawn1', 'A1', 'A8'),
    ('Pawn', 'A1', 'A4'),
    ('rook', 'A1', 'A6'),
    ('bishop', 'B2', 'D4'),
    ('PAWN', 'A1', 'D4'),
    ('PAWN', 'C1', 'C4'),
    ('PAWn', 'D2', 'D4'),
    ('PAWN', 'M2', 'C4'),
    ('PAWN', 'G5', 'J0'),
    ('pAwN', 'D6', 'J7'),
]


class TestPawn:
    @staticmethod
    @pytest.mark.parametrize("figure_name,start_position,end_position",
                             testdata_valid)
    def test_valid_move(figure_name, start_position, end_position):
        assert is_figure_movable(figure_name,
                                 position_input=start_position,
                                 move_input=end_position)

    @staticmethod
    @pytest.mark.parametrize("figure_name,start_position,end_position",
                             testdata_invalid)
    def test_invalid_move(figure_name, start_position, end_position):
        assert not is_figure_movable(figure_name,
                                     position_input=start_position,
                                     move_input=end_position)
