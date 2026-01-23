

# 📘 Classic Binary Search (Index-Based & Boundary Search)

## 🔹 Pattern Overview

This category covers **binary search directly on sorted data** (or logically sorted data) where you are:

* Searching for an **element**
* Finding **first / last occurrence**
* Finding **floor / ceil**
* Finding **peak / minimum / rotation point**
* Searching in **rotated, infinite, or special arrays**

Unlike *Binary Search on Answer*, here you are **searching indices**, not guessing answers.

---

## 🔍 How to Identify (Tells)

Use **Classic Binary Search** when:

* The input is **sorted** (or partially sorted / rotated / bitonic)
* You can compare `arr[mid]` with a target
* The answer is an **index or element**
* The problem explicitly mentions:

  * “sorted array”
  * “rotated sorted array”
  * “first / last occurrence”
  * “find minimum / peak”
  * “infinite sorted array”
  * “2D matrix with sorted rows/cols”

---

## 🧠 Mental Model

> **“I’m narrowing down the index range by comparing `arr[mid]` with the target or its neighbors.”**

Classic binary search always works on **indices**, not on an abstract answer space.

---

## 🧩 Core Binary Search Template (Exact Match)

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

---

## 🧩 Boundary Binary Search Templates

### ✅ First Occurrence

```python
def first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            ans = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return ans
```

---

### ✅ Last Occurrence

```python
def last_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            ans = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return ans
```

---

### ✅ Floor (Greatest ≤ target)

```python
def find_floor(arr, target):
    left, right = 0, len(arr) - 1
    res = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] <= target:
            res = arr[mid]
            left = mid + 1
        else:
            right = mid - 1

    return res
```

---

### ✅ Ceil (Smallest ≥ target)

```python
def find_ceil(arr, target):
    left, right = 0, len(arr) - 1
    res = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] >= target:
            res = arr[mid]
            right = mid - 1
        else:
            left = mid + 1

    return res
```

---

## 🔥 Problems Covered in This Category

### 🔹 Standard / Boundary

* search-insert-position.py
* find-first-and-last-position-of-element-in-sorted-array.py
* number-of-occurrences.py
* find_floor.py
* find_ceil.py
* find-smallest-letter-greater-than-target.py

---

### 🔹 Rotated Sorted Array

* search-in-rotated-sorted-array.py
* find-minimum-in-rotated-sorted-array.py
* number-of-times-a-sorted-array-is-rotated.py

---

### 🔹 Peak / Bitonic

* find-peak-element.py
* find-element-bitonic-array.py
* find-in-mountain-array.py
* single-element-in-a-sorted-array.py

---

### 🔹 Infinite / Unknown Size

* first-occurrence-of-1-in-an-infinite-sorted-binary-array.py
* search-in-a-sorted-array-of-unknown-size.py

---

### 🔹 2D Binary Search

* search-a-2d-matrix-ii.py

---

### 🔹 Advanced

* closest-element-in-a-sorted-array.py
* median-of-two-sorted-arrays.py

---

## ⚠️ Common Mistakes

❌ Using `while left < right` incorrectly
❌ Forgetting to store answer in boundary problems
❌ Infinite loops due to bad pointer updates
❌ Mixing index search with answer search logic

---

## ⏱ Complexity

* **Time:** `O(log n)`
* **Space:** `O(1)`

---

## 🧠 Interview One-Liner

> “Since the array is sorted, I use binary search on indices. For boundary problems, I continue searching after finding a match to ensure I get the first or last valid index.”

---

## 🧩 Rule of Thumb

| Question Type  | Template               |
| -------------- | ---------------------- |
| Find element   | Exact match            |
| First / Last   | Boundary search        |
| Floor / Ceil   | Boundary search        |
| Rotated array  | Modified binary search |
| Peak / Bitonic | Compare neighbors      |


