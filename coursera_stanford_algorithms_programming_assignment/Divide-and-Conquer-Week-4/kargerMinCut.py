import random
import copy
import time
records = []


def random_contraction(G):
    while len(G) > 2:  # bugfix: > not >=
        v = random.choice(list(G.keys()))
        u = random.choice(list(G[v]))
        for n in G[u]:
            if n != v:
                G[v].append(n)
                G[n].append(v)
            G[n].remove(u)
        del G[u]
    min_cut = len(G[list(G.keys())[0]])
    records.append(min_cut)


def graph_from_file(filename):
    graph = {}
    with open(filename) as file:
        for line in file:
            n = int(line.split()[0])
            e = []
            for l in line.split()[1:]:
                e.append(int(l))
            graph[n] = e
        file.close()
    return graph


if __name__ == '__main__':
    G = graph_from_file('/Users/yangyaoxian/Downloads/kargerMinCut.txt')
    # deepcopy: http://stackoverflow.com/questions/17873384/deep-copy-a-list-in-python
    start_time = time.time()  # compute the running time
    for i in range(1, 50):    # set executing times
        G1 = copy.deepcopy(G)
        random_contraction(G1)
    end_time = time.time()
    running_time = (end_time - start_time) / 50
    # print(G)
    # print(G1)
    print(min(records))
    print("running time(one loop) is", running_time, "sec")