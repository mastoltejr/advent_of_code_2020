import re

with open("day2_in","r") as f:
    lines = f.readlines()

def read_pass(pw):
    matches = re.match(r"(\d+)-(\d+) (.): (.*)", pw)
    lower, upper = int(matches.group(1)), int(matches.group(2))
    char, password = matches.group(3), matches.group(4)
    return (lower, upper, char, password)


def p1_valid(pw):
    lower, upper, char, password = read_pass(pw)
    return lower <= password.count(char) <= upper


def p2_valid(pw):
    first, second, char, password = read_pass(pw)
    return (password[first - 1] == char) ^ (password[second - 1] == char)

print('p1: ', sum(map(p1_valid, lines)))
print('p2: ', sum(map(p2_valid, lines)))