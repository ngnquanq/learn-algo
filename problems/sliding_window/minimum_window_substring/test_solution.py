import pytest
from .solution import solution


class TestMinimumWindowSubstring:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution("ADOBECODEBANC", "ABC") == "BANC"

    def test_example_2(self):
        assert solution("a", "a") == "a"

    def test_example_3(self):
        assert solution("a", "aa") == ""

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_t_not_in_s(self):
        assert solution("xyz", "a") == ""

    def test_s_equals_t(self):
        assert solution("abc", "abc") == "abc"

    def test_single_char_match(self):
        assert solution("b", "b") == "b"

    def test_duplicate_in_t(self):
        result = solution("ADOBECODEABANC", "AAB")
        assert "A" in result and result.count("A") >= 2

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        s = "A" * 50_000 + "B" + "A" * 49_999
        t = "B"
        result = solution(s, t)
        assert result == "B"
