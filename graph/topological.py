# topological sort using the queue method

import collections
def topological_sort(graph):
    n = len(graph)

    # number of inbound edges
    inbound = [0] * n
    # queue of nodes that has 0 inbound edge
    q = collections.deque()
    seen = set()
    # sorted nodes
    res = []

    for i in range(n):
        for j in range(n):
            inbound[j] += graph[i][j]

    for i in range(n):
        if inbound[i] == 0:
            q.append(i)
            seen.add(i)

    while q:
        node = q.popleft()
        res.append(node)

        for i in range(n):
            inbound[i] -= graph[node][i]
            if not i in seen and not inbound[i]:
                q.append(i)
                seen.add(i)

    return res

if __name__ == "__main__":
    # init graph
    N = 6
    graph = [[0] * N for _ in range(N)]
    graph[5][0] = 1
    graph[5][2] = 1
    graph[4][0] = 1
    graph[4][1] = 1
    graph[2][3] = 1
    graph[3][1] = 1

    # topological sort
    topological_sort(graph)