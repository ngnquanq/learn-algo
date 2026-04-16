"""
Problem: Meeting Rooms II
Difficulty: Medium
Source: LeetCode #253
Tags: intervals, sorting, heap, greedy

Real-World Context:
    You are building the room-booking backend for a company's internal
    calendar system (think Google Calendar or Outlook).

    When employees schedule meetings, the system must automatically assign
    them a physical conference room. Your team needs to answer one key
    question before the office expansion budget is approved:

        "Given all the meetings scheduled for tomorrow,
         what is the MINIMUM number of conference rooms we need
         so that no two overlapping meetings share a room?"

Problem Statement:
    Given an array of meeting time intervals `intervals` where
    intervals[i] = [start_i, end_i], return the minimum number of
    conference rooms required.

    A room is free again exactly at its end time (end time is exclusive —
    a meeting ending at 10 does NOT conflict with one starting at 10).

Examples:
    Example 1:
        Input:  intervals = [[0, 30], [5, 10], [15, 20]]
        Output: 2

        Explanation:
            Meeting [0,30] occupies room A all day.
            Meeting [5,10] overlaps with [0,30] → needs room B.
            Meeting [15,20] also overlaps with [0,30] but room B is
            free by then (10 <= 15), so it reuses room B.
            → 2 rooms needed.

    Example 2:
        Input:  intervals = [[7, 10], [2, 4]]
        Output: 1

        Explanation:
            The two meetings don't overlap → 1 room is enough.

    Example 3:
        Input:  intervals = [[1, 5], [2, 6], [3, 7]]
        Output: 3

        All three overlap at some point → 3 rooms needed.

Constraints:
    - 1 <= len(intervals) <= 10^4
    - 0 <= start_i < end_i <= 10^6

Hint (read only if stuck):
    Sort meetings by start time. Then think about what you need to
    efficiently track: which rooms are currently in use, and when
    does the EARLIEST-finishing meeting free up?
    A min-heap keyed on end times is very useful here.
"""


def solution(intervals: list[list[int]]) -> int:
    # TODO: implement your solution here
    pass
