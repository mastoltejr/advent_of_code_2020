import re
from collections import defaultdict

bagGraph = defaultdict(list)
bagGraph2 = defaultdict(list)

with open("day7.txt","r") as f:
    rules = f.read().splitlines()
    for rule in rules:
        parts = re.match(r"^(\w+\s?\w*) bags contain (.+)",rule,re.IGNORECASE)
        (parent, children) = parts.groups()
        children = re.findall(r"(\d+) (\w+\s?\w*) bags?[,.]?",children,re.IGNORECASE)
        for (num,bag) in children:
            bagGraph[bag].append(parent)
            bagGraph2[parent].append((num,bag))


def bagSearch(start,bags=set()):
    if start in bags:
        return bags
    bags.add(start)
    for bag in bagGraph[start]:
       bagSearch(bag,bags)
    return bags

print(len(bagSearch('shiny gold'))-1)

def bagSearch2(start):
    total = 1
    for (num,bag) in bagGraph2[start]:
       total += int(num)*bagSearch2(bag)
    return total

print(bagSearch2('shiny gold') - 1)