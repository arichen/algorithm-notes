# topological sort using the stack method

def topological_sort(graph):
    def visit(node, seen, stack, n):
        seen.add(node)

        for i in range(n):
            if not i in seen and graph[node][i]:
                visit(i, seen, stack, n)

        stack.append(node)

    n = len(graph)
    stack = []
    seen = set()
    for i in range(n):
        if not i in seen:
            visit(i, seen, stack, n)

    return stack[::-1]

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
    res = topological_sort(graph)
    print(res)