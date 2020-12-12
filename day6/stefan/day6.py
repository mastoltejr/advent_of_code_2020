from functools import reduce, partial

def common(grouping_function, group):
    answers = reduce(lambda shared, person: grouping_function(shared, person), 
                     map(set, group.splitlines()))
    return len(answers)

with open("day6_in","r") as f:
    groups = f.read().split('\n\n')
    print('p1:', sum(map(partial(common, set.union), groups)))
    print('p2:', sum(map(partial(common, set.intersection), groups)))
