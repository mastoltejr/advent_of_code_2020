from collections import defaultdict
numbers = [0]
with open('day10.txt','r') as f:
    for row in f:
        numbers.append(int(row))

numbers = sorted(numbers)
numbers.append(numbers[len(numbers)-1]+3)

joltages = defaultdict(lambda: 0)
options = defaultdict(lambda: 0)
options[0] = 1

for i in range(0,len(numbers)-1):
    joltages[numbers[i+1]-numbers[i]] += 1
    for o in [1,2,3]:
        if options[numbers[i]-o] > 0:
            options[numbers[i]] += options[numbers[i]-o]


print(joltages[1]*joltages[3])
print(options[numbers[len(numbers)-1]-3])