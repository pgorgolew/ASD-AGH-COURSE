from queue import Queue


# Maksymalny przepływ w grafie skierowanym (i krawędzie tylko w jedną stronę), O(VE^2), bo znajdywanie ścieżki
# powiększającej z użyciem BFSa
def FordFulkerson(G, s, t):
    parents = [None]*len(G)
    max_flow = 0
    graph = G[:]
    while BFS(graph, s, t, parents):
        path_flow = float("inf")
        end = t
        while end != s:
            path_flow = min(path_flow, graph[parents[end]][end])
            end = parents[end]
        max_flow += path_flow

        end = t
        while end != s:
            u = parents[end]
            graph[u][end] -= path_flow
            graph[end][u] += path_flow
            end = parents[end]

    return max_flow


def BFS(G, s, t, parents):
    Q = Queue()
    visited = [False]*len(G)
    visited[s] = True
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for v in range(len(G[s])):
            if G[u][v] != 0 and not visited[v]:
                visited[v] = True
                parents[v] = u
                Q.put(v)
    
    res = False
    if visited[t]: res = True

    return res


graph = [[0, 10, 10, 0, 0, 0],
         [0, 0, 2, 4, 8, 0],
         [0, 0, 0, 0, 9, 0],
         [0, 0, 0, 0, 0, 10],
         [0, 0, 0, 6, 0, 10],
         [0, 0, 0, 0, 0, 0]]

print(FordFulkerson(graph, 0, 5))