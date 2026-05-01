import sys
import time
import pandas as pd
from pathlib import Path

from parser.parser import parse_csv
from algorithms.heapprims import heapprims
from algorithms.prims import prims
from algorithms.kruskal import kruskal


def write_output(mst_df, output_path):
    # write MST edges to output file in the same space-separated format as input
    mst_df.to_csv(output_path, index=False, header=False, sep=' ')


def run_algorithm(name, fn, data):
    # run a single algorithm, time it, and return (result_df, elapsed)
    start = time.perf_counter()
    result = fn(data)
    elapsed = time.perf_counter() - start
    mst_df = pd.DataFrame(result) if not isinstance(result, pd.DataFrame) else result
    return mst_df, elapsed


def print_comparison(data, results):
    # print a comparison table of all three algorithms
    unique_nodes = set(data['Start Node ID']).union(data['End Node ID'])
    expected_edges = len(unique_nodes) - 1

    print()
    print(f"{'Algorithm':<20} {'MST Edges':>10} {'Expected':>10} {'Total Distance':>18} {'Runtime (s)':>12}")
    print("-" * 74)
    for name, mst_df, elapsed in results:
        total = mst_df['L2 Distance'].sum()
        edge_count = len(mst_df)
        print(f"{name:<20} {edge_count:>10} {expected_edges:>10} {total:>18.5f} {elapsed:>12.6f}")
    print()


def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py inputfile outputfile")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    data = parse_csv(input_file)
    if data is None:
        print(f"Error: could not parse input file '{input_file}'")
        sys.exit(1)

    repo_root = Path(__file__).resolve().parent.parent
    unique_nodes = set(data['Start Node ID']).union(data['End Node ID'])

    results = []
    algo_configs = [
        ("Heap Prim's", heapprims, "heapprims"),
        ("Naive Prim's", prims,    "prims"),
        ("Kruskal's",   kruskal,   "kruskal"),
    ]
    for name, fn, folder in algo_configs:
        mst_df, elapsed = run_algorithm(name, fn, data)
        results.append((name, mst_df, elapsed))

        # write output and summary csvs to output/<algo>/ folder
        output_dir = repo_root / 'output' / folder
        output_dir.mkdir(parents=True, exist_ok=True)

        write_output(mst_df, output_dir / f'{folder}_output.csv')

        summary = pd.DataFrame({
            'metric': ['Unique nodes', 'Input edges', 'MST edges', 'Expected (V-1)', 'Total L2 Distance', 'Runtime (seconds)'],
            'value':  [len(unique_nodes), len(data), len(mst_df), len(unique_nodes) - 1, mst_df['L2 Distance'].sum(), f'{elapsed:.6f}'],
        })
        summary.to_csv(output_dir / f'{folder}_summary.csv', index=False)

    print_comparison(data, results)

    # write heapprims result to the grader's output file
    write_output(results[0][1], output_file)


if __name__ == "__main__":
    main()