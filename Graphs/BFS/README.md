
#  Breadth First Search (BFS)



## 1️⃣ What is BFS? What does it do?

**Breadth First Search (BFS)** is a graph traversal technique that explores nodes **level by level**, visiting all neighbors at the current depth before moving deeper.

In graph problems, BFS is primarily used to:

* Find the **shortest path in an unweighted graph**
* Model **spreading processes** over time
* Traverse state spaces where each move has **equal cost**

BFS guarantees the **minimum number of steps** because it explores all nodes at distance `d` before any node at distance `d + 1`.

---

## 2️⃣ How to know if a problem can be solved using BFS

A problem is a strong candidate for BFS if:

* Each move/edge has the **same cost**
* You are asked for the **minimum number of steps**, moves, or time
* The process expands outward uniformly
* The problem naturally maps to **levels**

BFS answers *“How fast can I get there?”* rather than *“What exists?”*.

---

## 3️⃣ General tells to look for in the problem statement

Look for phrases like:

* “minimum number of steps”
* “shortest path”
* “minimum time”
* “in how many moves”
* “each move takes 1 minute”

Structural tells:

* State-space problems (locks, words, configurations)
* Grid problems where time spreads outward
* No edge weights (or all weights = 1)

If you see **time passing uniformly**, think BFS.

---

## 4️⃣ BFS Template (Level-by-Level)

This is the **canonical BFS template** used in shortest-path problems.

```python
from collections import deque

queue = deque([start])
visited = set([start])
steps = 0

while queue:
    for _ in range(len(queue)):   # process one level
        node = queue.popleft()

        if node == target:
            return steps

        for nei in neighbors(node):
            if nei not in visited:
                visited.add(nei)
                queue.append(nei)

    steps += 1
```

### Key points to notice

* `for _ in range(len(queue))` enforces **level separation**
* `steps` increases **after** each level
* `visited` is updated when enqueuing (not dequeuing)
* Ensures shortest path by construction

---

## 5️⃣ Problems That Use BFS

Below are the problems from your list that are best solved using BFS.

---

### 🟦 `word-ladder.py`

**Problem summary:**
Transform a begin word into an end word by changing one letter at a time, with each intermediate word existing in a given dictionary. Return the minimum number of transformations.

**BFS tells from the statement:**

* “Minimum number of transformations”
* “Each transformation changes exactly one letter”
* All transformations have equal cost

This is a classic **shortest path in an unweighted graph** problem.

---

### 🟦 `open-the-lock.py`

**Problem summary:**
Given a lock with 4 wheels, find the minimum number of moves required to reach a target combination while avoiding deadends.

**BFS tells from the statement:**

* “Minimum number of turns”
* Each action changes one wheel by ±1
* Uniform cost per move

This is a state-space BFS where each lock configuration is a node.

---


### 🟦 `rotting-oranges.py`

**Problem summary:**
Every minute, fresh oranges adjacent to rotten ones become rotten. Return the minimum time needed for all oranges to rot.

**BFS tells from the statement:**

* “Every minute”
* Spread happens simultaneously
* Time increases in discrete steps

This is a **multi-source BFS**, where all initially rotten oranges start at level 0.

---

### 🟦 `walls-and-gates.py`

**Problem summary:**
Fill each empty room with the distance to its nearest gate.

**BFS tells from the statement:**

* “Distance to nearest gate”
* All moves cost the same
* Multiple starting points (gates)

This is another **multi-source BFS**, expanding outward from all gates at once.

---

## 6️⃣ BFS vs DFS — Key Distinction

| DFS                               | BFS                       |
| --------------------------------- | ------------------------- |
| Explore fully before backtracking | Explore level by level    |
| Good for components               | Good for shortest paths   |
| Order doesn’t matter              | Order guarantees minimum  |
| No distance tracking              | Natural distance tracking |

If the problem says **“minimum”**, DFS is almost never correct.

---

## 7️⃣ What BFS is **not** good for

BFS is **not appropriate** when:

* Edge costs differ
* You must minimize a weighted value
* You must choose between paths with different penalties

In those cases, **Dijkstra** or **0–1 BFS** is required.

---

## 8️⃣ Mental Checklist for BFS

Before coding, ask:

* Does every move cost the same?
* Am I minimizing steps, moves, or time?
* Does the problem evolve level by level?

If yes → **BFS is the right tool.**

---


