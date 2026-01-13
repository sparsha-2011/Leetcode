

# 🧠 Master Categorization: Backtracking / Search Problems

---

## 🟦 1. Backtracking — Combination / Subset Generation

> *Choose or skip elements; order usually does NOT matter*

### Core idea

* At each step: **include or exclude**
* Use **index-based recursion**
* Often involves **duplicates handling**

### Problems

* `subsets.py`
* `subsets-ii.py`
* `combination-sum.py`
* `combination-sum-ii.py`
* `combination-sum-iii.py`
* `closest-dessert-cost.py`

### Tells in the problem

* “All possible combinations”
* “Choose k numbers”
* “Each number can be used once / unlimited times”
* “No duplicate combinations”

---

## 🟦 2. Backtracking — Permutations / Ordering

> *Order matters*

### Core idea

* Try every unused element
* Track **used[] or visited**
* Often factorial complexity

### Problems

* `permutations.py`
* `permutations-ii.py`
* `letter-tile-possibilities.py`
* `number-of-squareful-arrays.py`

### Tells in the problem

* “All permutations”
* “Rearrangements”
* “Distinct permutations”
* “Different sequences count separately”

---

## 🟦 3. Backtracking — String Partitioning / Construction

> *Build strings step by step*

### Core idea

* DFS over string indices
* Decide where to cut or what to append
* Often uses **validity checks**

### Problems

* `generate-parentheses.py`
* `restore-ip-addresses.py`
* `palindrome-partitioning.py`
* `letter-combinations-of-a-phone-number.py`

### Tells in the problem

* “Generate all valid strings”
* “Partition the string”
* “Every part must be valid”
* “Return all possible ways”

---

## 🟦 4. Backtracking — Constraint Satisfaction

> *Place things while respecting rules*

### Core idea

* Try placements
* Backtrack when constraints violated
* Often uses **sets / bitmasks**

### Problems

* `n-queens.py`
* `sudoku-solver.py`
* `matchsticks-to-square.py`
* `maximum-length-of-a-concatenated-string-with-unique-characters.py`

### Tells in the problem

* “Place without conflict”
* “Each row / column / group must be unique”
* “Can we form / arrange / fill?”
* “Return true/false or one valid configuration”

---

## 🟦 5. Backtracking on Graph / DAG Paths

> *Explore all paths*

### Core idea

* DFS from source
* Track current path
* Backtrack after visiting neighbors

### Problems

* `all-paths-from-source-to-target.py`

### Tells in the problem

* “All paths”
* “Source to target”
* Graph given as adjacency list
* DAG or acyclic graph

---

# 📌 Final Clean Mapping

| Category                               | Problems                                                                                 |
| -------------------------------------- | ---------------------------------------------------------------------------------------- |
| **Combinations / Subsets**             | subsets, subsets-ii, combination-sum (I/II/III), closest-dessert-cost                    |
| **Permutations**                       | permutations, permutations-ii, letter-tile-possibilities, number-of-squareful-arrays     |
| **String Construction / Partitioning** | generate-parentheses, restore-ip-addresses, palindrome-partitioning, letter-combinations |
| **Constraint Satisfaction**            | n-queens, sudoku-solver, matchsticks-to-square, max-length-unique-concat                 |
| **Graph Path Enumeration**             | all-paths-from-source-to-target                                                          |

---

# 🧩 Interview Insight (Important)

Although **everything here is “backtracking”**, interviewers expect you to recognize **which flavor**:

* **Choose vs order**
* **String vs numbers**
* **Validation heavy vs free exploration**
* **Graph vs array**

This lets you **instantly reach for the right template**.

---

