import re

regex = re.compile('^([0-9]+)-([0-9]+) ([a-z]{1}): ([a-z]+)')


def sledPolicy():
    correct_count = 0
    with open('input2.txt', 'r') as policies:
        for policy in policies:
            (min_count, max_count, letter, password) = regex.search(policy).groups()
            count = password.count(letter)
            if count >= int(min_count) and count <= int(max_count):
                correct_count += 1
    return correct_count


def tobogganPolicy():
    correct_count = 0
    with open('input2.txt', 'r') as policies:
        for policy in policies:
            (min_count, max_count, letter, password) = regex.search(policy).groups()
            min_count = int(min_count)
            max_count = int(max_count)
            if min_count > len(password) or max_count > len(password):
                next
            elif (password[min_count-1] == letter or password[max_count-1] == letter) and password[min_count-1] != password[max_count-1]:
                correct_count += 1
    return correct_count


print(sledPolicy())
print(tobogganPolicy())
