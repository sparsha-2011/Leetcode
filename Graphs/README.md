

# 📚 Graph Problem Categories — Master List


## 1️⃣ DFS (Depth-First Search)

Problems where **recursive or stack-based exploration** of nodes is key. Often used for **connected components, reachability, islands, or graph cloning**.

**Problems:**

* `number-of-islands.py`
* `max-area-of-island.py`
* `surrounded-regions.py`
* `rotting-oranges.py` *(DFS possible, BFS preferred for min time)*
* `walls-and-gates.py` *(DFS possible, BFS preferred for shortest distance)*
* `clone-graph.py`
* `graph-valid-tree.py`
* `island-perimeter.py`

---

## 2️⃣ BFS (Breadth-First Search)

Problems where **level-by-level traversal** is needed. Often used for **shortest paths in unweighted graphs, minimum steps, or spreading processes**.

**Problems:**

* `rotting-oranges.py` *(for minimum time to rot all oranges)*
* `walls-and-gates.py` *(for minimum distance to gates)*
* `open-the-lock.py`
* `word-ladder.py`

---

## 3️⃣ Topological Sort (Directed Acyclic Graph / Ordering)

Problems involving **dependencies, prerequisites, or ordering tasks/nodes**.

**Problems:**

* `course-schedule.py`
* `course-schedule-ii.py`
* `course-schedule-iv.py`
* `alien-dictionary.py`
* `verifying-an-alien-dictionary.py`
* `find-the-town-judge.py` *(treated as Topo Sort — judge is a sink node)*

---

## 4️⃣ Union-Find / Disjoint Set

Problems where **connected components, cycle detection, or dynamic connectivity** are key.

**Problems:**

* `graph-valid-tree.py` *(also DFS, can be solved with Union-Find)*
* `redundant-connection.py`
* `number-of-connected-components-in-an-undirected-graph.py`

---

## 5️⃣ Minimum Spanning Tree (MST — Prim / Kruskal)

Problems where **all nodes must be connected at minimum total cost**.

**Problems:**

* `min-cost-to-connect-all-points.py`

*(Others like `swim-in-rising-water.py` and `path-with-minimum-effort.py` can be treated as MST variants on implicit graphs.)*

---

## 6️⃣ Dijkstra / Shortest Path (Weighted Graphs)

Problems where **shortest paths in weighted graphs** are needed.

**Problems:**

* `network-delay-time.py`
* `cheapest-flights-within-k-stops.py`
* `swim-in-rising-water.py` *(can also be treated as Dijkstra on grid)*
* `path-with-minimum-effort.py`

---

## 7️⃣ Eulerian Path / Hierholzer (DFS + Backtracking)

Problems where **all edges must be used exactly once**, often requiring **reconstruction of a path**.

**Problems:**

* `reconstruct-itinerary.py`

---

## 8️⃣ Graph Property / Counting / In-degree Analysis

Problems where **graph structure, degrees, or simple properties** are checked rather than paths or orderings.

**Problems:**

* `find-the-town-judge.py` *(if treated as property problem instead of Topo Sort)*

---
