import pytest
from .solution import solution


class TestPowXN:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        assert solution(2.0, 10) == pytest.approx(1024.0)

    def test_example_2(self):
        assert solution(2.1, 3) == pytest.approx(9.261, rel=1e-3)

    def test_example_3(self):
        assert solution(2.0, -2) == pytest.approx(0.25)

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_zero_exponent(self):
        assert solution(5.0, 0) == pytest.approx(1.0)

    def test_zero_base(self):
        assert solution(0.0, 5) == pytest.approx(0.0)

    def test_one_base_large_n(self):
        assert solution(1.0, 2147483647) == pytest.approx(1.0)

    def test_negative_one_even(self):
        assert solution(-1.0, 4) == pytest.approx(1.0)

    def test_negative_one_odd(self):
        assert solution(-1.0, 3) == pytest.approx(-1.0)

    # -------------------------------------------------------
    # Performance cases (large inputs should finish in time)
    # -------------------------------------------------------
    def test_large_negative_exponent(self):
        result = solution(2.0, -2147483648)
        assert result == pytest.approx(0.0, abs=1e-300)
