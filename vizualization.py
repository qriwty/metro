import time
import matplotlib.pyplot as plt
import networkx as nx

from metro import *


def get_time(n=52):
    test_get = Metro(setup_environment=False)

    start_get = time.time()

    for i in range(n):
        for j in range(n):
            test_get.get_path(i, j)

    end_get = time.time()

    return end_get - start_get


def find_time(n=52):
    test_find = Metro(setup_environment=False)

    start_find = time.time()

    for i in range(n):
        for j in range(n):
            test_find.find_path(i, j)

    end_find = time.time()

    return end_find - start_find


def cache_comparison(filename=None):
    s = 52

    stations = []
    find_array = []
    get_array = []

    for i in range(s + 1):
        stations.append(i)

        find = find_time(i)
        get = get_time(i)

        find_array.append(find)
        get_array.append(get)

    plt.title('Cached vs Uncached')

    plt.xlabel("Stations (n)")
    plt.ylabel("Time (s)")

    plt.plot(stations, get_array, label="Cached")
    plt.plot(stations, find_array, label="Uncached")

    plt.legend()

    plt.draw()
    if filename is not None:
        plt.savefig(filename)

    plt.show()


def print_graph(resolution=2048, dpi=256, filename=None):
    metro = Metro()

    G = nx.DiGraph(directed=True)

    for node in metro.metro_map.keys():
        name = metro.get_station_name(node)
        G.add_node(node)

        for neighbour in metro.metro_map[node]["CONNECTIONS"]:
            neighbour_name = metro.get_station_name(neighbour[0])
            G.add_edge(name,
                       neighbour_name,
                       minlen=neighbour[1].total_seconds(),
                       weight=neighbour[1].total_seconds(),
                       label=time.strftime("%M:%S", time.gmtime(neighbour[1].total_seconds())),
                       type="regular")

        if metro.metro_map[node]["TYPE"] == "TRANSFER":
            for transfer in metro.metro_map[node]["TRANSFER"]:
                transfer_name = metro.get_station_name(transfer[0])
                G.add_edge(name,
                           transfer_name,
                           minlen=transfer[1].total_seconds(),
                           weight=transfer[1].total_seconds(),
                           label='',
                           type="transfer")

    dpi = dpi
    size = resolution

    plt.figure(figsize=(size / dpi, size / dpi), dpi=dpi)

    pos = nx.spring_layout(G)

    nx.draw_networkx_labels(G, pos, font_size=7)

    regular_edges = dict([((u, v), d['weight'])
                          for u, v, d in G.edges(data=True) if d['type'] == 'regular'])
    transfer_edges = dict([((u, v), d['weight'])
                          for u, v, d in G.edges(data=True) if d['type'] == 'transfer'])

    nx.draw_networkx_edges(G, pos, edgelist=regular_edges, edge_color='green', connectionstyle='arc3, rad = 0.1')
    nx.draw_networkx_edges(G, pos, edgelist=transfer_edges, edge_color='red', connectionstyle='arc3, rad = 0.1')

    plt.tight_layout()

    plt.draw()

    if filename is not None:
        plt.savefig(filename, dpi=dpi, bbox_inches="tight")

    plt.show()
    plt.close()


cache_comparison(filename="img/cache_comparison.png")

print_graph(resolution=2048 * 3, dpi=312, filename="img/graph.png")
