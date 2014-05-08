#!/usr/bin/env python
import sys
import networkx as nx
import matplotlib.pyplot as plt

def get_sorted_list(list, type=int):
    sorted_list = []
    for item in list:
        sorted_list.append(int(item))

    sorted_list = sorted(sorted_list)

    if type == str:
        for i in range(len(sorted_list)):
            sorted_list[i] = str(sorted_list[i])

    return sorted_list

def main(list):
    sorted_int_list = get_sorted_list(list)
    sorted_str_list = get_sorted_list(list, type=str)

    G = nx.DiGraph()

    pos = {}
    for i, item in enumerate(sorted_int_list):
        pos[item] = (i+1, 1)
    for i, item in enumerate(list):
        pos[item] = (i+1, 0)

    G.add_edges_from(zip(sorted_int_list, sorted_str_list))

    nx.draw_networkx(G, pos)
    plt.show()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        list = sys.argv[1].split(',')
        main(list)
    else:
        print("Usage: %s [list]" % sys.argv[0])
