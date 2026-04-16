import pytest
from .solution import solution


class TestMeetingRoomsII:
    # -------------------------------------------------------
    # Basic / Example cases
    # -------------------------------------------------------
    def test_example_1(self):
        # [0,30] and [5,10] overlap; [15,20] reuses freed room
        assert solution([[0, 30], [5, 10], [15, 20]]) == 2

    def test_example_2(self):
        # No overlap — one room is enough
        assert solution([[7, 10], [2, 4]]) == 1

    def test_example_3(self):
        # All three overlap simultaneously
        assert solution([[1, 5], [2, 6], [3, 7]]) == 3

    # -------------------------------------------------------
    # Edge cases
    # -------------------------------------------------------
    def test_single_meeting(self):
        assert solution([[5, 10]]) == 1

    def test_end_equals_start(self):
        """A meeting ending at 10 should NOT conflict with one starting at 10."""
        assert solution([[1, 10], [10, 20]]) == 1

    def test_all_same_time(self):
        """5 meetings all at the same time — need 5 rooms."""
        assert solution([[1, 5]] * 5) == 5

    def test_sequential_meetings(self):
        """All back-to-back — only 1 room needed."""
        assert solution([[1, 2], [2, 3], [3, 4], [4, 5]]) == 1

    def test_unsorted_input(self):
        """Solution must handle unsorted intervals."""
        assert solution([[10, 15], [1, 5], [5, 10]]) == 1

    def test_large_overlap(self):
        """Many short meetings inside one long one."""
        intervals = [[0, 100]] + [[i, i + 1] for i in range(10)]
        assert solution(intervals) == 2

    # -------------------------------------------------------
    # Performance case
    # -------------------------------------------------------
    def test_large_input(self):
        """10k non-overlapping meetings — must stay well under timeout."""
        intervals = [[i * 2, i * 2 + 1] for i in range(10_000)]
        assert solution(intervals) == 1

    def test_large_input_all_overlap(self):
        """10k meetings all overlapping — needs 10k rooms."""
        intervals = [[0, 10_000]] * 10_000
        assert solution(intervals) == 10_000
