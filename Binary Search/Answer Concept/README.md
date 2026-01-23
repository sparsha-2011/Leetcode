
# 📘 Binary Search on Answer

## 🔹 Pattern Overview

This pattern applies when you’re **searching over a range of possible answers** instead of searching a sorted array directly.
Instead of binary-searching a sorted input list, you binary search the **answer space** based on a *feasible / infeasible decision check*.

---

## 🔍 How to Identify (Tells)

Use this when a problem says something like:

* “minimize the **maximum** ...”
* “maximize the **minimum** ...”
* “find the **smallest/least** value that satisfies a condition”
* “find the **largest** value where a condition still holds”
* “find the minimum time ...”
* “given an answer guess, check feasibility”
* The search space is not the array itself but a **number range**

Examples patterns:

```
true true true false false
false false true true true
```

---

## 🧠 Mental Model (Interview-Ready)

> **“I binary search the answer space. At each guess `mid`, I check `feasible(mid)`. If it’s possible with `mid`, I move to the left/right half depending on whether I want the smallest or largest feasible answer.”**

This sentence alone demonstrates the right pattern.

---

## 🧩 Core Template (Binary Search on Answer Space)

```python
left, right = lower_bound, upper_bound
best = default_answer

while left <= right:
    mid = (left + right) // 2

    if feasible(mid):
        best = mid                # mid is a valid answer
        right = mid - 1          # try to minimize
        # OR left = mid + 1       # try to maximize
    else:
        left = mid + 1          # mid not feasible

return best
```

Depending on maximize/minimize, the update of `left`/`right` changes.

---

## 🧩 Feasible Function

This is the core helper:

```python
def feasible(x) -> bool:
    # returns True if x is good / valid
    # False otherwise
```

You must prove *monotonicity*:

* If `feasible(x)` is True → smaller (or larger) values may also be feasible
* If `feasible(x)` is False → larger (or smaller) values are never feasible

---

## 🔥 Included Problems (with Binary Search on Answer)

✔ **allocation / splitting problems**

* allocate-minimum-number-of-pages.py
* split-array-largest-sum.py
* koko-eating-bananas.py

✔ **repair / time scheduling**

* minimum-time-to-repair-cars.py (LeetCode 2594) ([AlgoMonster][1])

✔ **maximization with feasibility check**

* maximum-candies-allocated-to-k-children.py (LeetCode 2226) ([AlgoMonster][2])

---

## 🧠 Decision Heuristics (how to choose bounds)

### 💡 Common Lower/Upper Bounds

| Problem Type      | Lower Bound        | Upper Bound         |
| ----------------- | ------------------ | ------------------- |
| Time minimization | 0                  | `max_possible_time` |
| Allocation        | 0                  | `max_element`       |
| Split sums        | `max single piece` | sum of all pieces   |

Adjust based on problem semantics.

---

## 🧠 Example Story (How It Works)

Suppose you want the **minimum time** to finish a task:

* If `feasible(t)` → you can finish in `t` time → try a **smaller** time
* If not → you need more time → try a **larger** time

This creates a **monotonic feasibility pattern** that binary search can exploit.

---

## ⚠️ Interview Pitfalls

❌ Forgetting to prove feasibility monotonicity
❌ Wrong bounds (e.g., upper bound too low)
❌ Updating `left`/`right` incorrectly for maximize/minimize
❌ Off-by-one in feasible logic

---

## ⏱ Complexity

* **Time:** O(log(answer_range) × cost of feasibility check)
* **Space:** O(1)

Example:

* repairing cars: `O(n log T)` where `T` is max time bound ([AlgoMonster][1])
* maximum candies: `O(n log C)` where `C = max(candies)` ([AlgoMonster][2])


