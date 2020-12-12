from collections import defaultdict
import re
regex = re.compile(r"(\w{3}) ([+-]\d+)",re.IGNORECASE)
operations = defaultdict(lambda: False)

with open('day8/Michael/day8.txt','r') as f:
    instructions = f.read().splitlines()

accumulator = 0
index = 0
while (not operations[index]):
    if operations[index]:
        break

    (command, num) = regex.match(instructions[index]).groups()
    #print(index,command,num,operations[index],accumulator)
    operations[index] = True
    if command == 'acc':
        accumulator += int(num)
    elif command == 'jmp':
        index += int(num) - 1
    index += 1

print(accumulator)

index = len(instructions)-1
operations = defaultdict(lambda: False)

while not operations[index]:
    (command, num) = regex.match(instructions[index]).groups()
    operations[index] = True
    next_index = index - int(num)
    if command == 'jmp':
        if operations[next_index] or next_index < 0 or next_index > len(instructions):
            break
        index -= int(num)
    index -= 1

(command, num) = regex.match(instructions[index]).groups()
print(instructions[index])
instructions[index] = '{} {}{}'.format('nop' if command == 'jmp' else 'jmp','+' if int(num) >= 0 else '-',abs(int(num)))
print(instructions[index])

accumulator = 0
index = 0
while (not operations[index]):
    if operations[index]:
        break

    (command, num) = regex.match(instructions[index]).groups()
    #print(index,command,num,operations[index],accumulator)
    operations[index] = True
    if command == 'acc':
        accumulator += int(num)
    elif command == 'jmp':
        index += int(num) - 1
    index += 1

print(accumulator)
