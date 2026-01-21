# Fixed Window Sliding Window

## 🔹 Pattern Overview

Use this pattern when the window size is **constant** and slides one step at a time.

---

## 🔍 How to Identify (Tells)

* "subarray of size k"
* "window of length k"
* "every window of size k"
* window size never changes

Examples phrases:

* "maximum sum of any subarray of size k"
* "first negative number in every window of size k"

---

## 🧠 Mental Model (Say This in Interviews)

> "I keep a running window of exactly k elements. Each step I add the right element and remove the left element."

---

## 🧩 Canonical Template

```python
l = 0
window = 0

for r in range(len(nums)):
    window += nums[r]

    if r - l + 1 == k:
        update_answer(window)
        window -= nums[l]
        l += 1
```

---

## 🧩 Deque-Based Fixed Window (Max / Min / First Valid)

### When to Use a Deque

Use a deque when the problem asks for:

* maximum / minimum in every window
* first negative / first positive in every window
* monotonic behavior across the window

### 🧠 Mental Model

> "I maintain a deque that stores **useful candidates** for the current window while discarding irrelevant ones."

### 🔥 Deque Template (Monotonic Queue)

```python
from collections import deque

dq = deque()
l = 0

for r in range(len(nums)):
    # Remove elements outside the window
    while dq and dq[0] < l:
        dq.popleft()

    # Maintain monotonic decreasing order
    while dq and nums[dq[-1]] <= nums[r]:
        dq.pop()

    dq.append(r)

    if r - l + 1 == k:
        answer.append(nums[dq[0]])
        l += 1
```

### 🔥 First Negative Number Template

```python
from collections import deque

dq = deque()  # stores indices of negative numbers
l = 0

for r in range(len(nums)):
    if nums[r] < 0:
        dq.append(r)

    if r - l + 1 == k:
        if dq and dq[0] >= l:
            answer.append(nums[dq[0]])
        else:
            answer.append(0)
        l += 1
```

```python
l = 0
window = 0

for r in range(len(nums)):
    window += nums[r]

    if r - l + 1 == k:
        update_answer(window)
        window -= nums[l]
        l += 1
```

---

## 🔥 Problems Using This Pattern

### ➤ Sum / Count Based

* max_sum_subarray_of_size_k
* maximum-sum-of-distinct-subarrays-with-length-k

### ➤ Deque / Monotonic Queue Based

* sliding-window-maximum
* first-negative-integer-in-every-window-of-size-k
* sliding-subarray-beauty

---

## ⚠️ Common Pitfalls

* Off-by-one errors (`r - l + 1`)
* Forgetting to remove `nums[l]`
* Using `if` instead of checking exact window size
* Not using deque when max/min is required

---

## ⏱ Time & Space Complexity

* Time: O(n)
* Space: O(1) or O(k) depending on data structure

---

## ✅ Key Insight

The window **never shrinks or grows arbitrarily** — it always stays size k.

If the window size changes → this is NOT fixed window.
