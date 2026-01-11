
# Minimum Spanning Tree (MST)



## 1️⃣ What is a Minimum Spanning Tree? What does it do?

A **Minimum Spanning Tree (MST)** is a subset of the edges of a **connected, undirected, weighted graph** that:

* Connects all vertices together
* Has **no cycles**
* Has the **minimum possible total edge weight**

Key points:

* MST finds the **cheapest way to connect all points/nodes**.
* Common algorithms:

  * **Kruskal’s Algorithm** (uses Union-Find)
  * **Prim’s Algorithm** (uses priority queue / greedy expansion)

---

## 2️⃣ How to know if a problem can be solved using MST

A problem is a good candidate if:

* You are asked to **connect all nodes/points with minimum cost**
* The graph is **undirected and weighted**
* The problem asks for **total cost**, not paths between nodes
* You may need to **avoid cycles** while connecting nodes

MST is often used in **network design, road planning, or connecting points in space**.

---

## 3️⃣ General tells to look for in the problem statement

Look for phrases like:

* “Minimum total cost”, “connect all points”
* “All nodes must be connected”
* “Avoid cycles”, “redundant connections”
* “Cost to build network / cables / roads”

Structural tells:

* Undirected edges
* Edge weights exist
* Want **total cost**, not individual paths
* Often does not require shortest path between two specific nodes

---

## 4️⃣ MST Templates

### Kruskal’s Algorithm (Union-Find)

```python
def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])  # sort by weight
    uf = UnionFind(n)
    mst_cost = 0
    for u, v, w in edges:
        if uf.union(u, v):  # edge added to MST
            mst_cost += w
    return mst_cost
```

### Prim’s Algorithm (Priority Queue)

```python
import heapq
from collections import defaultdict

def prim(n, edges):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((w, v))
        graph[v].append((w, u))

    visited = set()
    pq = [(0, 0)]  # start from node 0
    mst_cost = 0

    while pq and len(visited) < n:
        w, node = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        mst_cost += w
        for nw, nei in graph[node]:
            if nei not in visited:
                heapq.heappush(pq, (nw, nei))

    return mst_cost
```

### Key points to notice

* **Kruskal**: sort edges, merge sets, skip cycles
* **Prim**: expand the cheapest edge from visited nodes
* Works only for **connected, undirected graphs**

---

## 5️⃣ Problems That Use MST

Below are the problems from your list that naturally fall under MST.

---

### 🟪 `min-cost-to-connect-all-points.py`

**Problem summary:**
Given a set of points in 2D space, connect all points with edges equal to Manhattan distance. Return the **minimum total cost** to connect all points.

**MST tells from the statement:**

* “Connect all points”
* “Minimum total cost”
* Edge weights are distances → weighted undirected graph
* Avoid cycles → MST

---

### Notes on why MST is needed

* BFS/DFS only explores connectivity, but **does not minimize total cost**
* Dijkstra finds shortest paths between nodes, but we need a **global minimum spanning tree**
* Union-Find or Prim are classic approaches

---

## 6️⃣ MST vs Other Graph Algorithms

| MST                                              | Dijkstra / BFS / DFS                              |
| ------------------------------------------------ | ------------------------------------------------- |
| Connects **all nodes** with minimum total weight | Finds shortest path from a **source node**        |
| Undirected weighted graphs                       | BFS: unweighted, Dijkstra: weighted shortest path |
| No path to a specific node needed                | Used to reach specific nodes efficiently          |
| Avoid cycles globally                            | DFS/BFS may not avoid cycles globally             |

Rule of thumb:

> “If the problem asks for **minimum cost to connect all points or nodes**, think MST.”

---

## 7️⃣ What MST is **not** good for

* Shortest path between two nodes → Dijkstra
* Grid connected components → DFS/BFS
* Topological ordering / DAG → Topo Sort
* Dynamic connectivity / cycle detection → Union-Find (Kruskal internally uses it, but only for union steps)

---

## 8️⃣ Mental Checklist for MST

Before coding, ask:

* Am I connecting **all nodes**?
* Do I want **minimum total cost**?
* Is the graph **weighted and undirected**?
* Do I need to **avoid cycles**?

If yes → **MST is the right tool.**

---


