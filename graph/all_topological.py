# find all topological sorts

import collections
def all_topological_sort(graph):
    def recur(path, inbound, seen, n, res):
        if len(path) == n:
            res += [path]
            return

        # seen.add(node)
        v = path[-1]
        for i in range(n):
            inbound[i] -= graph[v][i]

        for i in range(n):
            if not i in seen and inbound[i] == 0:
                recur(path + [i], inbound[::], seen | set([i]), n, res)

    n = len(graph)
    # number of inbound edges
    inbound = [0] * n

    # initialize the inbound count of all edges
    for i in range(n):
        for j in range(n):
            inbound[j] += graph[i][j]

    # scan for the 0 inbound nodes to start with
    res = []
    for i in range(n):
        if inbound[i] == 0:
            recur([i], inbound[::], set([i]), n, res)

    print(res)
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
    all_topological_sort(graph)