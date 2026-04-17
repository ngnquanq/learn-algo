import pytest
from .solution import solution


class TestLongestSubstringWithoutRepeating:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution("abcabcbb") == 3

    def test_example_2(self):
        assert solution("bbbbb") == 1

    def test_example_3(self):
        assert solution("pwwkew") == 3

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_empty(self):
        assert solution("") == 0

    def test_single_char(self):
        assert solution("a") == 1

    def test_two_chars(self):
        assert solution("au") == 2

    def test_all_unique(self):
        assert solution("abcdef") == 6

    def test_dvdf(self):
        assert solution("dvdf") == 3

    def test_space(self):
        assert solution(" ") == 1

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        s = "abcdefghij" * 5000
        assert solution(s) == 10
