# CSCI 311 — CityConnections Project  
## Minimum Spanning Tree Algorithm Comparison

This project implements and compares three Minimum Spanning Tree (MST) algorithms on a real-world weighted graph dataset. The goal is to evaluate correctness and performance across different algorithmic approaches.

---

## Algorithms Implemented

| Algorithm        | Time Complexity | Description |
|------------------|----------------|-------------|
| Heap Prim’s      | O(E log V)     | Uses a custom min-heap with lazy deletion |
| Naive Prim’s     | O(V²)          | Uses a NumPy-vectorized edge scan |
| Kruskal’s        | O(E log E)     | Uses Disjoint Set Union (union-by-rank + path compression) |

All algorithms produce valid MSTs and are verified by matching edge count and total weight.

---

## How to Run

From the root of the project:

python src/main.py <input_file> <output_file>

Example:

python src/main.py testingdata/data.csv output/result.txt

---

## Input Format

The input file must be a whitespace-separated edge list with no header:

<edge_id> <node_a> <node_b> <l2_distance>

---

## Output

Each algorithm produces:

- <algo>_output.csv → MST edges  
- <algo>_summary.csv → metrics and runtime  

Saved in:

output/
  heapprims/
  prims/
  kruskal/

Additionally:
- A comparison table is printed to the terminal
- Heap Prim’s result is written to the specified output file

---

## Project Structure

src/
  main.py
  parser/
    parser.py
  algorithms/
    heapprims.py
    prims.py
    kruskal.py
    helper/
      Heap.py
      Disjoint.py

testingdata/
  data.csv

output/
  (generated on run)

---

## Dependencies

pip install pandas numpy

---

## Notes

- Assumes the graph is connected
- MST correctness verified using:
  - Edge count = V - 1
  - Matching total distance across algorithms
- Performance differences are more noticeable on large datasets

---

## Authors

CSCI 311 CityConnections Project
