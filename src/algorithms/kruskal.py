import pandas as pd
import numpy as np
from algorithms.helper.Disjoint import Disjoint

def kruskal(data):
    data = data.sort_values(by="L2 Distance")

    starts = data['Start Node ID'].to_numpy()
    ends = data['End Node ID'].to_numpy()
    dists = data['L2 Distance'].to_numpy()

    disjoint = Disjoint()
    mst_edges = []
    nodes = set(data['Start Node ID']).union(set(data['End Node ID']))

    i = 0
    while len(mst_edges) < len(nodes) - 1:
        v1 = starts[i]
        v2 = ends[i]

        if v1 not in disjoint.nodes:
            disjoint.make_set(v1)
        if v2 not in disjoint.nodes:
            disjoint.make_set(v2)

        if disjoint.union(v1,v2):
            edge = data.iloc[i]
            mst_edges.append(edge)

        i += 1

    return mst_edges

