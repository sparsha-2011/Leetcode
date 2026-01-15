# 🔹 Subset Partitioning 

---

## 1️⃣ How to IDENTIFY this category (tells)

If the problem says any of the following, it is **subset / bucket partitioning**:

### 🔍 Problem tells

* “Divide the array into k subsets…”
* “Assign elements to groups / buckets…”
* “Each subset must satisfy…”
* “All subsets have equal sum / size / property…”
* “Use each element exactly once”

### Key characteristics

* Subsets are **not contiguous**
* Order **does not matter**
* Elements can be picked in **any order**

### 🚫 NOT string partitioning if:

* There is **no left → right index progression**
* Order of elements is irrelevant

---

## 2️⃣ Core mental model (say this in interviews)

> **“I assign each element to one of k buckets while maintaining constraints, and backtrack if any bucket becomes invalid.”**

This sentence alone often gets interviewer nods.

---

## 3️⃣ Canonical backtracking structure

### State variables

* `i` → index of element to assign
* `buckets` → current sums (or contents) of k subsets

### Skeleton (MOST IMPORTANT)

```python
def backtrack(i):
    if i == len(nums):
        return True   # all elements assigned successfully

    for b in range(k):
        if can_place(nums[i], b):
            place(nums[i], b)
            if backtrack(i + 1):
                return True
            unplace(nums[i], b)

    return False
```

---

## 4️⃣ Concrete template (equal-sum k subsets)

```python
def canPartitionKSubsets(nums, k):
    total = sum(nums)
    if total % k != 0:
        return False

    target = total // k
    nums.sort(reverse=True)          # 🔥 huge pruning
    buckets = [0] * k

    def backtrack(i):
        if i == len(nums):
            return True

        for b in range(k):
            if buckets[b] + nums[i] <= target:
                buckets[b] += nums[i]

                if backtrack(i + 1):
                    return True

                buckets[b] -= nums[i]

            # 🔥 symmetry pruning
            if buckets[b] == 0:
                break

        return False

    return backtrack(0)
```

---

## 5️⃣ Critical pruning rules (memorize these)

### ✅ 1. Sort descending

```python
nums.sort(reverse=True)
```

**Why:**

* Large numbers fail faster
* Reduces branching dramatically

---

### ✅ 2. Skip symmetric empty buckets

```python
if buckets[b] == 0:
    break
```

**Why:**

* All empty buckets are identical
* Prevents k! duplicate states

---

### ✅ 3. Early impossible checks

```python
if nums[0] > target:
    return False
```

---

## 6️⃣ Alternative formulation (fill ONE bucket at a time)

Sometimes cleaner:

```python
def backtrack(start, curr_sum, buckets_left):
    if buckets_left == 1:
        return True
    if curr_sum == target:
        return backtrack(0, 0, buckets_left - 1)

    for i in range(start, len(nums)):
        if used[i]:
            continue
        if curr_sum + nums[i] > target:
            continue

        used[i] = True
        if backtrack(i + 1, curr_sum + nums[i], buckets_left):
            return True
        used[i] = False

    return False
```

This version is also very common in solutions.

---

## 7️⃣ Time complexity expectations (be honest)

* Worst case: **O(kⁿ)** (NP-complete)
* With pruning: works for **n ≤ 16**

👉 Interviewers care more about **pruning logic** than raw complexity.

---

## 8️⃣ Common pitfalls (watch out)

❌ Forgetting symmetry pruning
❌ Not sorting descending
❌ Using `return` instead of `continue` in loops
❌ Treating this like string partitioning
❌ Reusing elements accidentally

---

## 9️⃣ One-minute explanation (perfect interview answer)

> “This is a subset assignment backtracking problem. I sort the numbers in descending order and try assigning each number to one of k buckets while keeping the bucket sum under the target. I prune symmetric states by avoiding placing into identical empty buckets. If all numbers are placed successfully, I return true.”

---

## Problems to practice after this

### Must-do

* **698** Partition to K Equal Sum Subsets
* **473** Matchsticks to Square
* **2305** Fair Distribution of Cookies

### Optional (harder)

* **1655** Distribute Repeating Integers

---

## TL;DR cheat sheet

```
IF:
  - k subsets
  - non-contiguous
  - equal constraint
THEN:
  → bucket-filling backtracking

KEY IDEAS:
  - assign elements to buckets
  - prune aggressively
  - symmetry matters
```
