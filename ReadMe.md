# CITI — Minimum Spanning Tree Comparison

CSCI 311 project implementing and benchmarking three MST algorithms on a real edge-weighted graph.

## Algorithms

| Algorithm | Complexity | Notes |
|---|---|---|
| Heap Prim's | O(E log V) | Min-heap priority queue, lazy deletion of stale entries |
| Naive Prim's | O(V²) | NumPy-vectorized crossing-edge scan |
| Kruskal's | O(E log E) | DSU with union-by-rank and path compression |

All three produce identical MSTs verified by matching edge count and total weight.

## Usage

```bash
python src/main.py <input_file> <output_file>
```

**Example:**
```bash
python src/main.py testingdata/data.csv output/result.txt
```

The primary result (Heap Prim's MST) is written to `<output_file>`. Per-algorithm results and timing summaries are written to `output/heapprims/`, `output/prims/`, and `output/kruskal/`.

## Input Format

Whitespace-separated edge list, no header. Each row:

```
<edge_id> <node_a> <node_b> <l2_distance>
```

## Output Format

Each algorithm produces two files:

- `<algo>_output.csv` — MST edges in the same format as input
- `<algo>_summary.csv` — node count, edge count, total distance, and runtime

## Project Structure

```
src/
  main.py                  # Entry point; runs all three algorithms and prints comparison
  parser/parser.py         # Edge list parser
  algorithms/
    heapprims.py           # Heap Prim's
    prims.py               # Naive Prim's
    kruskal.py             # Kruskal's
    helper/
      Heap.py              # Custom min-heap
      Disjoint.py          # Disjoint Set Union
testingdata/data.csv       # Test graph (7,035 edges, 6,105 nodes)
output/                    # Algorithm results regenerated on each run
```

## Dependencies

```
pandas
numpy
```

Install with:

```bash
pip install pandas numpy
```
