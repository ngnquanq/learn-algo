import pytest
from .solution import solution


class TestBrackets:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_nested(self):
        assert solution("{[()()]}") == 1

    def test_example_wrong(self):
        assert solution("([)()]") == 0

    def test_empty(self):
        assert solution("") == 1

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_single_opening(self):
        assert solution("(") == 0

    def test_simple_pair(self):
        assert solution("()") == 1

    def test_only_opening(self):
        assert solution("(((") == 0

    def test_only_closing(self):
        assert solution(")))") == 0

    def test_mismatched_types(self):
        assert solution("(]") == 0

    def test_deeply_nested(self):
        s = "(" * 10_000 + ")" * 10_000
        assert solution(s) == 1

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_balanced(self):
        s = "({[]})" * 33_333 + "()"  # ~200,000 chars
        assert solution(s) == 1
