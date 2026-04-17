import pytest
from .solution import solution


class TestCourseSchedule:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution(2, [[1, 0]]) is True

    def test_example_2(self):
        assert solution(2, [[1, 0], [0, 1]]) is False

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_no_prereqs(self):
        assert solution(3, []) is True

    def test_single_course(self):
        assert solution(1, []) is True

    def test_three_cycle(self):
        assert solution(3, [[0, 1], [1, 2], [2, 0]]) is False

    def test_chain(self):
        assert solution(4, [[1, 0], [2, 1], [3, 2]]) is True

    def test_disconnected(self):
        assert solution(4, [[1, 0], [3, 2]]) is True

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_input(self):
        n = 2000
        prereqs = [[i, i - 1] for i in range(1, n)]
        assert solution(n, prereqs) is True
