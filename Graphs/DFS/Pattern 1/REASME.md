# DFS Pattern 1 — Component Finding

## What is it?

The most fundamental DFS pattern. Start from an unvisited node, explore everything reachable — that's one component. Repeat for all unvisited nodes. Each new DFS call from the main loop = one new component.

## When to use

- "How many connected components?"
- "Group connected nodes together"
- "Find all nodes reachable from X"
- Any problem where you need to identify or count separate groups

---

## Core Template

### Count components only

```python
visited = set()
components = 0

def dfs(node):
    visited.add(node)
    for nei in graph[node]:
        if nei not in visited:
            dfs(nei)

for node in range(n):
    if node not in visited:
        dfs(node)
        components += 1      # each new DFS = new component
```

### Collect nodes in each component

```python
visited = set()
all_components = []

def dfs(node, component):
    visited.add(node)
    component.append(node)       # collect the node
    for nei in graph[node]:
        if nei not in visited:
            dfs(nei, component)

for node in range(n):
    if node not in visited:
        component = []
        dfs(node, component)
        all_components.append(component)

# all_components = [[0, 1, 2], [3, 4], [5]]
```

### Get component sizes

```python
for node in range(n):
    if node not in visited:
        component = []
        dfs(node, component)
        print(len(component))    # size of this component
```

---

## Graph Representations

### Undirected graph with adjacency list

Most common. Given a list of edges, build the adjacency list. **Always add both directions for undirected graphs.**

```python
from collections import defaultdict

adjL = defaultdict(list)
for u, v in edges:
    adjL[u].append(v)
    adjL[v].append(u)       # BOTH directions for undirected

def dfs(node):
    visited.add(node)
    for nei in adjL[node]:
        if nei not in visited:
            dfs(nei)
```

Common mistake: forgetting `adjL[v].append(u)` — this makes DFS miss connections and overcount components.

### Undirected graph with adjacency matrix (0/1 grid)

Given an n×n matrix where `graph[i][j] == 1` means i connects to j.

```python
def dfs(node):
    visited.add(node)
    for nei in range(n):
        if graph[node][nei] == 1 and nei not in visited:
            dfs(nei)
```

No need to build adjacency list — iterate all possible neighbors and check the matrix.

### 2D grid (matrix of cells)

Given a grid where `1` is land and `0` is water (e.g. Number of Islands).

```python
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def dfs(r, c):
    if r < 0 or r >= ROWS or c < 0 or c >= COLS:
        return
    if (r, c) in visited or grid[r][c] == 0:
        return
    visited.add((r, c))
    for dr, dc in directions:
        dfs(r + dr, c + dc)

for r in range(ROWS):
    for c in range(COLS):
        if grid[r][c] == 1 and (r, c) not in visited:
            dfs(r, c)
            components += 1
```

---

## The pattern is always the same

```
Step 1: For every node, if not visited → start DFS
Step 2: DFS explores the ENTIRE component
Step 3: After DFS returns → that was one complete component
Step 4: Do something with it (count, collect, measure size)
```

What changes per problem is only Step 4 — what you do with each component.

---

## LeetCode Problems Using Pattern 1

### Easy / Medium
| Problem | What you do with components |
|---|---|
| Number of Islands (200) | Count components on a 2D grid |
| Number of Provinces (547) | Count components in adjacency matrix |
| Number of Connected Components (323) | Count components with edge list |
| Graph Valid Tree (261) | Check if components == 1 and edges == n-1 |
| Accounts Merge (721) | Collect nodes per component, sort emails |

### Medium
| Problem | What you do with components |
|---|---|
| Minimize Malware Spread (924) | Count infected per component, check sizes |
| Most Stones Removed (947) | Answer = total stones - number of components |
| Regions Cut By Slashes (959) | Scale grid 3x, count components |
| Satisfiability of Equality Equations (990) | Group equal variables, check conflicts |
| Number of Operations to Make Network Connected (1319) | Need components-1 extra edges |
| Smallest String With Swaps (1202) | Sort characters within each component |

### Hard
| Problem | What you do with components |
|---|---|
| Minimize Malware Spread II (928) | Components + infected counting |
| Remove Max Number of Edges (1579) | Component tracking with edge selection |

---

## Pattern 1 vs Union Find

Both solve the same problems. Choose based on what you need:

| Need | Pattern 1 (DFS) | Union Find |
|---|---|---|
| Count components | ✓ | ✓ |
| Component sizes | ✓ (len of collected list) | ✓ (rank[root]) |
| List nodes in component | ✓ (natural) | ✗ (need extra work) |
| Edges arriving one at a time | ✗ (rebuild graph) | ✓ (incremental) |
| Cycle detection | ✓ (Pattern 4) | ✓ (union returns False) |

---

## Common Mistakes

1. **Undirected graphs**: forgetting to add both directions in adjacency list
2. **Visited timing**: add to visited when entering DFS, not after
3. **Grid bounds**: always check boundaries before accessing grid cells
4. **Variable shadowing**: don't name loop variable same as function parameter (e.g. `n`)
