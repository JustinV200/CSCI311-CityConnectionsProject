import pandas as pd
import numpy as np

def prims(data):
    """
    Implements Prim's algorithm to find the Minimum Spanning Tree (MST) of a graph.
    Takes in dataframe with columns: Edge ID, Start Node ID, End Node ID, L2 Distance.
    Cut into 2 peices, first containing one node and the second containing the rest of the nodes.
    find the smallest edge that connects the two peices, add it to the MST, and repeat until all nodes are connected.
    """
    #get all starts and ends, and create an adjacency list for the graph
    starts = data['Start Node ID'].to_numpy()
    ends   = data['End Node ID'].to_numpy()
    dists  = data['L2 Distance'].to_numpy()

    #track all nodes in the MST
    mst_nodes = set()
    #track all edges in the MST
    mst_edges = []
    #get all unique nodes in the graph
    nodes = set(data['Start Node ID']).union(set(data['End Node ID']))
    #add initial node to the MST
    mst_nodes.add(data['Start Node ID'].iloc[0])
    #start splitting
    while len(mst_nodes) < len(nodes):
        #find the smallest edge that connects the two peices
        '''
        This was my old idea, but gonna vectorize for speed
        for node in mst_nodes:
            edges = data[(data['Start Node ID'] == node) | (data['End Node ID'] == node)]
            for _, edge in edges.iterrows():
                if edge['Start Node ID'] not in mst_nodes or edge['End Node ID'] not in mst_nodes:
                    frontier.append(edge)
        '''
        #same as loop above, but vectorized for speed so we can win
        mst_arr = np.fromiter(mst_nodes, dtype=starts.dtype, count=len(mst_nodes))
        start_in = np.isin(starts, mst_arr)
        end_in   = np.isin(ends,   mst_arr)
        mask = start_in ^ end_in
        #if there are no edges connecting the two peices, then the graph is not fully connected
        if not mask.any():
            break
        #find the edge with the smallest L2 Distance
        idx = np.argmin(np.where(mask, dists, np.inf))
        min_edge = data.iloc[idx]

        mst_edges.append(min_edge)
        #get the node, add it to tree
        if min_edge['Start Node ID'] in mst_nodes:
            mst_nodes.add(min_edge['End Node ID'])
        else:
            mst_nodes.add(min_edge['Start Node ID'])

    return mst_edges


