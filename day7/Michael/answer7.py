import re
from collections import defaultdict

bagGraph = defaultdict(list)

with open("day7/Michael/day7.txt","r") as f:
    rules = f.read().splitlines()
    for rule in rules:
        parts = re.match(r"^(\w+\s?\w*) bags contain (.+)",rule,re.IGNORECASE)
        (parent, children) = parts.groups()
        #print(parts.groups())
        children = re.findall(r"(\d+) (\w+\s?\w*) bags?[,.]?",children,re.IGNORECASE)
        for (num,bag) in children:
            bagGraph[bag].append(parent)

print(bagGraph['shiny gold'])


def bagSearch(start,bags=set()):
    if start in bags:
        return bags
    bags.add(start)
    for bag in bagGraph[start]:
       bagSearch(bag,bags)
    return bags

x = bagSearch('shiny gold')
print(len(x) - 1)