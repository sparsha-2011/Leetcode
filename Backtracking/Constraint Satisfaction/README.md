
# 🟦 BACKTRACKING TEMPLATE 4: **Constraint Satisfaction**



## What is this category?

You are **placing items** (numbers, queens, sticks, characters…) while obeying **global constraints**.

* Each choice affects future choices
* A choice can **invalidate** the entire path
* You must **undo** choices when backtracking

Classic “try → validate → recurse → undo”.

---

## How to recognize this category (Tells)

Look for phrases like:

* “Place X so that…”
* “No two can share…”
* “Must satisfy all constraints”
* “Valid board / configuration”
* “Return any / all valid arrangements”

🚨 **Big tell:**
You are filling a structure (grid, board, groups) and **checking conflicts**.

---

## Core Mental Model

1. Pick the **next position** to fill
2. Try all **valid candidates**
3. Check constraints
4. Place candidate
5. Recurse
6. Undo placement

---

## Universal Constraint Satisfaction Template

```python
def backtrack(state):
    if isComplete(state):
        recordSolution(state)
        return

    for choice in getChoices(state):
        if isValid(choice, state):
            apply(choice, state)
            backtrack(state)
            undo(choice, state)
```

---

## Template: Grid / Board Placement

(N-Queens, Sudoku)

```python
def backtrack(r, c):
    if r == ROWS:
        res.append(copyBoard())
        return

    next_r, next_c = nextCell(r, c)

    for val in getCandidates(r, c):
        if isValid(r, c, val):
            place(r, c, val)
            backtrack(next_r, next_c)
            remove(r, c, val)
```

---

## Template: Row-by-Row Placement

(N-Queens optimized)

```python
def backtrack(row):
    if row == n:
        res.append(board.copy())
        return

    for col in range(n):
        if col not in cols and (row-col) not in diag1 and (row+col) not in diag2:
            cols.add(col)
            diag1.add(row-col)
            diag2.add(row+col)
            board[row] = col

            backtrack(row + 1)

            cols.remove(col)
            diag1.remove(row-col)
            diag2.remove(row+col)
```

---

## Template: Partition with Constraints

(Matchsticks to Square)

```python
def backtrack(i):
    if i == len(nums):
        return all(side == target for side in sides)

    for j in range(4):
        if sides[j] + nums[i] <= target:
            sides[j] += nums[i]
            if backtrack(i + 1):
                return True
            sides[j] -= nums[i]

    return False
```

---

## Constraint-Tracking Patterns (IMPORTANT)

### 🔹 Sets / Hashes

* Fast conflict checks

```python
rows, cols, boxes
```

### 🔹 Bitmask (advanced)

* Used in optimized Sudoku

### 🔹 Arrays for grouping

* `sides[4]`, `buckets[k]`

---

## Problems from Your List That Belong Here

* `n-queens.py`
* `sudoku-solver.py`
* `matchsticks-to-square.py`
* `word-search.py`
* `maximum-length-of-a-concatenated-string-with-unique-characters.py`

---

## Common Mistakes

❌ Forgetting to undo state
❌ Validity check after recursion
❌ Not pruning early
❌ Modifying shared state without copying

---

## Optimization Tricks (High Signal)

* Sort input (descending for matchsticks)
* Early pruning (break symmetric choices)
* Pre-calculate constraints
* Use sets instead of scanning arrays

---

## One-Line Recognition Rule

> If every choice affects future validity → **Constraint Satisfaction Backtracking**.

---


