

# 🟦 BACKTRACKING TEMPLATE 2: **Permutations / Ordering**



## What is this category?

This category is about **arranging elements in different orders**.

* You must consider **every possible ordering**
* Order **DOES matter**
* `[1,2]` and `[2,1]` are **different results**

Think:

> “What comes next in the sequence?”



## What does this technique do?

* Generates all possible **permutations**
* Handles:

  * Distinct elements
  * Duplicate elements (unique permutations)
* Ensures each element is used **exactly once per path**



## How to know a problem belongs here (Tells)

Look for phrases like:

* “All permutations”
* “All possible arrangements”
* “Reorder the array”
* “Different sequences count separately”
* “Return all unique permutations”

🚨 **Key tell:**
If `[a,b]` and `[b,a]` are considered **different**, this is **permutations**, not combinations.

---

## Core Backtracking Pattern (Mental Model)

At each step:

1. Try **every unused element**
2. Mark it as used
3. Recurse
4. Unmark it (backtrack)

---

## Template Code (Permutations – No Duplicates)

```python
def backtrack(path):
    if len(path) == len(nums):
        res.append(path[:])
        return

    for i in range(len(nums)):
        if used[i]:
            continue
        used[i] = True
        path.append(nums[i])
        backtrack(path)
        path.pop()
        used[i] = False
```

Call with:

```python
res = []
used = [False] * len(nums)
backtrack([])
return res
```

---

## Template: Permutations II (With Duplicates)

```python
nums.sort()
used = [False] * len(nums)

def backtrack(path):
    if len(path) == len(nums):
        res.append(path[:])
        return

    for i in range(len(nums)):
        if used[i]:
            continue
        if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
            continue  # skip duplicate permutations

        used[i] = True
        path.append(nums[i])
        backtrack(path)
        path.pop()
        used[i] = False
```

---

## Things to Always Watch Out For

### 1️⃣ Used Array

* Required to prevent reuse in same permutation
* Distinguishes permutations from combinations

### 2️⃣ Duplicate Skipping Rule

```python
if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
    continue
```

* Prevents same ordering from being generated multiple times

### 3️⃣ Base Case

* `len(path) == len(nums)` → complete permutation

---

## Problems That Use This Template

(From your list)

* `permutations.py`
* `permutations-ii.py`
* `letter-tile-possibilities.py`
* `number-of-squareful-arrays.py`

---

## One-Line Recognition Rule

> If the problem is about **arranging all elements in different orders** → **Permutation Backtracking**.

---

