# Algorithms Practice

A focused Python environment for solving **Codility / LeetCode** problems locally with fast feedback via `pytest`.

---

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## Run Tests

```bash
# Run all problems
pytest

# Run a specific problem
pytest problems/arrays/cyclic_rotation/

# Run and stop on first failure
pytest -x
```

---

## Repository Structure

```
algorithms/
├── problems/
│   ├── _template/          # Copy this for every new problem
│   │   ├── solution.py
│   │   └── test_solution.py
│   │
│   └── arrays/             # Group by topic (arrays, dp, graphs, …)
│       └── cyclic_rotation/
│           ├── solution.py
│           └── test_solution.py
│
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## Adding a New Problem

1. Create a folder under the relevant topic:
   ```
   problems/<topic>/<problem_name>/
   ```
2. Copy the template files:
   ```bash
   cp -r problems/_template/* problems/<topic>/<problem_name>/
   touch problems/<topic>/__init__.py
   touch problems/<topic>/<problem_name>/__init__.py
   ```
3. Fill in `solution.py` and write your test cases in `test_solution.py`.
4. Run `pytest` to verify.

---

## Pytest Configuration (`pytest.ini`)

| Setting | Value | Purpose |
|---|---|---|
| `testpaths` | `problems/` | Only looks here for tests |
| `timeout` | `10s` | Simulates Codility's time limit |
| `--tb=short` | — | Clean, readable failure output |

---

## Topics to Organise By

```
problems/
├── arrays/
├── strings/
├── linked_lists/
├── trees/
├── graphs/
├── dynamic_programming/
├── binary_search/
├── sorting/
├── heaps/
└── math/
```
