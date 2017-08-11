import sys
import threading


def graph_from_file(filename):
    graph = {}
    for k in range(1, 875715):
        graph[k] = []
    with open(filename) as file:
        for line in file:
            n = int(line.split()[0])
            e = int(line.split()[1])
            graph[n].append(e)
        file.close()
    return graph


def dfs(graph, i):
    global t
    node_explored.add(i)
    leaders[i] = s
    if i in graph:
        for j in graph[i]:
            if j not in node_explored:
                dfs(graph, j)
    t += 1
    f[i] = t


def dfs_loop(graph):
    global f, s, leaders, node_explored
    node_explored = set()
    f = {}

    for node in reversed(range(len(graph)+1)):
        if node not in node_explored:
            s = node
            dfs(graph, node)


def reverse(graph):
    new_graph = defaultdict(list)
    for u in graph:
        for v in graph[u]:
            new_graph[v].append(u)
    return new_graph


if __name__ == '__main__':
    threading.stack_size(67108864)
    sys.setrecursionlimit(2 ** 20)

    t = 0
    s = None
    leaders = {}
    G = graph_from_file('SCC.txt')
    G_rev = reverse(G)

    dfs_loop(G_rev)
    G_ft = {}
    for node in range(1, len(G) + 1):
        tmp = []
        for i in G[node]:
            tmp.append(f[i])
        G_ft[f[node]] = tmp

    leaders = {}
    dfs_loop(G_ft)
    print(list(leaders.values()))


