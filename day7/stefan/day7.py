from collections import defaultdict
import re


def parse_rule(rule):
    outer, inner = re.match(r"^(.+) bags contain (.+).",rule).groups()
    return outer, re.findall(r"(\d+) (\w+ \w+) bag[s]?[,]?", inner)
    

def build_graph(rules, backwards = False):
    graph = defaultdict(list)
    for outer, inner in map(parse_rule, rules):
        for count, bag in inner:
            if backwards:
                graph[bag].append((outer, 0))
            else:
                graph[outer].append((bag, int(count)))
    return graph


def traverse_topo(current, topology, visited = None):
    visited = {} if visited is None else visited
    if current not in visited:
        total = 0
        for bag, count in topology[current]:
            subtotal, _ = traverse_topo(bag, topology, visited)
            total += count * (subtotal + 1)
        visited[current] = total
    return visited[current], len(visited)

with open("day7_in","r") as f:
    rules = f.read().splitlines()
    _ , distinct_parents = traverse_topo('shiny gold', build_graph(rules, True))
    total_children, _ = traverse_topo('shiny gold', build_graph(rules))
    print('p1: ', distinct_parents - 1)
    print('p2: ', total_children)