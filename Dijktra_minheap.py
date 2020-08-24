import heapq
from heapq import heappush, heappop

import math
import osmnx as ox
import networkx as nx
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

### Original implementation of Dijkstra using a minheap.
### takes in G: a NX graph object
### and source: a numerical index of G, and target: a numerical index of G
### returns the distance from source to target, and path from source to target

def dijkstra(G, source, target): 
    if not source:
        raise ValueError('need source')
    if not source in G:
        raise AssertionError("Source not in Graph")
    if not target in G:
        raise AssertionError("Target not in Graph")
    if target == source:
        return (0, [target])
    paths = {source: [source]}
    dist = {} 
    heap = []
    seen = {source : 0}
    heappush(heap, (0, source))
    while heap:
        (d, v) = heappop(heap)
        if v in dist:
            continue
        dist[v] = d
        if v == target:
            break
        struc = G._succ[v]
        nexter, edge = struc.keys(), list(struc.values())
        for j in range(len(struc)):
            length = list(list(edge)[j].values())[0]['length']
            min_node = list(nexter)[j]
            new_dist = dist[v] + length
            if not min_node in seen or new_dist < seen[min_node]:
                seen[min_node] = new_dist
                heappush(heap, (new_dist, min_node))
                paths[min_node] = paths[v] + [min_node]
    return dist[target], paths[target]