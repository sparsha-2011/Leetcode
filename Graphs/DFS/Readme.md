
---

# Depth First Search (DFS)

---

## 1️⃣ What is DFS? What does it do?

**Depth First Search (DFS)** is a graph traversal technique that explores a path as deeply as possible before backtracking.

In graph problems, DFS is most commonly used to:

* Explore **connected components**
* Perform **flood fill**
* Check **reachability**
* Aggregate information over a component (area, perimeter, validity)

DFS is especially natural for **grid-based problems**, where each cell can be treated as a node connected to its neighbors.

---

## 2️⃣ How to know if a problem can be solved using DFS

A graph problem is a good candidate for DFS if:

* You need to **fully explore** a region or component before moving on
* The order of traversal **does not matter**
* You are not asked for the *shortest* or *minimum* path
* You need to **count**, **mark**, or **accumulate** over connected nodes

DFS works well when the question asks *“what exists?”* rather than *“what is the minimum?”*.

---

## 3️⃣ General tells to look for in the problem statement

Look for phrases like:

* “island”, “region”, “area”, “connected”
* “surrounded by”, “reachable from”
* “count the number of…”
* “find all cells that…”
* “mark visited cells”

Structural tells:

* Input is a **2D grid**
* Movement is limited to **up / down / left / right**
* No weights or costs involved

---

## 4️⃣ DFS Template (Grid-Based)

This is the **canonical DFS template** used in most grid problems.

```python
ROWS, COLS = len(grid), len(grid[0])
visited = set()
directions = [(1,0), (-1,0), (0,1), (0,-1)]

def dfs(r, c):
    # Edge conditions
    if r < 0 or c < 0 or r >= ROWS or c >= COLS:
        return
    if (r, c) in visited:
        return

    # Problem-specific invalid condition
    if grid[r][c] == '0':   # or water, wall, etc.
        return

    visited.add((r, c))

    for dr, dc in directions:
        dfs(r + dr, c + dc)
```

### Key points to notice

* **Edge conditions first**
* **Visited check early**
* **Problem-specific invalid condition included**
* Directions list avoids repeated code
* DFS explores the entire component before returning

---

## 5️⃣ Problems That Use DFS

Below are the problems from your list that naturally fall under DFS.

---

### 🟩 `number-of-islands.py`

**Problem summary:**
Given a grid of land (`1`) and water (`0`), count how many distinct islands exist. An island is a group of adjacent land cells connected horizontally or vertically.

**DFS tells from the statement:**

* “Count the number of islands”
* “An island is surrounded by water”
* “Connected horizontally or vertically”

These phrases clearly indicate **connected component counting**, which is a textbook DFS use case.

---

### 🟩 `max-area-of-island.py`

**Problem summary:**
Given a grid of land and water, find the maximum area of any island. Area is defined as the number of land cells in the island.

**DFS tells from the statement:**

* “Area of an island”
* “Connected 1s”
* Need to **fully explore** an island to compute its size

DFS allows you to traverse the entire island and accumulate its area.

---

### 🟩 `island-perimeter.py`

**Problem summary:**
Given a grid representing a single island, calculate the perimeter of the island.

**DFS tells from the statement:**

* “Island in a grid”
* “Perimeter depends on adjacent cells”
* Requires visiting every land cell exactly once

DFS lets you visit all land cells and check neighbors to compute perimeter.

---

### 🟩 `surrounded-regions.py`

**Problem summary:**
Capture all regions surrounded by `X` by flipping surrounded `O`s to `X`.

**DFS tells from the statement:**

* “Surrounded by”
* “Reachable from the border”
* Need to mark regions that should *not* be flipped

DFS is used to mark all `O`s connected to the boundary.

---

### 🟩 `pacific-atlantic-water-flow.py`

**Problem summary:**
Find all grid cells from which water can flow to both the Pacific and Atlantic oceans.

**DFS tells from the statement:**

* “Water can flow from cell to cell”
* “Reachable from ocean”
* Requires exploring all possible paths from boundaries

DFS is ideal for reachability problems without path optimization.

---

## 6️⃣ What DFS is **not** good for (Important)

DFS is **not** appropriate when:

* The problem asks for **minimum steps**
* The graph has **weights**
* You need the **shortest or cheapest path**

In those cases, BFS or Dijkstra is more appropriate.

---

## 7️⃣ Mental Checklist for DFS

Before coding, ask yourself:

* Am I exploring a whole region/component?
* Do I need to mark visited nodes?
* Is traversal order irrelevant?
* Am I aggregating information over connected nodes?

If yes → **DFS is likely the correct tool.**


