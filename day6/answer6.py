with open("day6.txt", "r") as f:
    groups = f.read().split('\n\n')
    anyoneCount = 0
    everyoneCount = 0
    for answers in groups:
        anyoneCount += len(set(answers.replace('\n', '')))
        answerSplit = answers.split('\n')
        everyoneCount += len(set(answerSplit[0]).intersection(*answerSplit))
    print(anyoneCount)
    print(everyoneCount)
