

# 🟦 BACKTRACKING TEMPLATE 3: **String Partitioning / Construction**

---

## What is this category?

This category is about **building strings step-by-step** or **splitting a string into valid parts**.

* You move using a **string index**
* At each step, you decide:

  * where to **cut**
  * or what to **append**
* Every piece must satisfy a **validity rule**

Think:

> “How many ways can I build this string so every part is valid?”

---

## What does this technique do?

* Explores all ways to:

  * partition a string
  * generate valid strings
  * map characters to choices
* Uses DFS with:

  * `start index`
  * current path (list or string)

---

## How to know a problem belongs here (Tells)

Look for phrases like:

* “Generate all valid strings”
* “Partition the string”
* “Split into substrings”
* “Each part must be valid”
* “Return all possible ways”

🚨 **Key tell:**
You are **walking through a string by index** and making decisions at each position.

---

## Core Backtracking Pattern (Mental Model)

At index `i`:

1. Try all possible substrings starting at `i`
2. Check if the substring is valid
3. Recurse from the next index
4. Backtrack

---

## Template Code (String Partitioning)

```python
def backtrack(start, path):
    if start == len(s):
        res.append(path[:])
        return

    for end in range(start + 1, len(s) + 1):
        substring = s[start:end]
        if isValid(substring):
            path.append(substring)
            backtrack(end, path)
            path.pop()
```

---

## Template: Build Valid Strings (Counts / Balance)

Used for problems like **Generate Parentheses**.

```python
def backtrack(cur, openCount, closeCount):
    if len(cur) == 2 * n:
        res.append(cur)
        return

    if openCount < n:
        backtrack(cur + "(", openCount + 1, closeCount)

    if closeCount < openCount:
        backtrack(cur + ")", openCount, closeCount + 1)
```

---

## Template: Fixed-Length Segment Construction

(Example: Restore IP Addresses)

```python
def backtrack(start, path):
    if len(path) == 4:
        if start == len(s):
            res.append(".".join(path))
        return

    for length in range(1, 4):
        if start + length > len(s):
            break
        segment = s[start:start + length]
        if isValid(segment):
            path.append(segment)
            backtrack(start + length, path)
            path.pop()
```

---

## Things to Always Watch Out For

### 1️⃣ Index Control

* `start` must move forward
* Never revisit earlier characters

### 2️⃣ Validity Check

* **Always validate before recursing**
* Example checks:

  * Palindrome
  * Length
  * Leading zeros
  * Character constraints

### 3️⃣ Base Case

* Reached end of string
* OR used required number of segments

### 4️⃣ String vs List

* Use **list** for path
* Join at the end for performance

---

## Problems That Use This Template

(From your list)

* `generate-parentheses.py`
* `restore-ip-addresses.py`
* `palindrome-partitioning.py`
* `letter-combinations-of-a-phone-number.py`

---

## One-Line Recognition Rule

> If you move through a string by index and each piece must be valid → **String Partitioning Backtracking**.

---



Say **“Constraint Satisfaction”** when ready 👍
