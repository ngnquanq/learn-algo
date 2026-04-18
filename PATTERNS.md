# Pattern Recognition Guide for Medium-Hard Codility Problems

This document teaches you how to **recognize** the algorithmic pattern behind a problem statement and how to **execute** the solution once you've identified it. For each pattern, you'll find: recognition signals, core intuition, step-by-step approach, a Python template, common variations, and pitfalls to watch for.

## How to use this guide

1. **Read a problem statement**. Don't panic, don't jump to code.
2. **Scan for recognition signals** listed in each pattern below. The signals are phrases in the problem statement, constraint shapes, or the type of answer requested.
3. **Identify the pattern**, then read the "core intuition" and "step-by-step approach" sections.
4. **Adapt the template** to the specific problem. Don't copy blindly — understand each line.
5. **Test locally** with edge cases before declaring done.

**Two important rules when in doubt:**
- If constraints show `N ≤ 10^5` or `10^6` and you think "brute force is O(n²)", you need a faster pattern — most likely prefix sums, two pointers, sorting, or binary search.
- If the problem says "find the minimum/maximum X such that...", it's almost always **binary search on the answer** or **greedy**.

---

## Table of Contents

1. [Prefix Sums](#1-prefix-sums)
2. [Sorting (and Counting)](#2-sorting-and-counting)
3. [Stacks & Queues](#3-stacks--queues)
4. [Binary Search](#4-binary-search)
5. [Two Pointers / Caterpillar Method](#5-two-pointers--caterpillar-method)
6. [Sliding Window](#6-sliding-window)
7. [Greedy Algorithms](#7-greedy-algorithms)
8. [Kadane's Algorithm (Maximum Slice)](#8-kadanes-algorithm-maximum-slice)
9. [Leader / Boyer-Moore Majority Vote](#9-leader--boyer-moore-majority-vote)
10. [Dynamic Programming](#10-dynamic-programming)
11. [Trees (BFS / DFS)](#11-trees-bfs--dfs)
12. [Graphs (BFS / DFS / Dijkstra / Union-Find / Topological Sort)](#12-graphs)
13. [Math & Number Theory (Sieve / GCD / Fast Power)](#13-math--number-theory)
14. [Bit Manipulation / XOR](#14-bit-manipulation--xor)

---

## 1. Prefix Sums

### What it is

Precompute the cumulative sum of an array so that you can answer "sum of A[L..R]" in O(1) per query, instead of re-summing each time.

### Recognize when

- The problem has a **fixed array** and many queries about **ranges**: "sum in range [L, R]", "count of X in [L, R]", "does a 0-sum slice exist?"
- Phrases like "range query", "sum of a slice", "count between positions P and Q"
- You see an outer loop over queries and you're tempted to write an inner loop over the range — that's O(Q·N) which is too slow for N, Q = 10^5.
- The problem involves **counting elements with a property** in subarrays (e.g., passing cars, count divisible, count of each character).

### Core intuition

If `prefix[i]` stores `A[0] + A[1] + ... + A[i-1]`, then the sum of `A[L..R]` (inclusive) equals `prefix[R+1] - prefix[L]`. Each range query becomes a single subtraction.

The trick generalizes: you can have one prefix array **per property**. For "count of character 'A' in substring S[L..R]", maintain `prefixA[i]` = count of 'A' in S[0..i-1].

### Step-by-step approach

1. Identify what quantity you need over ranges (sum? count? XOR?).
2. Build a prefix array of length N+1 with `prefix[0] = 0` and `prefix[i+1] = prefix[i] + transform(A[i])`.
3. Answer each query as `prefix[R+1] - prefix[L]`.
4. If multiple properties (like different characters), build one prefix array per property.

### Python template

```python
def solution(A: list[int], queries: list[tuple[int, int]]) -> list[int]:
    n = len(A)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + A[i]

    results = []
    for L, R in queries:
        results.append(prefix[R + 1] - prefix[L])
    return results
```

### Common variations

- **Prefix count** (instead of sum): `prefix[i+1] = prefix[i] + (1 if cond(A[i]) else 0)`.
- **Multiple prefix arrays**: one per distinct value (genomic range query has 4 arrays, one per nucleotide).
- **Prefix + hashmap for "subarray sum == K"**: seen in problems like Max ZeroSum Slice — as you scan, look up `prefix[i] - K` in a hashmap.
- **2D prefix sums** for matrix range queries.

### Pitfalls

- **Off-by-one** on `prefix[R+1]` vs `prefix[R]`. Always use `prefix` of length N+1 with `prefix[0] = 0` to make the math clean.
- Forgetting to handle `L == 0` specially if you use a length-N prefix array (use length N+1 to avoid this).
- Overflow: count of pairs can exceed 32-bit int (see passing_cars — return -1 if > 1,000,000,000).

### Problems in this repo

`prefix_sums/genomic_range_query`, `prefix_sums/count_div`, `prefix_sums/passing_cars`, `arrays/product_except_self` (prefix product), `mixed_practice/count_non_divisible`, `math/count_semiprimes`.

---

## 2. Sorting (and Counting)

### What it is

Many problems become trivial once the data is sorted. Sorting costs O(N log N), which is usually fine for N ≤ 10^6. When values are bounded small integers, **counting sort** gives O(N + K) — even faster.

### Recognize when

- Problem involves pairs, triplets, or comparisons between elements (triangle sides, three-sum, max product of three).
- The answer depends on **relative order**, not original positions (e.g., "count distinct values", "find median", "max after K operations").
- You have events to process in chronological order (disc intersections → sort by start points).
- Values are bounded small integers (e.g., 0..N) — use counting sort / frequency array.

### Core intuition

Sorting transforms the problem from "arbitrary order" to "monotonically increasing order," which enables:
- Two-pointer scans from both ends
- Binary search
- Sweep-line processing
- Greedy choice (always pick smallest/largest)

### Step-by-step approach

1. Identify whether sorting helps. Ask: "If I had this array sorted, would the problem be easier?"
2. Sort the relevant data. For pairs (e.g., `[value, index]`), sort by the relevant key.
3. Scan the sorted data once (or twice with two pointers) to compute the answer.

### Python template

```python
def solution(A: list[int]) -> int:
    A.sort()  # or sorted(A) if you must preserve the input

    # Example: maximum product of three
    # After sorting, either the last 3 elements, or
    # the two smallest (negatives) with the largest positive.
    return max(
        A[-1] * A[-2] * A[-3],
        A[0] * A[1] * A[-1],
    )
```

### Common variations

- **Counting sort** for bounded integers:
  ```python
  counts = [0] * (max_val + 1)
  for x in A:
      counts[x] += 1
  ```
- **Sort by custom key**: `sorted(pairs, key=lambda p: (p[0], -p[1]))` for tuples sorted by first asc, second desc.
- **Sweep line**: for each disc, emit start (`i - r`) and end (`i + r`) events; sort all events.
- **Index-preserving sort**: `sorted(range(n), key=lambda i: A[i])` gives indices sorted by value.

### Pitfalls

- Sorting mutates the list in-place. Use `sorted(A)` if you need the original.
- Custom comparators are slower than keys in Python — prefer `key=`.
- For large N with small value range, counting sort is dramatically faster than `sort()`.

### Problems in this repo

`sorting/max_product_of_three`, `sorting/distinct`, `sorting/dominator`, `sorting/equi_leader`, `mixed_practice/number_of_disc_intersections`, `two_pointers/three_sum` (sort first).

---

## 3. Stacks & Queues

### What it is

A **stack** (LIFO) maintains elements such that the most recently pushed is accessible first. A **queue** (FIFO) maintains elements in insertion order for BFS. A **monotonic stack/deque** keeps elements in sorted order relative to their indices — a powerful optimization.

### Recognize when

- Problem involves **matching pairs** of opening/closing markers: brackets, tags, parentheses.
- Problem describes an **iterative simulation** where the latest event cancels or combines with an earlier one: fish eating fish, stone wall blocks.
- You need the **next greater/smaller element** for every position (monotonic stack).
- You're processing a string/array and need to "undo" or "pop" based on current element.

### Core intuition

When processing sequentially and the "latest seen" matters, push onto a stack. When you see something that resolves/cancels the top, pop it. The stack remembers only relevant state — old, resolved things are gone.

For monotonic stacks: maintain an invariant (e.g., strictly decreasing). When a new element violates it, pop until it's restored. Each element is pushed and popped at most once → total O(N).

### Step-by-step approach

1. Identify the **state you care about** as you scan — what makes the top of the stack "current"?
2. Define **push** condition (when new element must be remembered).
3. Define **pop** condition (when top of stack is resolved or beaten).
4. Iterate through the input once. Each element triggers some combination of pushes and pops.

### Python template

```python
def solution(S: str) -> int:
    """Balanced brackets: return 1 if properly nested, else 0."""
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in S:
        if ch in '([{':
            stack.append(ch)
        else:
            if not stack or stack[-1] != pairs[ch]:
                return 0
            stack.pop()
    return 1 if not stack else 0
```

**Monotonic stack template (next greater element):**

```python
def next_greater(A: list[int]) -> list[int]:
    n = len(A)
    result = [-1] * n
    stack = []  # stores indices, values on stack are strictly decreasing
    for i in range(n):
        while stack and A[stack[-1]] < A[i]:
            result[stack.pop()] = A[i]
        stack.append(i)
    return result
```

### Common variations

- **Monotonic deque** for sliding window max (see pattern #6).
- **Stone wall**: stack of heights; pop taller ones when current is shorter; push when current is new.
- **Fish**: stack of downstream fish; upstream fish fights through them.

### Pitfalls

- Forgetting to check "stack is not empty" before peeking/popping.
- Storing values vs indices: if you later need the *position*, store indices. If you only care about values, store values.
- For monotonic: decide strict (`<`) vs non-strict (`<=`) carefully — changes answers on equal elements.

### Problems in this repo

`stacks_queues/brackets`, `stacks_queues/fish`, `stacks_queues/stone_wall`, `two_pointers/trapping_rain_water` (monotonic stack variant).

---

## 4. Binary Search

### What it is

A logarithmic search that works on any **monotonic** predicate. Two main flavors:

- **Classical**: find a target value in a sorted array.
- **Binary search on the answer** (the real power move): the answer space is an integer range, and you can check feasibility of a candidate in O(N). Total: O(N log(range)).

### Recognize when

**Classical:**
- Array is sorted (or rotated sorted).
- You're asked to find an element or its position.

**Binary search on the answer — this is the one to memorize.** Signals:
- "Find the **minimum K** such that...", "Find the **maximum X** such that..."
- "Minimize the maximum" or "Maximize the minimum"
- The feasibility of a candidate answer is **monotonic**: if K works, then K+1 also works (or vice versa).
- Constraints like: N ≤ 10^5, answer range could be up to 10^9 → need O(N log 10^9) ≈ O(30N).

Example phrasings that scream "binary search on answer":
- "Minimum speed K such that Koko can eat all bananas in H hours" → larger K → faster eating → more likely to finish.
- "Divide into K blocks minimizing the max block sum" → larger max_sum → easier to fit into K blocks.
- "Minimum number of nails to hammer all planks" → more nails → more planks covered.

### Core intuition

If you can answer **"does X work?"** in O(N) for any candidate X, and the yes/no answer is monotonic across X, then binary search over X to find the smallest/largest X where the answer flips.

### Step-by-step approach

**Binary search on the answer:**

1. Define the **answer range**: `lo`, `hi` (usually `lo = min possible answer`, `hi = max possible answer`).
2. Write a helper `feasible(X) -> bool` that runs in O(N) or O(N log N).
3. Binary search for the boundary where feasibility flips.

```python
def solution(...) -> int:
    lo, hi = min_possible, max_possible
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            hi = mid        # try smaller
        else:
            lo = mid + 1    # need bigger
    return lo
```

### Python template

**Classical (on sorted array):**

```python
def binary_search(A: list[int], target: int) -> int:
    lo, hi = 0, len(A) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if A[mid] == target:
            return mid
        elif A[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

**Binary search on answer (Koko Eating Bananas):**

```python
def solution(piles: list[int], h: int) -> int:
    def can_finish(K: int) -> bool:
        hours = sum((p + K - 1) // K for p in piles)  # ceil division
        return hours <= h

    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        if can_finish(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
```

### Common variations

- **Rotated sorted array**: at each step, figure out which half is sorted.
- **Binary search + greedy verification**: for each candidate K, greedily check if it works.
- **Binary search + prefix sums**: for each candidate, use prefix sums to check feasibility in O(1) per plank (see nailing_planks).
- **Lower bound / upper bound**: Python's `bisect.bisect_left` / `bisect.bisect_right`.

### Pitfalls

- **Off-by-one** on `lo`, `hi`, and the update (`mid` vs `mid + 1`). Pick a convention (e.g., `lo < hi`, `hi = mid`, `lo = mid + 1`) and stick with it.
- **Monotonicity**: verify the predicate is actually monotonic before choosing binary search.
- **Integer overflow in `mid`**: `(lo + hi) // 2` can overflow in other languages. Python is fine, but consider `lo + (hi - lo) // 2` as a habit.

### Problems in this repo

`binary_search/min_max_division`, `binary_search/nailing_planks`, `binary_search/search_in_rotated_sorted_array`, `binary_search/koko_eating_bananas`, `mixed_practice/flags`.

---

## 5. Two Pointers / Caterpillar Method

### What it is

Two indices that move through the array, often from both ends or both from the left. The pair maintains an invariant (e.g., "all elements between them are distinct") and each iteration either advances one pointer or both.

### Recognize when

- Problem involves **pairs** (two sum, container with most water) or **triplets** (three sum, count triangles).
- You need to find a **range** or **slice** satisfying a property: "longest subarray with distinct elements", "smallest window containing target characters".
- Sorted input plus "find pair summing to X" → two pointers from ends.
- "Caterpillar" variant: both pointers move left-to-right; left advances only when necessary.

### Core intuition

Each pointer moves forward only (monotonic motion), so total work is O(N), not O(N²). The key insight: when you advance a pointer, you don't need to reconsider positions it's already passed.

**Classic pair-sum trick (on sorted array):**
- If `A[left] + A[right] < target`: the smallest possible sum with `A[right]` is too small — advance `left`.
- If `A[left] + A[right] > target`: advance `right` leftward.
- If equal: record the pair, then advance both.

### Step-by-step approach

**Caterpillar (window-based):**
1. Initialize `left = 0`, maintain data structure tracking window state (count, set, etc.).
2. Advance `right` in a loop.
3. While window violates the invariant, advance `left` and update state.
4. At each step, record the current window's contribution to the answer.

### Python template

**Two pointers from ends (two sum on sorted array):**

```python
def two_sum_sorted(A: list[int], target: int) -> tuple[int, int]:
    left, right = 0, len(A) - 1
    while left < right:
        s = A[left] + A[right]
        if s == target:
            return (left, right)
        elif s < target:
            left += 1
        else:
            right -= 1
    return (-1, -1)
```

**Caterpillar (count slices with distinct elements):**

```python
def solution(M: int, A: list[int]) -> int:
    seen = set()
    left = 0
    result = 0
    for right in range(len(A)):
        while A[right] in seen:
            seen.remove(A[left])
            left += 1
        seen.add(A[right])
        result += right - left + 1  # all slices ending at `right`
    return min(result, 1_000_000_000)
```

### Common variations

- **Three-sum**: fix the first element, run two-pointer on the rest.
- **Trapping rain water**: two pointers from ends, tracking `left_max`, `right_max`.
- **Container with most water**: two pointers from ends, move the shorter side inward.
- **Minimum window substring**: caterpillar with character frequency counters.

### Pitfalls

- On sorted arrays with duplicates, skip duplicates explicitly after finding a match (else you'll emit the same triplet multiple times).
- Forgetting to update the window's auxiliary data structure (set, counter) when advancing `left`.
- Using `while` where `if` suffices, or vice versa.

### Problems in this repo

`two_pointers/count_distinct_slices`, `two_pointers/three_sum`, `two_pointers/container_with_most_water`, `two_pointers/trapping_rain_water`.

---

## 6. Sliding Window

### What it is

A specialization of the caterpillar method where the window is either fixed-size (always K elements) or variable-size with a clear grow/shrink rule.

### Recognize when

- "Find the longest/shortest subarray satisfying P" (variable window).
- "For each window of size K, compute X" (fixed window).
- "Max/min/sum in every window of size K".
- The naive O(N·K) solution is too slow.

### Core intuition

As the window slides one position right, it gains one element (on the right) and loses one element (on the left). Most statistics can be updated in O(1) per slide by computing `new_value = old_value + entering - leaving`.

For max/min over a window, use a **monotonic deque**: store indices in decreasing (for max) order. Remove indices falling out of the window from the front; remove smaller values from the back before inserting the new one.

### Step-by-step approach

**Fixed window (size K):**
1. Process the first K elements to initialize the window.
2. For each subsequent position, add the new element, remove the oldest, record the statistic.

**Variable window (longest substring without repeating):**
1. Expand `right` to grow the window.
2. When the invariant breaks, shrink `left` until restored.
3. Track the best length seen.

### Python template

**Variable window (longest substring without repeating chars):**

```python
def solution(s: str) -> int:
    seen = {}  # char -> last index
    left = 0
    best = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        best = max(best, right - left + 1)
    return best
```

**Fixed window (sliding window max via monotonic deque):**

```python
from collections import deque

def solution(nums: list[int], k: int) -> list[int]:
    dq = deque()  # indices, values A[dq] are strictly decreasing
    result = []
    for i, x in enumerate(nums):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and nums[dq[-1]] < x:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result
```

### Common variations

- **Min window substring**: count required chars, expand until all satisfied, shrink to find minimum.
- **Longest substring with at most K distinct chars**: similar with a char-count map.
- **Fixed window sum**: trivial prefix-sum or running sum.

### Pitfalls

- For character-frequency problems, don't forget to decrement when a char leaves the window — and remove it from the map if count drops to 0 (changes "distinct count" semantics).
- For monotonic deque: it stores *indices*, not values. Always access `A[dq[0]]` for the value.

### Problems in this repo

`sliding_window/minimum_window_substring`, `sliding_window/longest_substring_without_repeating`, `sliding_window/max_sliding_window`.

---

## 7. Greedy Algorithms

### What it is

At each step, make the choice that looks best locally, and prove (or trust) that these local choices combine into a globally optimal solution.

### Recognize when

- You need to **schedule**, **assign**, or **count** things under a constraint.
- Problem has a natural ordering (time, size, cost) and you process items in that order.
- There's no obvious "future dependency" — decisions can be made one at a time without reconsidering.
- Common phrases: "maximum number of X", "minimum number of Y to cover all", "can you complete the tour / journey / task list?"

### Core intuition

Greedy works when a **locally optimal choice** is also globally optimal. Usually there's an **exchange argument**: if you swap any non-greedy choice with the greedy one, the result is no worse.

### Step-by-step approach

1. Identify the **greedy choice rule** — what's "best locally"? (Smallest deadline? Largest value/weight ratio? Earliest start?)
2. Sort the input by that criterion if it helps.
3. Scan once, making the greedy choice at each step, maintaining only the state you need.
4. **Verify correctness** with an exchange argument or small examples. If greedy fails, fall back to DP.

### Python template

**Gas station:**

```python
def solution(gas: list[int], cost: list[int]) -> int:
    if sum(gas) < sum(cost):
        return -1
    tank = 0
    start = 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:
            tank = 0
            start = i + 1
    return start
```

**Tie ropes (accumulate until threshold):**

```python
def solution(K: int, A: list[int]) -> int:
    count = 0
    acc = 0
    for x in A:
        acc += x
        if acc >= K:
            count += 1
            acc = 0
    return count
```

### Common variations

- **Interval scheduling**: sort by end time, pick earliest-ending non-overlapping interval.
- **Jump game**: track the farthest reachable index; fail if current index exceeds it.
- **Task assignment**: sort tasks and workers, pair them optimally.
- **Huffman-style**: repeatedly combine two smallest elements (uses a min-heap).

### Pitfalls

- Greedy is easy to get wrong! **Always consider counter-examples**. If you can't convince yourself greedy works, try DP.
- "Greedy by value" vs "greedy by ratio" often differ — pick carefully.
- Don't confuse greedy with brute-force-with-early-exit.

### Problems in this repo

`greedy/gas_station`, `greedy/jump_game`, `mixed_practice/tie_ropes`, `intervals/meeting_rooms_ii`.

---

## 8. Kadane's Algorithm (Maximum Slice)

### What it is

Finds the maximum sum of a contiguous subarray in O(N). A fundamental DP insight: at each index, either extend the previous best slice or start a new one here.

### Recognize when

- "Maximum sum of a contiguous subarray"
- "Max profit from single buy/sell" (equivalent to max slice of differences)
- "Maximum subarray product" (variant: track both max and min because of negatives)
- "Find best time to buy/sell with K transactions" (more complex DP, but same flavor)

### Core intuition

Let `dp[i]` = max sum of a subarray ending exactly at index `i`. Then:
- `dp[i] = max(A[i], dp[i-1] + A[i])` — either start fresh at `A[i]`, or extend the slice ending at `i-1`.
- Answer = `max(dp)`.
- Space: O(1) since we only need the previous value.

### Step-by-step approach

1. Initialize `current_max = A[0]`, `best = A[0]`.
2. For each subsequent element `x`: `current_max = max(x, current_max + x)`; `best = max(best, current_max)`.
3. Return `best`.

### Python template

```python
def solution(A: list[int]) -> int:
    current = best = A[0]
    for x in A[1:]:
        current = max(x, current + x)
        best = max(best, current)
    return best
```

**Max profit (transform first, then Kadane on differences):**

```python
def max_profit(prices: list[int]) -> int:
    if len(prices) < 2:
        return 0
    min_so_far = prices[0]
    best = 0
    for p in prices[1:]:
        best = max(best, p - min_so_far)
        min_so_far = min(min_so_far, p)
    return best
```

### Common variations

- **Max double slice sum**: do two Kadane passes (left-to-right and right-to-left), then combine.
- **Max circular subarray**: answer = max(Kadane on original, total - Kadane on negated). Handle all-negative edge case.
- **Max product subarray**: track both max and min at each position (negatives flip signs).

### Pitfalls

- For "non-empty subarray": initialize to `A[0]`, not 0. If all elements are negative, the answer is the largest single element.
- For "can be empty" versions, initialize `best = 0`.
- `max_double_slice_sum` requires two directional Kadanes plus careful handling of empty slices.

### Problems in this repo

`arrays/max_slice_sum`, `arrays/max_double_slice_sum`, `arrays/max_profit`.

---

## 9. Leader / Boyer-Moore Majority Vote

### What it is

An O(N) time, O(1) space algorithm to find the element that appears more than N/2 times (the **dominator** or **leader**).

### Recognize when

- "Find the element appearing more than N/2 times"
- "Does a dominator exist?"
- Codility-style: "Equi Leader", "Dominator"
- Any problem where majority properties matter

### Core intuition

If an element truly appears more than N/2 times, every "cancellation" (one of that element vs one of something else) still leaves the majority standing. Maintain a candidate and a counter; pair off non-candidates against the candidate.

### Step-by-step approach

1. **Phase 1 — Find candidate**: scan once, maintain `(candidate, count)`. If count is 0, adopt current element as candidate. Increment count if match, decrement otherwise.
2. **Phase 2 — Verify**: scan again, count occurrences of candidate. If > N/2, it's the leader; else there's no leader.

### Python template

```python
def find_leader(A: list[int]) -> int | None:
    candidate = None
    count = 0
    for x in A:
        if count == 0:
            candidate = x
            count = 1
        elif x == candidate:
            count += 1
        else:
            count -= 1

    # Phase 2: verify
    if candidate is None:
        return None
    if A.count(candidate) > len(A) // 2:
        return candidate
    return None
```

### Common variations

- **Equi leader**: find leader, then scan prefix counting how many times the leader appears in A[0..i]; a split at i is valid if leader dominates both halves.
- **Majority element (n/3)**: can have at most two candidates; track two candidates with two counters.

### Pitfalls

- **Always verify in phase 2**. Without a true majority, phase 1 returns garbage.
- A dominator needs strictly more than half: count > N/2, not ≥.

### Problems in this repo

`sorting/dominator`, `sorting/equi_leader`.

---

## 10. Dynamic Programming

### What it is

Break a problem into overlapping subproblems whose solutions are reused. Store answers to subproblems in a table (bottom-up) or memo (top-down) to avoid recomputation.

### Recognize when

- You see "count the number of ways to..." or "find the min/max cost to..."
- Optimal solution of size N depends on optimal solutions of smaller subproblems.
- A recursive solution has overlapping calls (e.g., `f(n) = f(n-1) + f(n-2)`).
- Common families:
  - **1D DP**: climbing stairs, house robber, decode ways, coin change.
  - **2D DP**: grid paths, edit distance, longest common subsequence.
  - **Knapsack-style**: partition equal subset sum, coin change.
  - **DP on value ranges**: min abs sum (DP on total sum, not on N).

### Core intuition

Identify:
1. **State**: what information describes a subproblem? (`dp[i]`, `dp[i][j]`, or `dp[i][target]`?)
2. **Transition**: how does `dp[i]` relate to smaller subproblems?
3. **Base cases**: values of `dp[0]`, `dp[1]`, etc.
4. **Order**: bottom-up (iterate i = 0, 1, 2, ...) or top-down (recursive with memo).
5. **Answer**: which dp value is the final answer?

### Step-by-step approach

1. **Define the state** clearly. Write it down: "dp[i] = ...".
2. **Write the recurrence**. Identify all possible "last choices" that lead to state `i`.
3. **Base cases**: usually `dp[0]` and sometimes `dp[1]`.
4. **Iterate** in the right order.
5. **Space optimize** if only the last O(1) or O(M) states are needed.

### Python templates

**1D DP (house robber):**

```python
def solution(nums: list[int]) -> int:
    # dp[i] = max money from houses 0..i
    # dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    prev2 = 0
    prev1 = 0
    for x in nums:
        curr = max(prev1, prev2 + x)
        prev2 = prev1
        prev1 = curr
    return prev1
```

**2D DP (grid min path sum):**

```python
def solution(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
    return dp[m-1][n-1]
```

**0/1 Knapsack (partition equal subset sum):**

```python
def solution(nums: list[int]) -> bool:
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for x in nums:
        for s in range(target, x - 1, -1):
            dp[s] = dp[s] or dp[s - x]
    return dp[target]
```

### Common variations

- **Decode ways**: `dp[i]` from `dp[i-1]` (if current char valid) and `dp[i-2]` (if last two digits form valid code).
- **Longest increasing subsequence (LIS)**: O(n²) DP, or O(n log n) with patience sorting.
- **Edit distance**: 3-way transition (insert, delete, replace).
- **Min abs sum**: DP on sum values (0..total_sum/2), not on array indices.

### Pitfalls

- **Define the state precisely**. Vague states lead to buggy transitions.
- **Initialization**: `dp[0]` might be 1 (empty subset sums to 0) or 0 (no elements = no sum).
- **Iteration order** in knapsack matters: outer loop over items, inner loop reversed over capacities for 0/1 knapsack; forward for unbounded.
- **Off-by-one** on string DPs: `dp[i][j]` usually = distance between first i chars of word1 and first j chars of word2 — table is `(m+1) x (n+1)`.
- **Space**: many DPs only need the last 1-2 rows; reduce 2D to 1D when you can.

### Problems in this repo

`dynamic_programming/coin_change`, `dynamic_programming/climbing_stairs`, `dynamic_programming/house_robber`, `dynamic_programming/decode_ways`, `dynamic_programming/unique_paths`, `dynamic_programming/minimum_path_sum`, `dynamic_programming/longest_increasing_subsequence`, `dynamic_programming/longest_common_subsequence`, `dynamic_programming/edit_distance`, `dynamic_programming/partition_equal_subset_sum`, `mixed_practice/min_abs_sum`.

---

## 11. Trees (BFS / DFS)

### What it is

Traversal of hierarchical structures. **DFS** (via recursion or explicit stack) explores deeply before backtracking. **BFS** (via queue) processes level by level.

### Recognize when

- Input is a binary tree or a rooted tree.
- "Max depth", "min depth", "level-order traversal" → BFS.
- "Validate BST", "lowest common ancestor", "path sum" → DFS.
- "Serialize/deserialize" → either, usually DFS with preorder.

### Core intuition

- **DFS** naturally matches recursive definitions: "the max depth of a tree = 1 + max depth of its subtrees."
- **BFS** uses a queue to process siblings before children, giving level-by-level output.
- **Validate BST** needs min/max bounds passed down during DFS (not just comparing with parent).
- **Lowest common ancestor**: recurse left and right; if both return a node, current is the LCA.

### Step-by-step approach

**DFS recursive template:**

1. Write the base case (usually `None` or leaf).
2. Recurse on left and right subtrees.
3. Combine results.

**BFS iterative template:**

1. Initialize queue with root.
2. While queue not empty: pop front, process, enqueue children.
3. For level tracking: snapshot queue size at start of each iteration.

### Python templates

**DFS (max depth):**

```python
def max_depth(root: TreeNode | None) -> int:
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

**BFS (level-order):**

```python
from collections import deque

def level_order(root: TreeNode | None) -> list[list[int]]:
    if root is None:
        return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result
```

**Validate BST (DFS with bounds):**

```python
def is_bst(root: TreeNode | None, lo=float('-inf'), hi=float('inf')) -> bool:
    if root is None:
        return True
    if not (lo < root.val < hi):
        return False
    return is_bst(root.left, lo, root.val) and is_bst(root.right, root.val, hi)
```

### Common variations

- **LCA**: recurse on both sides, `return root if both sides non-null else the non-null side`.
- **Path sum**: pass accumulator down, check at leaves.
- **Tree diameter**: return height from each subtree, update global diameter.
- **Serialize**: preorder DFS with `None` sentinels.

### Pitfalls

- **Recursion depth**: Python default is ~1000. For a left-skewed tree of 10^4 nodes, use `sys.setrecursionlimit` or iterate.
- **Validate BST**: comparing only with parent is *wrong* — you need bounds from all ancestors.
- Handling `None` at the top level — forgetting → null-pointer crash.

### Problems in this repo

`trees/max_depth_binary_tree`, `trees/validate_binary_search_tree`, `trees/lowest_common_ancestor`, `trees/binary_tree_level_order_traversal`.

---

## 12. Graphs

### What it is

Nodes connected by edges. Key algorithms:
- **BFS**: shortest path in unweighted graph, level-by-level exploration.
- **DFS**: connectivity, cycle detection, topological ordering.
- **Dijkstra**: shortest path in weighted graph (non-negative weights).
- **Union-Find**: dynamic connectivity, cycle detection when edges arrive online.
- **Topological Sort**: ordering of a DAG (via BFS/Kahn or DFS).

### Recognize when

- Problem involves **nodes and edges** (explicit or implicit).
- Grid problems with connectivity ("number of islands", "flood fill") → BFS/DFS.
- "Can we reach X from Y?" → BFS/DFS.
- "Shortest path with weights" → Dijkstra.
- "Do edges form a cycle?" → DFS (recursion-stack coloring) or Union-Find.
- "Course ordering with prereqs" → topological sort.
- Word ladders, transformation sequences → BFS on implicit graph.

### Core intuitions

**BFS**: explores in order of distance from source. First time you reach a node is via a shortest path.

**DFS**: dives into one branch, backtracks. Three states (white/gray/black or 0/1/2) detect cycles.

**Dijkstra**: a priority queue always picks the node with smallest known distance. Once popped, its distance is final. Requires non-negative weights.

**Union-Find**: every node has a parent pointer; root of the component represents the component. `union` links two roots; `find` walks up to the root (with path compression).

**Kahn's algorithm (topological sort via BFS)**: start with nodes of in-degree 0, "remove" them (decrement neighbors' in-degrees). If all nodes processed, the order is a topological sort; if not, there's a cycle.

### Python templates

**BFS on grid:**

```python
from collections import deque

def bfs_grid(grid, start):
    m, n = len(grid), len(grid[0])
    visited = {start}
    queue = deque([start])
    while queue:
        r, c = queue.popleft()
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc))
    return visited
```

**Dijkstra:**

```python
import heapq

def dijkstra(graph: dict[int, list[tuple[int, int]]], source: int, n: int) -> list[float]:
    dist = [float('inf')] * (n + 1)
    dist[source] = 0
    pq = [(0, source)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist
```

**Topological sort (Kahn's):**

```python
from collections import deque, defaultdict

def has_topo_order(n: int, edges: list[list[int]]) -> bool:
    """Returns True if the directed graph is acyclic."""
    indeg = [0] * n
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        indeg[v] += 1
    queue = deque(i for i in range(n) if indeg[i] == 0)
    processed = 0
    while queue:
        u = queue.popleft()
        processed += 1
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                queue.append(v)
    return processed == n
```

**Union-Find:**

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True
```

### Common variations

- **Multi-source BFS**: start with all sources in the queue simultaneously (rotting oranges).
- **0-1 BFS**: when weights are 0 or 1, use a deque — push 0-weight edges to front, 1-weight to back.
- **BFS on implicit graph**: word ladder — neighbors are words differing by one letter.
- **Detect cycle in undirected graph**: Union-Find; if two endpoints of an edge are already connected, it's a cycle.

### Pitfalls

- Forgetting to mark a node as visited on enqueue (not dequeue) → exponential blow-up.
- Dijkstra with negative weights → wrong answer. Use Bellman-Ford instead.
- Union-Find without path compression → O(N) per operation in the worst case.
- In topological sort, an "all in-degrees processed" check is required to detect cycles.

### Problems in this repo

`graphs/number_of_islands`, `graphs/clone_graph`, `graphs/course_schedule`, `graphs/network_delay_time`, `graphs/word_ladder`, `graphs/redundant_connection`.

---

## 13. Math & Number Theory

### What it is

Problems that hinge on mathematical properties: primes, divisors, GCD/LCM, modular arithmetic, combinatorics.

### Recognize when

- "Count primes less than N" → **Sieve of Eratosthenes**.
- "Count semiprimes", "smallest prime factor" → sieve variant.
- "GCD / LCM", "Chocolates by Numbers", periodic cycles → **Euclidean algorithm**.
- "Compute x^n efficiently" → **binary exponentiation**.
- "Same prime divisors" → repeated GCD reduction.
- "Count divisors" → iterate up to sqrt(N).

### Core intuitions

**Sieve of Eratosthenes**: mark each composite by iterating multiples of primes. Total operations: O(N log log N).

**Euclidean algorithm**: `gcd(a, b) = gcd(b, a % b)`, base case `gcd(a, 0) = a`. O(log min(a, b)).

**Binary exponentiation**: `x^n = (x^(n/2))^2` if n even, `x * x^(n-1)` if odd. O(log n).

**Common prime divisors**: two numbers have the same set of prime divisors iff dividing each repeatedly by `gcd(a, b)` and its successors reduces both to 1.

### Python templates

**Sieve (count primes < N):**

```python
def count_primes(n: int) -> int:
    if n < 2:
        return 0
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False
    return sum(is_prime)
```

**Smallest prime factor sieve (for semiprimes):**

```python
def smallest_prime_factor(N: int) -> list[int]:
    spf = [0] * (N + 1)
    for i in range(2, N + 1):
        if spf[i] == 0:
            for j in range(i, N + 1, i):
                if spf[j] == 0:
                    spf[j] = i
    return spf
```

**GCD (Euclidean):**

```python
def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a
```

**Binary exponentiation:**

```python
def power(x: float, n: int) -> float:
    if n < 0:
        x, n = 1 / x, -n
    result = 1.0
    while n > 0:
        if n & 1:
            result *= x
        x *= x
        n >>= 1
    return result
```

### Common variations

- **Prefix sum of primes / semiprimes**: combine sieve with prefix sum for range-count queries.
- **Count divisors up to sqrt(N)**: iterate i from 1 to sqrt(N); if `N % i == 0`, add both i and N/i.
- **Modular exponentiation**: same as binary exponentiation but take `% MOD` at each step.

### Pitfalls

- Off-by-one on sieve bounds (`i*i` vs `i+i` start — use `i*i` for correctness).
- Integer overflow (not an issue in Python, but watch for `float` precision in pow).
- `pow(x, n)` with `n == INT_MIN` — take absolute value carefully (Python handles negatives cleanly).

### Problems in this repo

`math/count_primes`, `math/pow_x_n`, `math/gcd_and_lcm`, `math/count_semiprimes`, `math/common_prime_divisors`, `mixed_practice/count_non_divisible`.

---

## 14. Bit Manipulation / XOR

### What it is

Using bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to solve problems in O(1) space or leverage algebraic properties of binary.

### Recognize when

- "Find the unique element" where all others appear in pairs → XOR.
- "Count set bits", "check if power of two" → bitwise.
- "Generate all subsets" → iterate over `1 << n` bitmasks.
- The problem explicitly mentions binary representation.

### Core intuition

**XOR properties** (the key ones to memorize):
- `x ^ x = 0` — XOR with self cancels.
- `x ^ 0 = x` — XOR with 0 is identity.
- XOR is commutative and associative, so order of operations doesn't matter.

Consequence: XOR-ing all elements of an array where every element appears twice except one leaves the unpaired element. O(N) time, O(1) space.

**Common bit tricks:**
- `x & (x - 1)` clears the lowest set bit.
- `x & -x` isolates the lowest set bit.
- Counting bits: iterate `x & (x-1)` until 0.
- Check power of two: `x > 0 and (x & (x - 1)) == 0`.

### Python template

**Find unique element in array of pairs:**

```python
def solution(A: list[int]) -> int:
    result = 0
    for x in A:
        result ^= x
    return result
```

### Common variations

- **Two unique numbers in array of pairs**: XOR all to get `a ^ b`. Find any set bit of `a ^ b` to partition into two groups.
- **Count set bits**: `bin(x).count('1')` in Python, or `x.bit_count()` in 3.10+.
- **Subset generation**: for mask in range(1 << n): `subset = [A[i] for i in range(n) if mask & (1 << i)]`.

### Pitfalls

- Python integers are arbitrary precision — no overflow, but watch for negative numbers in `&` and `~`.
- XOR solutions assume exactly *one* unique; breaks if counts differ.

### Problems in this repo

`arrays/odd_occurrences_in_array`.

---

## Appendix: Quick Pattern Lookup Table

| Problem phrasing contains... | Likely pattern |
|---|---|
| "sum/count in range [L, R]", many queries | Prefix sums (§1) |
| "max product of three", "count distinct" | Sorting (§2) |
| "balanced brackets", "fish eating" | Stack (§3) |
| "next greater element" | Monotonic stack (§3) |
| "sorted array, find target" | Binary search classical (§4) |
| "min K such that...", "min max" / "max min" | Binary search on answer (§4) |
| "two sum on sorted array", "pair summing to X" | Two pointers (§5) |
| "longest subarray with property" | Caterpillar / sliding window (§5, §6) |
| "max in every window of size K" | Monotonic deque (§6) |
| "minimum number to cover / achieve" | Greedy (§7) |
| "maximum contiguous subarray sum" | Kadane (§8) |
| "element appearing > N/2 times" | Boyer-Moore (§9) |
| "count ways", "min cost to..." | Dynamic programming (§10) |
| "can partition into subsets summing to X" | 0/1 knapsack DP (§10) |
| "tree depth / validate / traverse" | Tree BFS/DFS (§11) |
| "shortest path unweighted" | BFS (§12) |
| "shortest path weighted, non-negative" | Dijkstra (§12) |
| "detect cycle in graph" | DFS coloring or Union-Find (§12) |
| "course prerequisites", "ordering" | Topological sort (§12) |
| "count primes / semiprimes" | Sieve of Eratosthenes (§13) |
| "GCD", "periodic", "cycles around" | Euclidean algorithm (§13) |
| "x^n efficiently" | Binary exponentiation (§13) |
| "find unique element, rest in pairs" | XOR (§14) |

## Appendix: How to approach an unseen problem

1. **Read carefully.** Note every constraint (N, value ranges, time limit hints).
2. **Map constraints to complexity.** N ≤ 20 → maybe brute force or bitmask DP. N ≤ 10^3 → O(N²). N ≤ 10^5 → O(N log N). N ≤ 10^7 → O(N). N ≤ 10^9 → O(log N) or O(1).
3. **Spot signals** from the pattern tables above.
4. **Commit to a pattern.** Write the template from memory, then adapt to the problem.
5. **Dry-run on a small example** before coding.
6. **Code, test, run against examples, run against edge cases, run against performance tests.**

If you're stuck for more than ~20 minutes: re-read the problem. The key signal is often in a phrase you skimmed past.
