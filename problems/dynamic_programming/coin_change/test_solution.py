import pytest
from .solution import solution


class TestCoinChange:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_atm_denominations(self):
        # US-style coins: 1¢, 5¢, 10¢, 25¢ → make 36¢ in 3 coins
        assert solution([1, 5, 10, 25], 36) == 3

    def test_example_classic(self):
        assert solution([1, 2, 5], 11) == 3

    def test_impossible(self):
        # Only coin is 2, amount is odd — impossible
        assert solution([2], 3) == -1

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_amount_zero(self):
        # 0 coins needed for 0 amount
        assert solution([1, 2, 5], 0) == 0

    def test_exact_single_coin(self):
        assert solution([5], 5) == 1

    def test_large_coin_only(self):
        # Coin larger than amount — impossible
        assert solution([10], 3) == -1

    def test_multiple_ways_pick_minimum(self):
        # 6 = 3+3 (2 coins) or 6 = 1+1+1+1+1+1 (6 coins) → should pick 2
        assert solution([1, 3, 4], 6) == 2

    def test_single_coin_denomination(self):
        assert solution([1], 100) == 100

    # -------------------------------------------------------
    # Performance case
    # -------------------------------------------------------
    def test_large_amount(self):
        # max amount = 10^4, must finish well within timeout
        result = solution([1, 2, 5], 10_000)
        assert result == 2000  # 5 * 2000 = 10000
