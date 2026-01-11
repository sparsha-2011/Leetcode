
# Eulerian Path / Hierholzer (Reconstruct Itinerary)



## 1️⃣ What is an Eulerian Path? What does it do?

An **Eulerian Path** is a path in a graph that **visits every edge exactly once**.

Key points:

* Works on **directed or undirected graphs**
* Eulerian Path exists if:

  * **Directed graph**: at most one node has out-degree = in-degree + 1 (start), one node has in-degree = out-degree + 1 (end), all others have in-degree = out-degree
  * **Undirected graph**: exactly 0 or 2 nodes have odd degree
* Hierholzer’s algorithm is the standard **constructive approach** to build the Eulerian path

In LeetCode, this pattern is used for problems where **you need to reconstruct a sequence of edges**.

---

## 2️⃣ How to know if a problem can be solved using Eulerian Path / Hierholzer

A problem is a strong candidate if:

* You need to **use all edges exactly once** (tickets, connections, flights)
* There is a **directed or undirected graph** implicitly
* You are asked to **reconstruct a valid order / path** rather than just check existence
* Lexicographical order may also matter

---

## 3️⃣ General tells to look for in the problem statement

Look for phrases like:

* “Reconstruct itinerary / route / sequence”
* “Use each ticket exactly once”
* “Return the path using all edges”
* “Lexicographically smallest” (optional, for tie-breaking)

Structural tells:

* The graph is **directed**
* Each edge must be used **exactly once**
* Output is a **sequence of nodes / airports / cities**

---

## 4️⃣ Eulerian Path / Hierholzer Template (DFS / Backtracking)

```python
from collections import defaultdict

def findItinerary(tickets):
    graph = defaultdict(list)
    # Sort destinations in reverse for efficient pop
    for u, v in sorted(tickets, reverse=True):
        graph[u].append(v)

    route = []

    def visit(airport):
        while graph[airport]:
            next_airport = graph[airport].pop()
            visit(next_airport)
        route.append(airport)

    visit("JFK")
    return route[::-1]  # reverse to get correct order
```

### Key points to notice

* Sort destinations in **reverse order** if lexicographical smallest path is required
* Use **DFS** to recursively consume all edges
* Append to route **after visiting all neighbors** (post-order)
* Reverse route at the end

---

## 5️⃣ Problem That Uses This Pattern

### 🟪 `reconstruct-itinerary.py`

**Problem summary:**
Given a list of airline tickets `[from, to]`, reconstruct the itinerary starting from `"JFK"` using all tickets exactly once. Return **lexicographically smallest path** if multiple itineraries exist.

**Eulerian Path / Hierholzer tells from the statement:**

* “Use all tickets exactly once” → every edge must be traversed **exactly once**
* “Return the itinerary” → need **actual path / sequence**
* Lexicographical tie-breaking → sort adjacency list

---

## 6️⃣ Eulerian Path vs DFS / Backtracking

| Eulerian Path                       | Standard DFS                                   |
| ----------------------------------- | ---------------------------------------------- |
| Uses **all edges exactly once**     | Explores nodes / components arbitrarily        |
| Route is **sequence of edges**      | Often solves reachability or counting problems |
| Often uses **post-order traversal** | Pre-order or simple recursive traversal        |
| Lexicographical ordering possible   | Usually irrelevant                             |

---

## 7️⃣ What Eulerian Path is **not** good for

* Counting islands → DFS
* Shortest path / minimum time → BFS / Dijkstra
* Topological ordering / dependencies → Topo Sort
* Union-Find / connected components → cycle detection

---

## 8️⃣ Mental Checklist for Eulerian Path

Before coding, ask:

* Must I **use each edge exactly once**?
* Do I need to **reconstruct a full path**?
* Is **lexicographical order** relevant?

If yes → **Eulerian Path / Hierholzer DFS is the right tool.**

---
