def binary_search(instructions):
    start, end = 0, 2 ** len(instructions) - 1
    for instruction in instructions:
        mid = (end + start) // 2
        start, end = (mid + 1, end) if instruction else (start, mid)
    assert start == end
    return start

def assign_2_id(assignment):
    instructions = [char in {'B','R'} for char in assignment]
    row, col = binary_search(instructions[:-3]), binary_search(instructions[-3:])
    return row *  8 + col

with open("day5_in","r") as f:
    assignments = f.read().splitlines()
    ids = {assign_2_id(assignment) for assignment in assignments}
    print('p1:', max(ids))
    for id in ids:
        if id + 1 not in ids and id + 2 in ids:
            print('p2:', id + 1)
            break
    