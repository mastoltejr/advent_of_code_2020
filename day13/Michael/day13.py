from math import inf,ceil,gcd
with open('day13/Michael/day13.txt','r') as f:
    rows = f.read().splitlines()

timestamp = int(rows[0])
buses = [int(bus) for bus in rows[1].replace(',x','').split(',')]

earliest = (0,inf)
for bus in buses:
    difference = ceil(timestamp/bus)*bus-timestamp
    (id,diff) = earliest
    if difference < diff:
        earliest = (bus,difference)

print(earliest[0]*earliest[1])

## part 2
buses = [(int(bus),e) for e,bus in enumerate(rows[1].split(',')) if bus != 'x']

print(buses)

guess = 0

def check(n):
    for id,minAfter in buses[1:]:
        if n%id != minAfter:
            return False
    return True

inc = 17*449
total = 23356980000000
while not check(total-17):
    if total%10000000 == 0:
        print(total)
    total += inc
    if total >= 900000000000000:
        break
print('=============')
print(total)