from functools import reduce, partial

def slide(map, size_x, size_y):
    height, width = len(map), len(map[0])
    steps = range(height // size_x)
    accumulator = lambda count, step: count + map[step * size_x][step * size_y % width]
    return reduce(accumulator, steps)

with open("day3_in","r") as f:
    lines = f.read().splitlines()
    map = [[square == '#' for square in line] for line in lines]
    exact_slide = partial(slide, map)
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    print('p1: ',exact_slide(1, 3))
    accumulator = lambda product, slope: product * exact_slide(*slope)
    print('p2: ',reduce(accumulator, slopes, 1))