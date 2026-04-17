import pytest
from .solution import solution


class TestDecodeWays:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution("12") == 2

    def test_example_2(self):
        assert solution("226") == 3

    def test_example_3(self):
        assert solution("06") == 0

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_zero(self):
        assert solution("0") == 0

    def test_single_digit(self):
        assert solution("1") == 1

    def test_ten(self):
        assert solution("10") == 1

    def test_twenty_seven(self):
        assert solution("27") == 1

    def test_all_ones(self):
        assert solution("1111") == 5

    def test_trailing_zero(self):
        assert solution("2101") == 1

    def test_eleven_one_zero_six(self):
        assert solution("11106") == 2
