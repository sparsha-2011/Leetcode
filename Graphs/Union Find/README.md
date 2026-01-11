

# Union-Find (Disjoint Set)



## 1️⃣ What is Union-Find? What does it do?

**Union-Find**, also called **Disjoint Set Union (DSU)**, is a data structure used to efficiently:

* Track **connected components**
* Merge components dynamically
* Detect **cycles** in an undirected graph

It supports two main operations:

1. **find(x)** → returns the representative (root) of the set containing `x`
2. **union(x, y)** → merges the sets containing `x` and `y`

With **path compression** and **union by rank/size**, each operation runs in nearly constant time (`O(α(n))`).

---

## 2️⃣ How to know if a problem can be solved using Union-Find

A problem is a good candidate if:

* You are asked to **track connected components**
* You need to **check if adding an edge forms a cycle**
* The graph is **undirected**
* You may need to **merge sets** dynamically

Union-Find is particularly useful for **dynamic connectivity problems**.

---

## 3️⃣ General tells to look for in the problem statement

Look for phrases like:

* “connected components”
* “redundant connection”
* “is graph a tree?”
* “merge groups” or “union sets”
* “check connectivity after adding edges”

Structural tells:

* Undirected graph
* Need **fast component checks**
* You may be **adding edges incrementally**

---

## 4️⃣ Union-Find Template (Python)

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  # Already connected / cycle detected
        # Union by rank
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        self.rank[px] += self.rank[py]
        return True
```

### Key points to notice

* `find` with **path compression** reduces tree height
* `union` with **rank/size** keeps trees balanced
* Returns **False** if merging creates a cycle (useful for cycle detection)

---

## 5️⃣ Problems That Use Union-Find

Below are the problems from your list that naturally fall under Union-Find.

---

### 🟧 `graph-valid-tree.py`

**Problem summary:**
Given `n` nodes and edges, determine if the graph is a valid tree.

**Union-Find tells from the statement:**

* “Graph is a tree” → n-1 edges + no cycles
* Undirected graph
* Check **for cycles** while connecting nodes

Union-Find allows **cycle detection** efficiently.

---

### 🟧 `redundant-connection.py`

**Problem summary:**
Given edges forming a graph that is almost a tree, return the edge that creates a cycle.

**Union-Find tells from the statement:**

* “Return the edge that creates a cycle”
* Dynamic edge addition
* Undirected edges

Union-Find detects the **first edge where `union` fails**.

---

### 🟧 `number-of-connected-components-in-an-undirected-graph.py`

**Problem summary:**
Count the number of connected components in an undirected graph.

**Union-Find tells from the statement:**

* “Count connected components”
* Union all edges
* Count distinct parents after unions

---

### 🟧 `find-the-town-judge.py`

**Problem summary:**
In a trust graph, identify the town judge (trusted by everyone, trusts no one).

**Union-Find tells from the statement:**

* Can use **connected component logic** to group people
* Each trust relation = potential union
* While not classic Union-Find, connected components reasoning applies

---

## 6️⃣ Union-Find vs DFS/BFS

| Union-Find                              | DFS/BFS                             |
| --------------------------------------- | ----------------------------------- |
| Tracks connected components dynamically | Explores components explicitly      |
| Works well for cycle detection          | Cycle detection possible but slower |
| Edge order can matter                   | Usually traverses entire graph      |
| Efficient for incremental unions        | Traversal-based, O(V+E) each time   |

Rule of thumb:

> “If the problem involves **merging sets or detecting cycles efficiently**, think Union-Find.”

---

## 7️⃣ What Union-Find is **not** good for

* Shortest paths (use BFS / Dijkstra)
* DAG ordering (use Topological Sort)
* Grid-based connected components (DFS is simpler)

---

## 8️⃣ Mental Checklist for Union-Find

Before coding, ask:

* Am I working with an **undirected graph**?
* Do I need to **track connected components dynamically**?
* Am I detecting **cycles** efficiently?
* Will edges be **added incrementally** or in arbitrary order?

If yes → **Union-Find is the right tool.**

---

