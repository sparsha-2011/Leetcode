# Variable Window Sliding Window

## 🔹 Pattern Overview

Use this pattern when the window size is **dynamic** and depends on constraints rather than a fixed length.

---

## 🔍 How to Identify (Tells)

If the problem says any of the following, it is **variable window**:

* "longest / shortest substring"
* "at most k"
* "no more than k distinct"
* "minimum window"
* "maximize / minimize while satisfying condition"

Key signal:

> The window **expands and shrinks** based on a condition.

---

## 🧠 Core Mental Model (Say This in Interviews)

> "I expand the window by moving the right pointer, and when the constraint is violated, I shrink from the left until it becomes valid again."

This sentence alone signals mastery.

---

## 🧩 Canonical Variable Window Template

```python
l = 0
freq = {}

for r in range(len(s)):
    freq[s[r]] = freq.get(s[r], 0) + 1

    while constraint_violated(freq):
        freq[s[l]] -= 1
        if freq[s[l]] == 0:
            del freq[s[l]]
        l += 1

    update_answer(l, r)
```

---

## 🔥 Common Constraint Patterns

### ➤ At Most K Distinct

```python
while len(freq) > k:
    freq[s[l]] -= 1
    if freq[s[l]] == 0:
        del freq[s[l]]
    l += 1
```

### ➤ No Repeating Characters

```python
while freq[s[r]] > 1:
    freq[s[l]] -= 1
    l += 1
```

### ➤ Character Replacement (Max Frequency Trick)

```python
while (r - l + 1) - max_freq > k:
    freq[s[l]] -= 1
    l += 1
```

---

## 🔥 Problems Using This Pattern

### ➤ Distinct / Frequency Based

* longest-substring-without-repeating-characters
* longest-k-unique-characters-substring
* fruit-into-baskets

### ➤ Optimization Based

* longest_repeating_character_replacement
* minimum_window_substring

---

## ⚠️ Common Pitfalls

* Using `if` instead of `while` to shrink
* Updating the answer before the window is valid
* Forgetting to clean up zero-count keys
* Misunderstanding "at most" vs "exactly"

---

## ⏱ Time & Space Complexity

* Time: O(n)
* Space: O(1) to O(σ), where σ is alphabet size

---

## ✅ Key Insight

Right pointer always moves forward.
Left pointer only moves forward.

➡️ Total operations remain linear.

If the window size does NOT depend on constraints → this is NOT variable window.
