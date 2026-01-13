

# 🟦  **Combinations / Subsets**

---

## What is this category?

This category is about **choosing elements**, not ordering them.

* You are deciding **which elements to include**
* Order **does NOT matter**
* You usually move forward using an **index**
* This is the most common form of backtracking

Think:

> “Pick or don’t pick”
> “Include this number or skip it”

---

## What does this technique do?

* Explores all possible **combinations or subsets**
* Ensures no duplicates (when required)
* Handles:

  * Unlimited reuse of elements
  * Single-use elements
  * Fixed-size selections (choose k)

---

## How to know a problem belongs here (Tells)

Look for phrases like:

* “All possible combinations”
* “Return all subsets”
* “Choose k elements”
* “Each number can be used once / unlimited times”
* “The order of numbers does not matter”
* “No duplicate combinations”

🚨 **Key tell:**
If `[2,3]` and `[3,2]` are considered the **same**, this is **combinations**, not permutations.

---

## Core Backtracking Pattern (Mental Model)

At each step:

1. Decide whether to **take** the current element
2. Move forward to the **next index**
3. Backtrack (undo the choice)

---

## Template Code (Combinations / Subsets)

### Base Template (No Duplicates)

```python
def backtrack(start, path):
    res.append(path[:])
    
    for i in range(start, len(nums)):
        path.append(nums[i])
        backtrack(i + 1, path)
        path.pop()
```

Call with:

```python
res = []
backtrack(0, [])
return res
```

---

## Template: Combination Sum (Unlimited Use)

```python
def backtrack(start, path, total):
    if total == target:
        res.append(path[:])
        return
    if total > target:
        return

    for i in range(start, len(nums)):
        path.append(nums[i])
        backtrack(i, path, total + nums[i])  # reuse allowed
        path.pop()
```

---

## Template: Combination Sum II (No Reuse, Handle Duplicates)

```python
nums.sort()

def backtrack(start, path, total):
    if total == target:
        res.append(path[:])
        return
    if total > target:
        return

    for i in range(start, len(nums)):
        if i > start and nums[i] == nums[i - 1]:
            continue  # skip duplicates
        path.append(nums[i])
        backtrack(i + 1, path, total + nums[i])
        path.pop()
```

---

## Things to Always Watch Out For

### 1. Start Index

* `start` prevents reusing earlier elements
* Controls **combination vs permutation**

### 2. Duplicate Handling

* Sort input first
* Skip duplicates using:

  ```python
  if i > start and nums[i] == nums[i - 1]:
      continue
  ```
### 3. Unlimited Use vs No Reuse

* Unlimited use

  ```python
  baktrack(i,path)
  ```
  
* No Reuse

  ```python
  baktrack(i+1,path)
  ```

### 4. Copy the Path

* Always append `path[:]`, **not `path`**

### 5. Pruning

* Stop recursion early when:

  * Sum exceeds target
  * Length exceeds k

---

## Problems That Use This Template

(From your list)

* `subsets.py`
* `subsets-ii.py`
* `combination-sum.py`
* `combination-sum-ii.py`
* `combination-sum-iii.py`
* `closest-dessert-cost.py`

---

## One-Line Recognition Rule

> If the problem is about **choosing elements**, order doesn’t matter, and you move forward with an index → **Combination Backtracking**.

---

