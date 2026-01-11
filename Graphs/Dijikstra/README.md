

# Dijkstra’s Algorithm



## 1️⃣ What is Dijkstra? What does it do?

**Dijkstra’s Algorithm** is a graph algorithm used to find the **shortest path** from a starting node to all other nodes in a **weighted graph with non-negative weights**.

Key points:

* Unlike BFS, Dijkstra handles **variable edge weights**.
* Guarantees **minimum total cost** to reach a node.
* Can be implemented with a **priority queue (min-heap)** for efficiency.
* Can also be adapted to **minimax problems** where path cost is defined as **max edge weight along the path** (e.g., `swim-in-rising-water.py`).

---

## 2️⃣ How to know if a problem can be solved using Dijkstra

A problem is a strong candidate for Dijkstra if:

* The graph is **weighted**, and weights are non-negative.
* You are asked for a **minimum cost, time, or effort** to reach a target.
* BFS is **not enough** because edge costs are unequal.
* Sometimes the problem involves **grids**, but the “cost” of moving depends on the cell (height, elevation, delay, etc.).

---

## 3️⃣ General tells to look for in the problem statement

Look for phrases like:

* “minimum cost”, “minimum time”, “minimum effort”
* “weights” on edges or grid cells
* “each move has a cost”
* “reach the destination with minimum …”

Structural tells:

* Weighted edges (either explicit or implied)
* Need to **track cumulative cost**
* Question may ask for **path to a specific node** or **all nodes**

If you see **weights + shortest path**, Dijkstra is almost always correct.

---

## 4️⃣ Dijkstra Template (Weighted Graph / Grid)

```python
import heapq

def dijkstra(start, graph):
    # graph[node] = list of (neighbor, weight)
    pq = [(0, start)]  # (cost, node)
    dist = {start: 0}
    visited = set()

    while pq:
        cost, node = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)

        for nei, w in graph[node]:
            new_cost = cost + w
            if new_cost < dist.get(nei, float('inf')):
                dist[nei] = new_cost
                heapq.heappush(pq, (new_cost, nei))

    return dist
```

### Grid / Minimax variant (used in `swim-in-rising-water.py`)

```python
import heapq

def minimax_dijkstra(grid):
    n = len(grid)
    pq = [(grid[0][0], 0, 0)]  # (time, r, c)
    visited = set()

    while pq:
        time, r, c = heapq.heappop(pq)
        if (r, c) in visited:
            continue
        visited.add((r, c))

        if r == n - 1 and c == n - 1:
            return time

        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                next_time = max(time, grid[nr][nc])
                heapq.heappush(pq, (next_time, nr, nc))
```

---

## 5️⃣ Problems That Use Dijkstra

Below are the problems from your list that are best solved using Dijkstra.

---

### 🟪 `network-delay-time.py`

**Problem summary:**
Given a network of nodes and travel times between nodes, determine the time it takes for a signal to reach all nodes from a source node.

**Dijkstra tells from the statement:**

* “Travel times” = weights on edges
* “Minimum time for signal” = shortest path
* Non-negative weights
* Need the **earliest arrival** at each node

---

### 🟪 `path-with-minimum-effort.py`

**Problem summary:**
Given a grid with heights, find a path from top-left to bottom-right such that the **maximum difference in heights along the path is minimized**.

**Dijkstra tells from the statement:**

* “Minimize maximum height difference” → minimax problem
* Grid treated as weighted graph
* Each move has a cost depending on the height difference

---

### 🟪 `swim-in-rising-water.py`

**Problem summary:**
Reach the bottom-right of a grid where each cell has a height. The minimum time required is the **max height along the path**.

**Dijkstra tells from the statement:**

* “Minimum time to reach destination”
* Weight = cell height
* Path cost = max along path → solved using **minimax Dijkstra**
* BFS is insufficient because edge “costs” differ

---

### 🟪 `cheapest-flights-within-k-stops.py`

**Problem summary:**
Find the cheapest flight from source to destination with at most `k` stops.

**Dijkstra tells from the statement:**

* “Cheapest flight” → weighted edges
* Edge weights = ticket prices
* Constraint on **number of stops** can be incorporated using a **modified Dijkstra / BFS with priority queue**
* Edge weights not uniform → BFS alone is not enough

---

## 6️⃣ Dijkstra vs BFS — Key Distinction

| BFS                    | Dijkstra                      |
| ---------------------- | ----------------------------- |
| Unweighted graph       | Weighted graph (non-negative) |
| Each move costs 1      | Each move has a cost          |
| Shortest path in steps | Shortest path in total cost   |
| Simple queue           | Priority queue (min-heap)     |

**Rule of thumb:**

> If BFS doesn’t guarantee minimal cost because edge weights differ → Dijkstra.

---

## 7️⃣ Mental Checklist for Dijkstra

Before coding, ask:

* Does each move/edge have a **cost that differs**?
* Am I minimizing **total cost** rather than steps?
* Is BFS insufficient due to weights?
* Do I need **minimax path** or weighted shortest path?

If yes → **Dijkstra is the right tool.**

---


