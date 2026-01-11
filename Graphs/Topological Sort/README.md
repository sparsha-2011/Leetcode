
# Topological Sort (DAG)



## 1️⃣ What is Topological Sort? What does it do?

**Topological Sort** is an ordering of the nodes in a **Directed Acyclic Graph (DAG)** such that for every directed edge `u → v`, `u` comes **before** `v` in the ordering.

Key points:

* Only works for **DAGs** (no cycles).
* Often used to resolve **dependencies**, e.g., tasks, courses, or character orders.
* Can be implemented with:

  * **Kahn’s algorithm** (BFS-based using indegrees)
  * **DFS-based post-order traversal**

---

## 2️⃣ How to know if a problem can be solved using Topological Sort

A problem is a good candidate if:

* There are **dependencies** or prerequisites
* The task is to **find an ordering** that satisfies all constraints
* You need to **detect cycles** (to check if ordering is possible)
* The problem involves **partial ordering** (some elements must come before others)

Topological sort answers questions like *“In what order should I do things?”*.

---

## 3️⃣ General tells to look for in the problem statement

Look for phrases like:

* “Prerequisites”, “before / after”
* “Ordering of tasks/courses/characters”
* “Dependencies”
* “Check if ordering is possible”
* “Return valid sequence”

Structural tells:

* Directed edges (dependencies)
* No edge weights
* You might need to **detect cycles** to know if a solution exists

---

## 4️⃣ Topological Sort Template (Kahn’s Algorithm)

```python
from collections import defaultdict, deque

def topological_sort(n, edges):
    graph = defaultdict(list)
    indegree = [0] * n

    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    q = deque([i for i in range(n) if indegree[i] == 0])
    order = []

    while q:
        node = q.popleft()
        order.append(node)
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    if len(order) == n:
        return order  # valid topological order
    else:
        return []     # cycle detected
```

### DFS-based Topological Sort (Alternative)

```python
def dfs_topo(node):
    visited[node] = True
    for nei in graph[node]:
        if not visited[nei]:
            dfs_topo(nei)
    order.append(node)

# Reverse order at the end
order.reverse()
```

---

## 5️⃣ Problems That Use Topological Sort

Below are the problems from your list that naturally fall under Topological Sort.
---
🟨 find-the-town-judge.py

Problem summary:
Given n people labeled from 1 to n and a list of trust relationships [a, b] (person a trusts person b), find the town judge — the person who is trusted by everyone else but trusts nobody. Return the judge’s label or -1 if no judge exists.

Topological Sort tells from the statement:

“Person a trusts person b” → directed edge a → b

“Judge trusts nobody” → out-degree = 0

“Judge is trusted by everyone” → in-degree = n-1

You can think of this as a dependency graph, where arrows point toward the judge

Topological sort intuition: the judge is a sink node (node with zero outgoing edges) in the directed graph
---

### 🟨 `course-schedule.py`

**Problem summary:**
Determine if it’s possible to finish all courses given prerequisites as pairs `[u, v]` where `v` must be taken before `u`.

**Topological Sort tells from the statement:**

* “Prerequisites” → dependency graph
* “Finish all courses” → check for cycle existence
* Directed edges, no weights

---

### 🟨 `course-schedule-ii.py`

**Problem summary:**
Return a valid order in which courses can be finished.

**Topological Sort tells from the statement:**

* “Return a valid order” → direct topological sort
* Prerequisites define directed edges
* Cycle detection required for impossibility

---

### 🟨 `course-schedule-iv.py`

**Problem summary:**
Check if it is possible to take course `u` before course `v` for multiple queries, given prerequisites.

**Topological Sort tells from the statement:**

* “Multiple queries about order”
* “Directed acyclic prerequisites”
* Can precompute reachability using **DFS or topological ordering**

---

### 🟨 `alien-dictionary.py`

**Problem summary:**
Given a list of words sorted in an alien language, determine a possible ordering of characters.

**Topological Sort tells from the statement:**

* “Determine the order of letters” → dependency graph between characters
* Compare adjacent words → edge from first differing character
* DAG → topological sort returns one valid ordering

---

### 🟨 `verifying-an-alien-dictionary.py`

**Problem summary:**
Verify if a list of words is sorted according to a given alien character order.

**Topological Sort tells from the statement:**

* “Verify ordering according to custom character sequence”
* Dependency graph already implied by character order
* Check for violations along adjacency → cycle detection not always needed

---

## 6️⃣ Topological Sort vs DFS / BFS

| Topo Sort                              | DFS/BFS                            |
| -------------------------------------- | ---------------------------------- |
| Works on **directed acyclic graph**    | Works on any graph                 |
| Orders nodes according to dependencies | Explores components or levels      |
| Detects cycles for impossibility       | No cycle detection unless explicit |
| Often uses indegrees or post-order DFS | Uses visited set for exploration   |

Rule of thumb:

> “If the problem asks **in what order** tasks/letters/courses should happen → think Topological Sort.”

---

## 7️⃣ What Topological Sort is **not** good for

* BFS/DFS problems like counting islands or shortest path
* Weighted shortest path problems (use Dijkstra instead)
* Unweighted shortest path (use BFS)

---

## 8️⃣ Mental Checklist for Topological Sort

Before coding, ask:

* Are there **dependencies** between items?
* Am I asked for **any valid order** that satisfies all dependencies?
* Do I need to **check for cycles** to detect impossibility?

If yes → **Topological Sort is the right tool.**

---


