from parser.parser import parse_csv
from algorithms.prims import prims
from algorithms.heapprims import heapprims
from algorithms.kruskal import kruskal
import pandas as pd
import numpy as np
import time
from pathlib import Path

def main():
    repo_root = Path(__file__).resolve().parent.parent
    file_path = repo_root / 'testingdata' / 'data.csv'
    data = parse_csv(file_path)
    #data format: Edge ID, Start Node ID, End Node ID, L2 Distance)
    #print(data.head())

    #Prims Algorithm - time this
    start = time.perf_counter()
    result = prims(data)
    elapsed = time.perf_counter() - start
    mst_df = pd.DataFrame(result)

    #stats, for checking correctness (should have V-1 edges, where V is the number of unique nodes in the graph)
    unique_nodes = set(data['Start Node ID']).union(data['End Node ID'])
    total = mst_df['L2 Distance'].sum()

    #output to output/prims_output.csv
    output_dir = repo_root / 'output' / 'prims'
    output_dir.mkdir(parents=True, exist_ok=True)   # create folder if missing
    output_path = output_dir / 'prims_output.csv'
    summary_path = output_dir / 'prims_summary.csv'

    mst_df.to_csv(output_path, index=False)

    #write summary stats to a separate file
    summary = pd.DataFrame({
        'metric': ['Unique nodes', 'Input edges', 'MST edges', 'Expected (V-1)', 'Total L2 Distance', 'Runtime (seconds)'],
        'value':  [len(unique_nodes), len(data), len(mst_df), len(unique_nodes) - 1, total, f'{elapsed:.6f}'],
    })
    summary.to_csv(summary_path, index=False)

    print(f"Prim's algorithm output saved to {output_path}")
    print(f"Prim's summary saved to {summary_path}")

    #heapprims Algorithm - time this
    start = time.perf_counter()
    result = heapprims(data)
    elapsed = time.perf_counter() - start
    mst_df = pd.DataFrame(result)

    #stats, for checking correctness (should have V-1 edges, where V is the number of unique nodes in the graph)
    total = mst_df['L2 Distance'].sum()

    #output to output/heapprims_output.csv
    output_dir = repo_root / 'output' / 'heapprims'
    output_dir.mkdir(parents=True, exist_ok=True)   # create folder if missing
    output_path = output_dir / 'heapprims_output.csv'
    summary_path = output_dir / 'heapprims_summary.csv'

    mst_df.to_csv(output_path, index=False)

    #write summary stats to a separate file
    summary = pd.DataFrame({
        'metric': ['Unique nodes', 'Input edges', 'MST edges', 'Expected (V-1)', 'Total L2 Distance', 'Runtime (seconds)'],
        'value':  [len(unique_nodes), len(data), len(mst_df), len(unique_nodes) - 1, total, f'{elapsed:.6f}'],
    })
    summary.to_csv(summary_path, index=False)

    print(f"Heap Prim's algorithm output saved to {output_path}")
    print(f"Heap Prim's summary saved to {summary_path}")

    #kruskall Algorithm - time this
    start = time.perf_counter()
    result = kruskal(data)
    elapsed = time.perf_counter() - start
    mst_df = pd.DataFrame(result)

    #stats, for checking correctness (should have V-1 edges, where V is the number of unique nodes in the graph)
    total = mst_df['L2 Distance'].sum()

    #output to output/heapprims_output.csv
    output_dir = repo_root / 'output' / 'kruskal'
    output_dir.mkdir(parents=True, exist_ok=True)   # create folder if missing
    output_path = output_dir / 'kruskal_output.csv'
    summary_path = output_dir / 'kruskal_summary.csv'

    mst_df.to_csv(output_path, index=False)

    #write summary stats to a separate file
    summary = pd.DataFrame({
        'metric': ['Unique nodes', 'Input edges', 'MST edges', 'Expected (V-1)', 'Total L2 Distance', 'Runtime (seconds)'],
        'value':  [len(unique_nodes), len(data), len(mst_df), len(unique_nodes) - 1, total, f'{elapsed:.6f}'],
    })
    summary.to_csv(summary_path, index=False)

    print(f"Kruskal's algorithm output saved to {output_path}")
    print(f"Kruskal's summary saved to {summary_path}")


if __name__ == "__main__":
    main()