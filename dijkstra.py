from collections import defaultdict

graph = {'a': (('b', 4),
               ('c', 3),
               ('e', 2)),
         'b': (('d', 2),),
         'c': (('b', 1),
               ('d', 1)),
         'd': (('a', 1),
               ('g', 2),
               ('h', 1)),
         'e': (('a', 1),
               ('h', 4),
               ('i', 7)),
         'f': (('b', 3),
               ('g', 1)),
         'g': (('c', 3),
               ('i', 2)),
         'h': (('c', 2),
               ('g', 2)),
         'i': ()}


# Removing from a priority queue is O(n), so we might as well just
# search through all the keys
def find_smallest(path_weight, graph, remaining):
    smallest_weight = float('inf')
    for node in graph.keys():
        if node in remaining and path_weight[node] <= smallest_weight:
            smallest_weight = path_weight[node]
            result = node
    return result


def dijkstra(origin, goal, graph):
    remaining = set()
    for node in graph.keys():
        remaining.add(node)

    path_weight = defaultdict(lambda: float('inf'))
    path_weight[origin] = 0
    previous = defaultdict(lambda: float('inf'))
    while remaining:
        vertex = find_smallest(path_weight, graph, remaining)
        for neighbor in graph[vertex]:
            neigh_node, weight = neighbor
            new_weight = path_weight[vertex] + weight
            if new_weight < path_weight[neigh_node]:
                path_weight[neigh_node] = new_weight
                previous[neigh_node] = vertex
        remaining.remove(vertex)
    return (path_weight[goal], previous)


print(dijkstra('a', 'i', graph)[0])
