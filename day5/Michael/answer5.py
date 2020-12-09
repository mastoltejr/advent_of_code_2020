import math
def findSeat(path,mapping):
    (front,back) = mapping
    minValue = 0
    maxValue = 2**len(path)-1
    for letter in path:
        if letter == front:
            maxValue -= (maxValue-minValue)//2 + 1
        elif letter == back:
            minValue += (maxValue-minValue)//2 + 1
        else:
            raise Exception('invalid Mapping')
    return maxValue if letter == front else minValue

minID = math.inf
maxID = -math.inf
maxID = 0
seatIDs = set([])
with open('day5.txt','r',newline='\n') as f:
    seats = f.read().splitlines()
    for seat in seats:
        seatID = findSeat(seat[:7],('F','B'))*8+findSeat(seat[7:],('L','R'))
        minID = seatID if seatID < minID else minID
        maxID = seatID if seatID > maxID else maxID
        seatIDs.add(seatID)

print(maxID)
seatOptions = set(range(minID,maxID))
print(seatOptions-seatIDs)