import heapq
import math

def heapprims(data):
    #heaps with a priority queue of edges, where the priority is the L2 Distance
    #Should be O(E log V) if implemented correctly


    #pull raw numpy arrays once
    starts = data['Start Node ID'].to_numpy()
    ends   = data['End Node ID'].to_numpy()
    dists  = data['L2 Distance'].to_numpy()

    #build adjacency list: node -> [(dist, neighbor, edge_index), ...]
    #store row index (idx) instead of the row itself so columns survive intact
    adj = {}
    for i in range(len(starts)):
        s, e, d = starts[i], ends[i], dists[i]
        adj.setdefault(s, []).append((d, e, i))
        adj.setdefault(e, []).append((d, s, i))

    all_nodes = set(adj)
    start = next(iter(all_nodes))  # start from an arbitrary node
    in_tree = {start} #start the tree with one node, arbitrary which one we start with, it shouldnt change the result
    mst_edge_indices = []

    #best[node] = cheapest known distance from the tree to that node
    #only push when we discover a strictly cheaper connection
    best = {n: math.inf for n in adj}
    best[start] = 0.0

    #seed the heap with the start node's edges and record their distances as best
    heap = list(adj[start])
    heapq.heapify(heap)
    for d, nbr, _ in adj[start]:
        if d < best[nbr]:
            best[nbr] = d

    #while the tree has fewer nodes than the graph, keep adding edges
    while heap and len(in_tree) < len(all_nodes):
        #get the distance, the node, and the row index of the edge
        dist, nbr, idx = heapq.heappop(heap)
        if nbr in in_tree:
            #lazy deletion: stale entry from before nbr joined the tree
            continue
        in_tree.add(nbr)
        mst_edge_indices.append(idx)

        #relax outgoing edges: only push if we found a cheaper path to "other"
        for d, other, i in adj[nbr]:
            if other not in in_tree and d < best[other]:
                best[other] = d
                heapq.heappush(heap, (d, other, i))
    #pull the actual rows out of the original dataframe in MST order
    return data.iloc[mst_edge_indices].reset_index(drop=True)
